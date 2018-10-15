.. _location:

``location``
============

Attributes
----------

.. csv-table::
    :header: "Name","Type","Comment"
    :widths: 20, 10, 70

    "``location_id``", "``integer``", ""
    "``country``", "``varchar``", ""
    "``state``", "``varchar``", ""
    "``city``", "``varchar``", ""
    "``code``", "``varchar``", ""

Diagram
-------

.. image:: /_static/img/location.png

.. seealso::

  :ref:`Growout <growout>`

DDL
---

.. literalinclude:: ../../ddl/createtables.sql
    :language: postgresql
    :linenos:
    :start-after: location table
    :end-before: --
