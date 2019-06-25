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
###### ROOT ######
yum -y update && \
yum -y install wget unzip gcc perl dos2unix epel-release && \
yum -y install yum install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm && \
yum -y install postgresql96 postgresql96-server postgresql96-contrib postgresql96-libs postgresql96-devel && \
git clone -b development --single-branch https://github.com/tparkerd/acrid-oregano.git pgwasdb && \
database_types=("prod" "staging" "qa") && \
pushd pgwasdb && \
commit_hash="$(git rev-parse --short=7 HEAD)" && \
popd 

# For each database instance, (prod, staging, qa), create the database and 
# install the TINYINT library
for dt in "${database_types[@]}"
do
    cp -rv pgwasdb "$dt"
    database_name="pgwasdb_${commit_hash}_${dt}"
    pushd "$dt"
    sed -i "s/pgwasdb_commit_type/${database_name}/g" `find . -type f`
    export PATH=/usr/pgsql-9.6/bin:$PATH
    postgresql96-setup initdb
    pg_libdir=$(pg_config --pkglibdir)
    pg_installdir="$pg_libdir/${database_name}"
    mkdir -vp -m 755 "$pg_installdir"
    systemctl enable postgresql-9.6.service
    systemctl start postgresql-9.6.service
    popd 

    pushd "./$dt/c"
    make
    cp -v array_multi_index.so imputed_genotype.so summarize_variant.so "$pg_installdir"
    chmod -Rv 755 "$pg_installdir" 
    popd

    pushd "./$dt/lib/tinyint-0.1.1"
    make
    sed -i -e "1i\\\connect ${database_name}" -e "s|$libdir\/tinyint|$libdir/${database_name}/tinyint|g" tinyint.sql
    cp -v tinyint.so "$pg_installdir"
    chmod -Rv 755 "$pg_installdir"
    cp -v tinyint.sql "$pg_installdir"
    printf "Created TINYINT SQL and moved to $pg_installdir.\n"
    popd

    # At this point, you will run these commands once for each instance of the database
    # If you want to create a qa, staging, and production, you'll need to modify
    # the credentials and name of the database in the following files. I suggest
    # using the `sed` command to swap out each of to reflect the commit version and
    # its username and password. I'm considering each of the users as a role

    # cp ./ddl/setup.sql ./ddl/createtables.sql ./ddl/updatepermissions.sql "$pg_installdir"
    cp -rv ./pgwasdb/ddl/ "$pg_installdir"

done

###### END ROOT ######

sudo su postgres

database_types=("prod" "staging" "qa")
for dt in "${database_types[@]}"
do
    # Run the following command as postgres user
    # Make sure to reset the installation directory

    pg_installdir="/usr/pgsql-9.6/lib/${dt}"
    # Change to your home directory, out of /root
    # For each database type
    for folder in $(find "$pg_installdir/ddl")
    do
        psql -q -U postgres -f "$folder/setup.sql"
        psql -q -U postgres -f "$folder/tinyint.sql"
        psql -q -U postgres -f "$folder/createtables.sql"
        psql -q -U postgres -f "$folder/updatepermissions.sql"
    done
done
sed -i "1s/^/local baxdb baxdb_owner trust\n/" "$(psql -t -P "format=unaligned" -c "SHOW hba_file;")"
psql -t -P "format=unaligned" -c "SELECT pg_reload_conf();"

# Update the postgresql.conf
# Change the listening addresses to listen for all
# listen_addresses = '*'
sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" /var/lib/pgsql/9.6/data/postgresql.conf

# Update pg_hba.conf
# Change it so that it will listen for VirtualBox bridged connection
# host      all             all         10.0.0.0/0          md5
printf "host\tall\tall\t10.0.0.0/0\tmd5" >> /var/lib/pgsql/9.6/data/pg_hba.conf

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