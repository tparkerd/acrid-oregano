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
sudo

###### END ROOT ######

sudo su postgres

cd $HOME
database_types=("prod" "staging" "qa")
installation_basedir="/usr/pgsql-9.6/lib/"
for dt in "${database_types[@]}"
do
    # Run the following command as postgres user
    # Make sure to reset the installation directory
    pg_installdir="$(find ${installation_basedir} -type d -iname "*${dt}" -print)"
    database_name=${pg_installdir##*/}
    # Change to your home directory, out of /root
    # For each database type
    psql -q -U postgres -f "${pg_installdir}/ddl/setup.sql"
    psql -q -U postgres -f "${pg_installdir}/tinyint.sql"
    psql -q -U postgres -f "${pg_installdir}/ddl/createtables.sql"
    psql -q -U postgres -f "${pg_installdir}/ddl/updatepermissions.sql"
    owner_name="pgwasdb_${dt}_owner"
    printf "host\t${database_name}\t${owner_name}\t0.0.0.0/0\tmd5\n" >> "$(psql -t -P "format=unaligned" -c "SHOW hba_file;")"
done
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