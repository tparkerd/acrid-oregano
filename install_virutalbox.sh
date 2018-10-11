#!/bin/bash

git clone https://github.com/tparkerd/BaxDB.git && cd BaxDB && ./install.sh

# Update the postgresql.conf
# Change the listening addresses to listen for all
# listen_addresses = '*'
sudo vi /var/lib/pgsql/9.5/data/postgresql.conf

# Update pg_hba.conf
# Change it so that it will listen for VirtualBox bridged connection
# host      all             all         10.0.0.0/0          md5
sudo vi /var/lib/pgsql/9.5/data/pg_hba.conf


# Open port 5432 (postgres)
sudo firewall-cmd --permanent --add-port=5432/tcp
sudo firewall-cmd --reload

# Verify that postgresql server is running
sudo systemctl restart postgres-9.5.service && sudo systemctl status postgresql-9.5.service
