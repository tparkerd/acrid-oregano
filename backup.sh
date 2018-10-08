#!/bin/bash
pg_dump -d baxdb --username=baxdb_owner --quote-all-identifiers > "/opt/dbBackups/BaxDBbackups/BaxDB_dump_$(date +%Y.%m.%d-%H.%M.%S).sql"