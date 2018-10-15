.. _chromosome:

``chromosome``
==============

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``chromosome_id``", "``integer``", ""
    "``chromosome_name``", "``varchar``", ""
    "``chromosome_species``", "``integer``", "see :ref:`species.species_id <species>`"

Constraints
-----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "", "``unique``", "``chromosome_name``, ``chromosome_species``"

Diagram
-------

.. image:: /_static/img/chromosome.png

.. seealso::

  :ref:`Genotype <genotype>`, :ref:`GWAS Result <gwas_result>`, :ref:`Species <species>`, :ref:`Variant <variant>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: chromosome table
    :end-before: --