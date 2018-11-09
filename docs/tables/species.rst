.. _species:

``species``
===========

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``species_id``", "``integer``", ""
    "``shortname``", "``varchar``", "Nickname/alias for species for everyday use"
    "``binomial``", "``varchar``", "Two-term name using `Binomial nomenclature <https://en.wikipedia.org/wiki/Binomial_nomenclature>`_"
    "``subspecies``", "``varchar``", ""
    "``variety``", "``varchar``", ""

.. note::
  Subspecies and Variety do not seem to be in use at the moment.

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
