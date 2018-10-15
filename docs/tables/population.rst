.. _population:

``population``
==============

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``population_id``", "``integer``", ""
    "``population_name``", "``varchar``", ""
    "``population_species``", "``integer``", "see :ref:`species.species_id <species>`"

Diagram
-------

.. image:: /_static/img/population.png

.. seealso::

  :ref:`Genotype Version <genotype_version>`, :ref:`Growout <growout>`, :ref:`Line <line>`, :ref:`Species <species>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: population table
    :end-before: --
