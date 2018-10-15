.. _phenotype:

``phenotype``
=============

Attributes
-----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``phenotype_id``", "``integer``", ""
    "``phenotype_line``", "``integer``", "see :ref:`line.line_id <line>`"
    "``phenotype_trait``", "``integer``", "see :ref:`trait.trait_id <trait>`"
    "``phenotype_value``", "``varchar``", ""

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
