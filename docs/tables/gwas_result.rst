.. _gwas_result:

``gwas_result``
===============

.. note::
    Probably the most important table

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``gwas_result_id``", "``integer``", ""
    "``gwas_result_chromosome``", "``integer``", "see :ref:`chromosome.chromosome_id <chromosome>`"
    "``basepair``", "``integer``", ""
    "``gwas_result_gwas_run``", "``integer``", "see :ref:`gwas_run.gwas_run_id <gwas_run>`"
    "``pval``", "``numeric``", ""
    "``cofactor``", "``numeric``", ""
    "``_order``", "``numeric``", ""
    "``null_pval``", "``numeric``", ""
    "``model_added_pval``", "``numeric``", ""
    "``model``", "``text``", ""
    "``pcs``", "``integer[]``", ""

Constraints
-----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "", "``unique``", "``gwas_result_chromosome``, ``basepair``, ``gwas_result_gwas_run``, ``model``"

Diagram
-------

.. image:: /_static/img/gwas_result.png

.. seealso::

  :ref:`Chromosome <chromosome>`, :ref:`GWAS Run <gwas_run>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: gwas_result table
    :end-before: --
