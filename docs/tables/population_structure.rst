.. _population_structure:

``population_structure``
========================

.. warning::
    ``population_structure_file_path`` is not known to be a local or remote location

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``population_structure_id``", "``integer``", ""
    "``population_structure_algorithm``", "``integer``", "see :ref:`population_structure_algorithm.population_structure_algorithm_id <population_structure_algorithm>`"
    "``population_structure_file_path``", "``text``", "[need additional info]"

Diagram
-------

.. image:: /_static/img/population_structure.png

.. seealso::

  :ref:`GWAS Run <gwas_run>`, :ref:`Population Structure Algorithm <population_structure_algorithm>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: population_structure table
    :end-before: --
