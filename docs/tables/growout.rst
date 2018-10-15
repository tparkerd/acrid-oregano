.. _growout:

``growout``
===========

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``growout_id``", "``integer``", ""
    "``growout_name``", "``varchar``", ""
    "``growout_population``", "``integer``", "see :ref:`population.population_id <population>`"
    "``growout_location``", "``integer``", "see :ref:`location.location_id <location>`"
    "``year``", "``integer``", ""
    "``growout_growout_type``", "``integer``", "see :ref:`growout_type.growout_type_id <growout_type>`"

Diagram
-------

.. image:: /_static/img/growout.png

.. seealso::

  :ref:`Growout Type <growout_type>`, :ref:`Location <location>`, :ref:`Population <population>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: growout table
    :end-before: --
