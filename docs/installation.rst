.. _installation:

############
Installation
############

For development and testing, you have two options. If you have access to `Docker <https://www.docker.com>`_, it is the fastest way to spin up a copy of the database. Otherwise, it is best to create a copy of the database in a virtual machine. `VirtualBox`_ works great for our purposes.

******
Docker
******

Dependencies
============
    - `Docker <https://www.docker.com>`_
    - `Docker Composer <https://docs.docker.com/compose/install/>`_

Step-by-Step Guide
==================
    # Install `Docker <https://www.docker.com>`_
    # Install `Docker Composer <https://docs.docker.com/compose/install/>`_
    # Pull copy of Docker image ``docker pull tparkerd/gwas`` (https://hub.docker.com/r/tparkerd/gwas/)
    # Clone GitHub repo ``git clone https://github.com/tparkerd/gwas_database.git``

*****
Setup
*****

Dependencies
============
    - `VirtualBox`_
    - `CentOS 7 Minimal`_

Step-by-Step Guide
==================

    #. Install `VirtualBox`_
    #. Create new virtual machine (VM)
    #. Install `CentOS 7 Minimal`_ onto the VM
    #. Start VM and log in as ``root``
    #. Install ``git`` onto VM with ``yum -y install git``
    #. Create user ``postgres`` with ``useradd postgres``
    #. Download source code and run ``install.sh``

If you have already created a VM, copy and paste the following code to complete steps 5 through 7.

.. code-block:: bash
    :linenos:

    yum -y install git
    useradd postgres
    git clone https://github.com/tparkerd/gwas_database.git &&
    cd gwas_database &&
    ./install.sh

.. note::
    If you want to just initialize the database without installing PostgreSQL, simply run ``init_db.sh``.

**Done!** At this point, you should be able to access the database using the PostgreSQL client, ``psql``. You can verify that the database was correctly initialized by logging in as ``postgres``.

.. code-block:: bash

    sudo -u postgres psql -U postgres -d baxdb
 
Configuration
=============

In order to access the database from another machine, you'll need to alter PostgreSQL's host-based authentication file, ``pg_hba.conf``. See PostgreSQL's `documentation`_ for additional info. If you have followed the step-by-step guide, in order to connect to the database from your host machine, you will need to update two configuration files, ``pg_hba.conf`` and ``postgresql.conf``. In addition, make sure to open the port PostgreSQL listens on (default: ``5432``).

.. code-block:: bash
    :linenos:

    # Update the postgresql.conf
    # Change the listening addresses to listen for all
    # listen_addresses = '*'
    vi /var/lib/pgsql/9.6/data/postgresql.conf

    # Update pg_hba.conf
    # Change it so that it will listen for VirtualBox bridged connection
    # host      all             all         10.0.0.0/0          md5
    vi /var/lib/pgsql/9.6/data/pg_hba.conf

    # Restart postgresql service to update listening addresses and host
    # authentication
    systemctl restart postgresql-9.6.service

    # Open port 5432 (postgres)
    firewall-cmd --permanent --add-port=5432/tcp
    firewall-cmd --reload

.. hint::
    Make sure that your VM's network adapter is set as 'Attached to **Bridged Adapter**'.

Importing Data
==============

*todo*

Troubleshooting
===============

*todo*

************
Source Files
************

GitHub Repository: https://github.com/tparkerd/gwas_database.git

The ``init_db.sh`` script performs some configuration and installs the custom C libraries, ``array_multi_index``, ``imputed_genotype``, and ``summarize_variant`` from Lichtenwalter and the `tinyint library`_ from Hitoshi Harada. It then runs three .sql files.

:``./ddl/setup.sql``: creates the PostgreSQL database and the database owner role
:``./lib/tinyint-0.1.1/tinyint.sql``: configures the custom tinyint type to be used in the PostgreSQL database
:``./ddl/createtables.sql``: creates all tables, foreign keys, and indices in the current database schema

:``./dml``: contains code for inserting data into the database and for finding items within the database.  There is also a module, parsinghelpers.py, which contains some helper functions used in parsing data from files to be inserted using the functions in insert.py.  The script insertMaize282.py contains most of the code that was actually executed to load in the Maize282 dataset.  It can be used as a guideline for applying the functions in the insert/find/parsinghelpers modules to insert additional datasets in the future.

The GitHub repository is cloned in ``/opt/BaxDB`` on ``adriatic``.

.. _documentation: https://www.postgresql.org/docs/9.6/static/auth-pg-hba-conf.html

.. _tinyint library: https://github.com/umitanuki/tinyint-postgresql
.. _VirtualBox: https://www.virtualbox.org/
.. _CentOS 7 Minimal: https://www.centos.org/download/
