Datazilla metrics
=================

This package implements statistical methods useful for `Datazilla`_.

.. _Datazilla: https://github.com/mozilla/datazilla

Currently the only methods implemented are Welch's t-test
(``dzmetrics.ttest.welchs_ttest``) and Benjamini-Hochberg false discovery rate
control (``dzmetrics.ttest.fdr``). See the docstrings of those functions for
details.


Installation
------------

Datazilla-metrics requires `scipy`_ and thus also `numpy`_. If installed via
`pip`_, these must be installed sequentially (first numpy then scipy), and
scipy requires the BLAS and LAPACK libraries and a Fortran compiler. For
instance, to get everything in place on an Ubuntu 12.04 system, run::

   sudo apt-get install libblas-dev liblapack-dev gfortran
   pip install numpy
   pip install scipy

It may be easier to just use the system packages for numpy and scipy (``sudo
apt-get install python-scipy``); in that case to import it from within a
`virtualenv`_ you'd need to create the virtualenv with the
``--system-site-packages`` flag.


.. _scipy: http://www.scipy.org
.. _numpy: http://numpy.scipy.org
.. _pip: http://www.pip-installer.org
.. _virtualenv: http://www.virtualenv.org
