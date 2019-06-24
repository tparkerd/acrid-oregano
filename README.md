# acrid-oregano
PostgreSQL Database System for GWAS in the Baxter Lab

Credit - Ryan Lichtenwalter https://github.com/rlichtenwalter/pgsql_genomics

# Environment
Operating System: CentOS 7
RDBMS: PostgreSQL 9.6

# Installation

## Docker Installation

    # Start docker container
    docker-compose up [-d]

## Manual Installation

The following command will install the GWAS database onto a CentOS 7 System.
The first portion is just to install PostgreSQL 9.6 onto the system, so it this 
is already installed, you may skip it and continue with pulling the database's
code from this repo.

Also, the command require both root access and the postgres user. Installing
PostgreSQL should create the postgres user for you, but if it does not, you will
need to create one manually. See your Linux distribution's documentation on how
to do so.

```bash
# Run the following commands as root
yum -y update && \
yum -y install wget unzip gcc perl dos2unix epel-release && \
yum -y install yum install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm && \
yum -y install postgresql96 postgresql96-server postgresql96-contrib postgresql96-libs postgresql96-devel && \
git clone -b development --single-branch https://github.com/tparkerd/acrid-oregano.git && \
export PATH=/usr/pgsql-9.6/bin:$PATH && \
postgresql96-setup initdb && \
pg_libdir=$(pg_config --pkglibdir) && \
pg_installdir="$pg_libdir/baxdb" && \
mkdir -p -m 755 "$pg_installdir"

systemctl enable postgresql-9.6.service && \
systemctl start postgresql-9.6.service 


cd ./c &&
make &&
cp array_multi_index.so imputed_genotype.so summarize_variant.so "$pg_installdir" && \
chmod -R 755 "$pg_installdir" 

cd ./lib/tinyint-0.1.1 &&
make &&
sed -i -e '1i\\\connect baxdb' -e 's|$libdir\/tinyint|$libdir/baxdb/tinyint|g' tinyint.sql && \
cp tinyint.so "$pg_installdir" && \
chmod -R 755 "$pg_installdir" && \
cp tinyint.sql "$pg_installdir"
printf "Created TINYINT SQL and moved to $pg_installdir.\n"

cd ../../ && \
cp ./ddl/setup.sql ./ddl/createtables.sql ./ddl/updatepermissions.sql "$pg_installdir"

# Run the following command as postgres user

# Make sure to reset the installation directory
pg_installdir="/usr/pgsql-9.6/lib/baxdb"
# Change to your home directory, out of /root
psql -q -U postgres -f "$pg_installdir/setup.sql"
psql -q -U postgres -f "$pg_installdir/tinyint.sql"
psql -q -U postgres -f "$pg_installdir/createtables.sql"
psql -q -U postgres -f "$pg_installdir/updatepermissions.sql"
sed -i "1s/^/local baxdb baxdb_owner trust\n/" "$(psql -t -P "format=unaligned" -c "SHOW hba_file;")"
psql -t -P "format=unaligned" -c "SELECT pg_reload_conf();"

# Update the postgresql.conf
# Change the listening addresses to listen for all
# listen_addresses = '*'
vi /var/lib/pgsql/9.6/data/postgresql.conf

# Update pg_hba.conf
# Change it so that it will listen for VirtualBox bridged connection
# host      all             all         10.0.0.0/0          md5
vi /var/lib/pgsql/9.6/data/pg_hba.conf

# Restart postgresql service to update listening addresses and host
# authentication
systemctl restart postgresql-9.6.service

# Open port 5432 (postgres)
firewall-cmd --permanent --add-port=5432/tcp
firewall-cmd --reload

```

## Additional Installation Information for Production, Staging, and Test databases
Install PostgreSQL as you would normally, but once you get to the section that 
requires actions to be performed by the `postgres` user, you will modify each
of the SQL files in `./ddl/` to reflect the database name and credentials that
will be used to connect to each instance of the database.

These may be installed into a single or multiple database clusters.