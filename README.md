# acrid-oregano
PostgreSQL Database System for GWAS in the Baxter Lab

Credit - Ryan Lichtenwalter https://github.com/rlichtenwalter/pgsql_genomics

# Environment
Operating System: CentOS 7

RDBMS: PostgreSQL 9.6

# Live Database Instance

The live version of the database is stored on a virtual machine hosted by the 
Data Science Facility at the Danforth Center.

There are three instances of the database: _production_, _staging_, and _QA_. Each instance 
has a respective owner. The owner of production has full access to the staging and QA servers as well. The owner of staging has full access to the QA server too.

Officially, the only means for connecting to the database is through an R package. Its working title is [Deathy Parsley](https://github.com/tparkerd/deathly-parsley). However, you can connect to the database so long as you are accessing the VM from the Center's
network (e.g., VPN or SSH tunnel through Data Science Facility).

However, you can access the database directly to view its contents. Below are the credentials for accessing the QA instance of the database. Its contents do not reflect the master copy of data stored in the database; that is stored in the production server. The R package access data stored in the production server. The QA server is subject to purging during development and testing.

#### QA Database Server Credentials
```
Hostname: 10.5.1.102
Database: pgwasdb_3011261_qa
Username: pgwasdb_qa_owner
Password: password
Port:     5432
```

## Remote Access

In order to access the database server, you must be connected to the Center's network. The easiest way to do this is via the Center's VPN–`asavpn.ddpsc.org`.

If you would like to connect to the database through a database management like, such as [DBeaver](https://dbeaver.io/), then you can connect via an SSH tunnel. You will use your account with the Data Science Facility.

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
popd && \
echo "PATH=/usr/pgsql-9.6/bin:$PATH" >> ~/.bashrc && source ~/.bashrc && \
pg_libdir=$(pg_config --pkglibdir) && \
postgresql96-setup initdb && \
systemctl enable postgresql-9.6.service && \
systemctl start postgresql-9.6.service


database_types=("prod" "staging" "qa")

# For each database instance, (prod, staging, qa), create the database and 
# install the TINYINT library
for dt in "${database_types[@]}"
do
    cp -r pgwasdb "$dt"
    database_name="pgwasdb_${commit_hash}_${dt}"
    pushd "$dt"
    echo -e "\e[104mChanging database reference name in each of the DDL files...\e[0m"
    for f in $(find ./ddl -type f)
        do
            sed -i "s/pgwasdb_commit_type/${database_name}/g" "$f"
            sed -i "s/pgwasdb_owner/pgwasdb_${dt}_owner/g" "$f"
        done
    echo "Done!\e[0m"
    popd 

    pg_installdir="$pg_libdir/${database_name}"
    echo "Installation directory: ${pg_installdir}"
    mkdir -vp -m 755 "$pg_installdir"
 
    pushd "./$dt/c"
    make
    echo "Copying the library files into ${pg_installdir}"
    cp -v array_multi_index.so imputed_genotype.so summarize_variant.so "$pg_installdir"
    chmod -R 755 "$pg_installdir" 
    popd
 
    pushd "./$dt/lib/tinyint-0.1.1"
    make
    cp -v tinyint.so "$pg_installdir"
    chmod -R 755 "$pg_installdir"
    cp -v tinyint.sql "$pg_installdir"
    echo -e "\e[104mChanging database reference name in <tinyint.sql>\e[0m"
    sed -i -e "1i\\\\\connect ${database_name}" -e "s|$libdir\/tinyint|$libdir/$database_name/tinyint|g" "${pg_installdir}/tinyint.sql"
    popd

    # At this point, you will run these commands once for each instance of the database
    # If you want to create a qa, staging, and production, you'll need to modify
    # the credentials and name of the database in the following files. I suggest
    # using the `sed` command to swap out each of to reflect the commit version and
    # its username and password. I'm considering each of the users as a role
    cp -rv ./${dt}/ddl/ "$pg_installdir"

done

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
psql -c "GRANT pgwasdb_staging_owner TO pgwasdb_prod_owner;"
psql -c "GRANT pgwasdb_qa_owner TO pgwasdb_staging_owner;"


# Update the postgresql.conf
# Change the listening addresses to listen for all
# listen_addresses = '*'
sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" /var/lib/pgsql/9.6/data/postgresql.conf

# Update pg_hba.conf
# Change it so that it will listen for VirtualBox bridged connection
# host      all             all         10.0.0.0/0          md5
printf "host\tall\tall\t10.0.0.0/0\tmd5" >> /var/lib/pgsql/9.6/data/pg_hba.conf
sed -i "s/local\s+all\s+all\s+peer/local\tall\tall\tmd5/gmi" /var/lib/pgsql/9.6/data/pg_hba.conf
sed -i -E 's/(local\s+all\s+all\s+)\S+/\1md5/gmi' /var/lib/pgsql/9.6/data/pg_hba.conf
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
