\connect postgres

SET client_min_messages TO WARNING;
DROP DATABASE IF EXISTS pgwasdb_commit_prod;
DROP ROLE IF EXISTS pgwasdb_owner;

CREATE ROLE pgwasdb_owner WITH
    LOGIN
    CREATEROLE
    ENCRYPTED PASSWORD 'password'
    ;
CREATE DATABASE pgwasdb_commit_prod
    WITH OWNER = pgwasdb_owner
    ENCODING = 'UTF-8'
    ;