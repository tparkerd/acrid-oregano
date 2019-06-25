\connect pgwasdb_commit_qa

GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO pgwasdb_commit_qa_owner;

GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO pgwasdb_commit_qa_owner;