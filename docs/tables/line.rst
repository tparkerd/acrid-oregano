.. _line:

``line``
========

Attributes
-----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``line_id``", "``integer``", ""
    "``line_name``", "``varchar``", ""
    "``line_population``", "``integer``", "see :ref:`population.population_id <population>`"

Constraints
-----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "", "``unique``", "``line_name``, ``line_population``"

Diagram
-------

.. image:: /_static/img/line.png

.. seealso::

  :ref:`Genotype <genotype>`, :ref:`Genotype Version <genotype_version>`, :ref:`Phenotype <phenotype>`, :ref:`Population <population>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: line table
    :end-before: --
