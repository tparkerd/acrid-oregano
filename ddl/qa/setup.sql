\connect postgres

SET client_min_messages TO WARNING;
DROP DATABASE IF EXISTS pgwasdb_commit_qa;
DROP ROLE IF EXISTS pgwasdb_commit_qa_owner;

CREATE ROLE pgwasdb_commit_qa_owner WITH
    LOGIN
    CREATEROLE
    ENCRYPTED PASSWORD 'password'
    ;
CREATE DATABASE pgwasdb_commit_qa
    WITH OWNER = pgwasdb_commit_qa_owner
    ENCODING = 'UTF-8'
    ;