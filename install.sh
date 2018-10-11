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
yum -y install https://download.postgresql.org/pub/repos/yum/9.5/redhat/rhel-7-x86_64/pgdg-centos95-9.5-3.noarch.rpm
yum -y install postgresql95 postgresql95-server postgresql95-contrib postgresql95-libs postgresql95-devel
export PATH=/usr/pgsql-9.5/bin:$PATH
postgresql95-setup initdb
systemctl enable postgresql-9.5.service
systemctl start postgresql-9.5.service

# Run script that creates the TINYINT datatype and then create the tables
./setup.sh
