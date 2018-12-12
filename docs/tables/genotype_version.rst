.. _genotype_version:

``genotype_version``
====================

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``genotype_version_id``", "``integer``", ""
    "``genotype_version_name``", "``varchar``", ""
    "``genotype_version``", "``varchar``", ""
    "``reference_genome``", "``integer``", "see :ref:`line.line_id <line>`"
    "``genotype_version_population``", "``integer``", "see :ref:`population.population_id <population>`"

Constraints
-----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "", "``unique``", "``genotype_version``, ``reference_genome``"

Diagram
-------

.. image:: /_static/img/genotype_version.png


.. seealso::

  :ref:`Genotype <genotype>`, :ref:`GWAS Run <gwas_run>`, :ref:`Line <line>`, :ref:`Population <population>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: genotype_version table
    :end-before: --