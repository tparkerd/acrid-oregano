######
Extras
######

***************
Web Application
***************

Before development began on the PostgreSQL BaxDB database, some work was done to set up a web application that would eventually connect to the BaxDB backend.  This code can certainly be configured to work with the PostgreSQL database, but it will first require an upgrade to a newer version of ``Flask ~>0.12.3``. The ``models.py`` module can be modified to match the ``models.py`` in the BaxDB code.  The web application code is on `GitHub`_.  The web application code is on adriatic in ``/var/www/GWASdb``.  It can be accessed from within the Danforth Center network at ``adriatic.ddpsc.org`` (click “GWAS Database” on the landing page).

.. note::
  Since the web appliation is in very early development, it may be worth starting from scratch and using a more familiar framework.

.. _GitHub: https://github.com/mwohl/BaxDB_flask

.. literalinclude:: ../dml/database.ini
    :caption: Example database.ini
    :name: database.ini
    :language: ini
    :linenos:
