.. _variant:

``variant``
===========

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``variant_id``", "``integer``", ""
    "``variant_species``", "``integer``", "see :ref:`species.species_id <species>`"
    "``variant_chromosome``", "``integer``", "see :ref:`chromosome.chromosome_id <chromosome>`"
    "``variant_pos``", "``integer``", ""

Contraints
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "", "``unique``", "``variant_species``, ``variant_chromosome``, ``variant_pos``"

Diagram
-------

.. image:: /_static/img/variant.png

.. seealso::

  :ref:`Chromosome <chromosome>`, :ref:`Species <species>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: variant table
    :end-before: --