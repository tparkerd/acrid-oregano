\connect pgwasdb_commit_staging

GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO pgwasdb_commit_staging_owner;

GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO pgwasdb_commit_staging_owner;