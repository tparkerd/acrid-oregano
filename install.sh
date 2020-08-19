#!/bin/bash
# Installation script for pgwasdb (i.e., GWAS database)
# Operating system: CentOS 7
# RDBMS: PostgreSQL 9.6
# NOTE: Make sure to run this under `root` user

if [ "$EUID" -ne 0 ]; then
  echo "Must be installed as root."
  exit
fi

# Install the dependencies
yum -y update
yum -y install wget unzip gcc perl dos2unix
yum -y install epel-release

# Install PostgreSQL 9.6 if not already installed
systemctl status postgresql-9.6
psql_status=$?
if [ $psql_status -ne 0 ]; then
  # Attempt to start service if not running
  if [ $psql_status -eq 3 ]; then
    systemctl start postgresql-9.6.service || {
      printf "Unable to start postgresql-9.6 Aborting.\n" 1>&2
      exit 1
    }
  fi

  # PostgreSQL 9.6 is not installed
  if [ $psql_status -eq 4 ]; then
    dnf install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm
    dnf -qy module disable postgresql
    dnf install -y postgresql96-server postgresql96-devel
    export PATH="/usr/pgsql-9.6/bin/:$PATH"
    postgresql96-setup initdb
    systemctl enable postgresql-9.6 || {
      printf "Unable to enable postgresql-9.6 Aborting.\n" 1>&2
      exit 1
    }
    systemctl start postgresql-9.6 || {
      printf "Unable to start postgresql-9.6 Aborting.\n" 1>&2
      exit 1
    }
  fi
fi

# Install extentions into PostgreSQL
# Verify that pg_config is accessible to the user
command -v pg_config >/dev/null 2>&1 || {
  printf "Command 'pg_config' is required but not found in path. Make sure PostgreSQL client tools are installed. Aborting.\n" 1>&2
  exit 1
}

# Compile TINYINT extention and install it into PostgreSQL
pg_libdir=$(pg_config --pkglibdir)
pg_installdir="$pg_libdir/pgwasdb"
mkdir -p -m 755 "$pg_installdir" || {
  printf "Unable to create directory '$pg_installdir' for installation into PostgreSQL. Aborting.
\n" 1>&2
  exit 1
}

(
  cd ./c &&
    make &&
    cp array_multi_index.so imputed_genotype.so summarize_variant.so "$pg_installdir" &&
    chmod -R 755 "$pg_installdir"
  printf "Created array_multi_index, imputed_genotype, and summarize_variant.\n"
)

(
  cd ./lib/tinyint-0.1.1 &&
    make &&
    sed -i -e '1i\\\connect pgwasdb' -e 's|$libdir\/tinyint|$libdir/pgwasdb\/tinyint|g' tinyint.sql &&
    cp tinyint.so "$pg_installdir" &&
    chmod -R 755 "$pg_installdir" &&
    cp tinyint.sql "$pg_installdir" # move the tinyint.sql into a location accessible by postgres user
  printf "Created TINYINT SQL and moved to $pg_installdir.\n"
)

# Move the remaining SQL scripts to a location accessible by postgres user
cp ./ddl/setup.sql ./ddl/createtables.sql ./ddl/updatepermissions.sql "$pg_installdir"
printf "Relocated $(ls ./ddl) to $pg_installdir.\n"

sudo -u postgres psql -q -U postgres -f "$pg_installdir/setup.sql" || {
  printf "Unable to perform setup for 'pgwasdb' database as user 'postgres'. Check UNIX account privileges and pg_hba.conf. Aborting.\n" 1>&2
  exit 1
}
sudo -u postgres psql -q -U postgres -f "$pg_installdir/tinyint.sql" || {
  printf "Unable to add 'tinyint' type to database 'pgwasdb'. Aborting.\n" 1>&2
  exit 1
}
sudo -u postgres psql -q -U postgres -f "$pg_installdir/createtables.sql" || {
  printf "Unable to perform setup for 'pgwasdb' database as user 'postgres'. Check UNIX account privileges and pg_hba.conf. Aborting.\n" 1>&2
  exit 1
}
sudo -u postgres psql -q -U postgres -f "$pg_installdir/updatepermissions.sql" || {
  printf "Unable to perform setup for 'pgwasdb' database as user 'postgres'. Check UNIX account privileges and pg_hba.conf. Aborting.\n" 1>&2
  exit 1
}
sed -i "1s/^/local pgwasdb pgwasdb_owner trust\n/" "$(sudo -u postgres psql -t -P "format=unaligned" -c "SHOW hba_file;")"
sudo -u postgres psql -t -P "format=unaligned" -c "SELECT pg_reload_conf();"

# Remove the installation files from the database directory
rm -f "$pg_installdir/setup.sql $pg_installdir/createtables.sql $pg_installdir/updatepermissions.sql"
printf "Removed the temporary SQL files for building 'pgwasdb' database.\n"
printf "Setup completed successfully.\n"
printf "Please consider checking your 'pg_hba.conf' file to alter permissions to access the database. Permissions are currently set as 'local pgwasdb pgwasdb_owner trust'.\n"

# At this point, I was to be able to run
# pip ./dml/setup.py install
# It may be worth distributing the package once the project has come far enough along
#  Therefore, you'd be able to just run `pip install gwas_database` or something
# to that effect
