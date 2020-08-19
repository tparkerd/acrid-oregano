database_types=("prod" "staging" "qa")
installation_basedir="/usr/pgsql-9.6/lib/"
for dt in "${database_types[@]}"; do
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
  printf "host\t${database_name}\t${owner_name}\t0.0.0.0/0\tmd5\n" >>"$(psql -t -P "format=unaligned" -c "SHOW hba_file;")"
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
printf "host\tall\tall\t10.0.0.0/0\tmd5" >>/var/lib/pgsql/9.6/data/pg_hba.conf
sed -i "s/local\s+all\s+all\s+peer/local\tall\tall\tmd5/gmi" /var/lib/pgsql/9.6/data/pg_hba.conf
sed -i -E 's/(local\s+all\s+all\s+)\S+/\1trust/gmi' /var/lib/pgsql/9.6/data/pg_hba.conf
