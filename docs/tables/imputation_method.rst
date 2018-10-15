.. _imputation_method:

``imputation_method``
=====================

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``imputation_method_id``", "``integer``", ""
    "``imputation_method``", "``text``", "Name of the method used. E.g., ???"

Diagram
-------

.. image:: /_static/img/imputation_method.png

.. seealso::

  :ref:`GWAS Run <gwas_run>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: imputation_method table
    :end-before: --
