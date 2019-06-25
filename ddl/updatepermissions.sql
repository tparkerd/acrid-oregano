\connect pgwasdb_commit_type

GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO pgwasdb_owner;

GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO pgwasdb_owner;