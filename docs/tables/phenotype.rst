.. _phenotype:

``phenotype``
=============

.. note::
    The value is a p-value for the trait provided by a ``5.mergedWeightNorm.LM.rankAvg.longFormat.csv`` file. 

Attributes
-----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``phenotype_id``", "``integer``", ""
    "``phenotype_line``", "``integer``", "see :ref:`line.line_id <line>`"
    "``phenotype_trait``", "``integer``", "see :ref:`trait.trait_id <trait>`"
    "``phenotype_value``", "``varchar``", "p-value for trait given a line"

Diagram
-------

.. image:: /_static/img/phenotype.png

.. seealso::

  :ref:`Line <line>`, :ref:`Trait <genotype_version>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: phenotype table
    :end-before: --
