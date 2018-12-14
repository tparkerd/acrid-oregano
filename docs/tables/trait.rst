.. _trait:

``trait``
=========

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``trait_id``", "``integer``", ""
    "``trait_name``", "``varchar``", "E.g., height, weight"
    "``measurement_unit``", "``varchar``", "E.g., millimeters, milligrams"
    "``measurement_device``", "``varchar``", "Tool used to take measurement"
    "``description``", "``text``", ""

Diagram
-------

.. image:: /_static/img/trait.png

.. seealso::

  :ref:`GWAS Run <gwas_run>`, :ref:`Phenotype <phenotype>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: trait table
    :end-before: --
