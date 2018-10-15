.. _database:

###############
Database Schema
###############

The decision to use PostgreSQL 9.6 was in part due to `a paper published`_ by `Ryan Lichtenwalter`_ et al. in which he outlines an efficient method for storing and querying genotypic data.

********
Diagrams
********
- `Entity-Relationship Model`_

.. _Entity-Relationship Model: _static/erdiagram.png

******
Tables
******

Below is a list of all the tables that comprise the :abbr:`GWAS(Genome-wide association study)` database. Each subsection provides the identifier for the table, a description, a list of its fields, and any association to other tables.

.. toctree::
  :maxdepth: 1
  :glob:

  /tables/*

External Resources
  - `Genotypic Data in Relational Database: Efficient Storage and Rapid Retrieval`_ --- Ryan N. Lichtenwalter, Katerina, Zorina-Lichtenwalter, and Luda Diatchenko
  - `pgsql_genomics`_ --- Ryan N. Lichtenwalter
  - `Ryan Lichtenwalter`_ --- GitHub

.. _Ryan Lichtenwalter: https://github.com/rlichtenwalter
.. _a paper published: https://drive.google.com/file/d/10G2juH9zrgI-TmEJzp7EKhg2ewQIs0LI/view
.. _Genotypic Data in Relational Database\: Efficient Storage and Rapid Retrieval: https://drive.google.com/file/d/10G2juH9zrgI-TmEJzp7EKhg2ewQIs0LI/view
.. _pgsql_genomics: https://github.com/rlichtenwalter/pgsql_genomics








