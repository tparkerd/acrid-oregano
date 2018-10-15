.. _kinship:

``kinship``
===========

Attributes
-----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``kinship_id``", "``integer``", ""
    "``kinship_algorithm``", "``integer``", "see :ref:`kinship_algorithm.kinship_algorithm_id <kinship_algorithm>`"
    "``kinship_file_path``", "``text``", ""

Diagram
-------

.. image:: /_static/img/kinship.png

.. seealso::

  :ref:`GWAS Run <gwas_run>`, :ref:`Kinship Algorithm <kinship_algorithm>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: kinship table
    :end-before: --
