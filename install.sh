#/bin/bash

# Candidate installation script for BaxDB (i.e., GWAS database)
# Operating system: CentOS 7
# RDBMS: PostgreSQL 9.5
# NOTE: Make sure to run this under `root` user

# Known issues: 
# During ./setup.sh, the build throws the error that a parameter is unused (postgresql v9.5)

# Install the dependencies
yum -y update
yum -y install wget unzip gcc perl dos2unix
yum -y install epel-release
yum -y install https://download.postgresql.org/pub/repos/yum/9.4/redhat/rhel-7-x86_64/pgdg-centos94-9.4-3.noarch.rpm
yum -y install postgresql94 postgresql94-server postgresql94-contrib postgresql94-libs postgresql94-devel
export PATH=/usr/pgsql-9.4/bin:$PATH
postgresql94-setup initdb
systemctl enable postgresql-9.4.service
systemctl start postgresql-9.4.service

# Run script that creates the TINYINT datatype and then create the tables
./setup.sh
