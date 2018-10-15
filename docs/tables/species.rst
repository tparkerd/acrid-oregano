.. _species:

``species``
===========

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``species_id``", "``integer``", ""
    "``shortname``", "``varchar``", ""
    "``binomial``", "``varchar``", ""
    "``subspecies``", "``varchar``", ""
    "``variety``", "``varchar``", ""

Diagram
-------

.. image:: /_static/img/species.png

.. seealso::

  :ref:`Chromosome <chromosome>`, :ref:`Popluation <population>`, :ref:`Variant <variant>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: species table
    :end-before: --
