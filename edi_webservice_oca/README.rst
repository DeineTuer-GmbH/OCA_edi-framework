==============
EDI WebService
==============

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:fb40b5df23b69cb369c0753c50d539fd7667551141ee75cd9cf1933353941ff6
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fedi--framework-lightgray.png?logo=github
    :target: https://github.com/OCA/edi-framework/tree/17.0/edi_webservice_oca
    :alt: OCA/edi-framework
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/edi-framework-17-0/edi-framework-17-0-edi_webservice_oca
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/edi-framework&target_branch=17.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

Plug webservice module within EDI framework. Allows to configure attach
webservices on an EDI backend and/or on an exchange type.

**Table of contents**

.. contents::
   :local:

Configuration
=============

Go to "EDI -> Config -> Backends" and edit or create one. Find the tab
"Webservice" and add a webservice. On the webservice record you can
specify all the general parameters to connect to the service (see
webservice README for more details).

If you want to take full control on if/how the webservice is used you
can do it via exchange type's advanced settings.

Hence, assuming your webservice has a URL configured as
\`\ https://my.endpoint/%7Bpath%7D\ \`:

::

   components:
     send:
       usage: webservice.send  # or any custom component usage inheriting from this
       work_ctx:
         webservice:
           method: post  # mandatory
           url_params:
             path: endpoint1/foo

For each call related to this type, you'll get a POST request against
https://my.endpoint/endpoint/foo.

``url_params`` can contain all the keys need for URL interpolation.

In addition, you can user ``url`` to override the full url used for the
call per exchange type.

If you want to send data as bytes you can use the option send_as_bytes
like:

::

   [...]
         webservice:
           send_as_bytes: true
   [...]

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/edi-framework/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/edi-framework/issues/new?body=module:%20edi_webservice_oca%0Aversion:%2017.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Creu Blanca
* Camptocamp

Contributors
------------

- Enric Tobella <etobella@creublanca.es>
- Simone Orsi <simone.orsi@camptocamp.com>

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-etobella| image:: https://github.com/etobella.png?size=40px
    :target: https://github.com/etobella
    :alt: etobella
.. |maintainer-simahawk| image:: https://github.com/simahawk.png?size=40px
    :target: https://github.com/simahawk
    :alt: simahawk

Current `maintainers <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-etobella| |maintainer-simahawk| 

This module is part of the `OCA/edi-framework <https://github.com/OCA/edi-framework/tree/17.0/edi_webservice_oca>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
