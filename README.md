# Plant Genome-wide Association Study Database (PGWASDB)

PostgreSQL Database System for GWAS in the Baxter Lab

# Environment

|                  |                |
| ---------------- | -------------- |
| Operating System | Centos 7       |
| RDBMS            | PostgreSQL 9.6 |

# Live Database Instance

The live version of the database is stored on a virtual machine hosted by the
Data Science Facility at the Danforth Center.

There are three instances of the database: _production_, _staging_, and _QA_.
Each instance has a respective owner. The owner of production has full access to
the staging and QA servers as well. The owner of staging has full access to the
QA server too.

Officially, the only means for connecting to the database is through an R
package. Its working title is
[pgwasdbc](https://github.com/danforthcenter/pgwasdbc). However, you can
connect to the database so long as you are accessing the VM from the Center's
network (e.g., VPN or SSH tunnel through Data Science Facility).

However, you can access the database directly to view its contents. Below are
the credentials for accessing the QA instance of the database. Its contents do
not reflect the master copy of data stored in the database; that is stored in
the production server. The R package access data stored in the production
server. The QA server is subject to purging during development and testing.

#### QA Database Server Credentials

```txt
Hostname: 10.5.1.102
Database: pgwasdb_3011261_qa
Username: pgwasdb_qa_owner
Password: password
Port:     5432
```

## Remote Access

In order to access the database server, you must be connected to the Center's
network. The easiest way to do this is via the Center's VPN–`asavpn.ddpsc.org`.

If you would like to connect to the database through a database management like,
such as [DBeaver](https://dbeaver.io/), then you can connect via an SSH tunnel.
You will use your account with the Data Science Facility.

# Installation

## Manual Installation

The following command will install the GWAS database onto a CentOS 7 System.
The first portion is just to install PostgreSQL 9.6 onto the system, so it this
is already installed, you may skip it and continue with pulling the database's
code from this repo.

Also, the command require both root access and the postgres user. Installing
PostgreSQL should create the postgres user for you, but if it does not, you will
need to create one manually. See your Linux distribution's documentation on how
to do so.

```bash
# As root
git clone https://github.com/tparkerd/pgwasdb.git
bash pgwasdb/install.sh
```

## Additional Installation Information for Production, Staging, and Test databases

Install PostgreSQL as you would normally, but once you get to the section that
requires actions to be performed by the `postgres` user, you will modify each
of the SQL files in `./ddl/` to reflect the database name and credentials that
will be used to connect to each instance of the database.

These may be installed into a single or multiple database clusters.

## Credits

Ryan Lichtenwalter https://github.com/rlichtenwalter/pgsql_genomics
