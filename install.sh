#/bin/bash

# Candidate installation script for BaxDB (i.e., GWAS database)
# Operating system: CentOS 7
# RDBMS: PostgreSQL 9.6
# NOTE: Make sure to run this under `root` user

# Known issues: 
# During ./setup.sh, the build throws the error that a parameter is unused (postgresql v9.6)

# Install the dependencies
yum -y update
yum -y install wget unzip gcc perl dos2unix
yum -y install epel-release
yum -y install https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm
yum -y install postgresql96 postgresql96-server postgresql96-contrib postgresql96-libs postgresql96-devel
export PATH=/usr/pgsql-9.6/bin:$PATH
postgresql96-setup initdb
systemctl enable postgresql-9.6.service
systemctl start postgresql-9.6.service

# Run script that creates the TINYINT datatype and then create the tables
./setup.sh
