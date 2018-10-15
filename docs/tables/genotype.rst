.. _genotype:

``genotype``
============

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``genotype_id``", "``integer``", ""
    "``genotype_line``", "``integer``", "see :ref:`line.line_id <line>`"
    "``genotype_chromosome``", "``integer``", "see :ref:`chromosome.chromosome_id <chromosome>`"
    "``genotype``", "``tinyint[]``", "Possible values: 0, 1, 2"
    "``genotype_genotype_version``", "``integer``", "see :ref:`genotype_version.genotype_version.id <genotype_version>`"

Constraints
-----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "", "``unique``", "``genotype_line``, ``genotype_chromosome``"

Diagram
-------

.. image:: /_static/img/genotype.png

.. seealso::

  :ref:`Chromosome <chromosome>`, :ref:`Genotype Version <genotype_version>`, :ref:`Line <line>`

DDL
---

.. warning::
    DDL differs from how foreign keys are written

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: genotype table
    :end-before: --