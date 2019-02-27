# acrid-oregano
PostgreSQL Database System for GWAS in the Baxter Lab

Credit - Ryan Lichtenwalter https://github.com/rlichtenwalter/pgsql_genomics

# Environment
Operating System: CentOS 7
RDBMS: PostgreSQL 9.6

# Installation

## Docker Installation

## Manual Installation
```bash
#!/bin/bash
git clone https://github.com/tparkerd/gwas_database.git &&
cd gwas_database &&
./install.sh

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
