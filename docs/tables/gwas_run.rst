.. _gwas_run:

``gwas_run``
============

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``gwas_run_id``", "``integer``", ""
    "``gwas_run_trait``", "``integer``", "see :ref:`trait.trait_id <trait>`"
    "``nsnps``", "``integer``", ""
    "``nlines``", "``integer``", ""
    "``gwas_run_gwas_algorithm``", "``integer``", "see :ref:`gwas_algorithm.gwas_algorithm_id <gwas_algorithm>`"
    "``gwas_run_genotype_version``", "``integer``", "see :ref:`genotype_version.genotype_version_id <genotype_version>`"
    "``missing_snp_cutoff_value``", "``numeric``", ""
    "``missing_line_cutoff_value``", "``numeric``", ""
    "``minor_allele_frequency_cutoff_value``", "``numeric``", ""
    "``gwas_run_imputation_method``", "``integer``", "see :ref:`imputation_method.imputation_method_id <imputation_method>`"
    "``gwas_run_kinship``", "``integer``", "see :ref:`kinship.kinship_id <kinship>`"
    "``gwas_run_population_structure``", "``integer``", "see :ref:`population_structure.population_structure_id <population_structure>`"

Constraints
-----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70
    :stub-columns: 1

    "", "``unique``", "``gwas_run_trait``, ``nsnps``, ``nlines``, ``gwas_run_gwas_algorithm``, ``gwas_run_genotype_version``, ``missing_snp_cutoff_value``, ``missing_line_cutoff_value``, ``minor_allele_frequency_cutoff_value``, ``gwas_run_imputation_method``, ``gwas_run_kinship``, ``gwas_run_population_structure``"


Diagram
-------

.. image:: /_static/img/gwas_run.png

.. seealso::

  :ref:`GWAS Result <gwas_result>`, :ref:`Genotype Version <genotype_version>`, :ref:`GWAS Algorithm <gwas_algorithm>`, :ref:`Imputation Method <imputation_method>`, :ref:`Kinship <kinship>`, :ref:`Population Structure <population_structure>`, :ref:`Trait <trait>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: gwas_run table
    :end-before: --
