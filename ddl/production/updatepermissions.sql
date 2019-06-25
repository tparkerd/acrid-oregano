\connect pgwasdb_commit_prod

GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO pgwasdb_owner;

GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO pgwasdb_owner;