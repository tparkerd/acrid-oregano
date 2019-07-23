.. _genotype_version:

``genotype_version``
====================

The genotype version identifies a specific line as a reference genome. This is defined using an assembly and 
annoation. The assembly is the entire genome line that was sequence beforehand. The annoation is the mapping
between trait and sequence. The trait-sequence mapping is beyond the scope of this database.

.. note::
    In its current state, the reference genome indirectly refers to genotype which holds the VCF allele calls
    on specific genomes. It is not certain if the actual contents of the :ref:`genotype <genotype>` table
    reflects the actual sequence. As far as I know, there is not a way to transform the allele calls (.012)
    back to its original sequence (ATCG).

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``genotype_version_id``", "``integer``", ""
    "``genotype_version_assembly_name``", "``varchar``", "(e.g., B73 RefGen_v4)"
    "``genotype_version_annotation_name``", "``varchar``", "(e.g., AGPv4)"
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