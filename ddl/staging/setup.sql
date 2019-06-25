\connect postgres

SET client_min_messages TO WARNING;
DROP DATABASE IF EXISTS pgwasdb_commit_staging;
DROP ROLE IF EXISTS pgwasdb_commit_staging_owner;

CREATE ROLE pgwasdb_commit_staging_owner WITH
    LOGIN
    CREATEROLE
    ENCRYPTED PASSWORD 'password'
    ;
CREATE DATABASE pgwasdb_commit_staging
    WITH OWNER = pgwasdb_commit_staging_owner
    ENCODING = 'UTF-8'
    ;