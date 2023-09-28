.. _data_products:

***********
Data products
***********

The current release of the Ulagam simulations contains the following data products:


=============
1. Density field/shell
=============

The primary product of this suite are HEALPix maps of the counts of particles. This can be easily converted to the overdensity delta as

.. code-block:: bash
  
    overdensity = counts/mean(counts) - 1


The maps are provided in the "fits.fz" format, which is a fits file compressed with the fpack/unpack (https://heasarc.gsfc.nasa.gov/fitsio/fpack/) These do not need to be unzipped by the user. 
The astropy fits class in python automatically reads in fits.fz files as

.. code-block:: bash

    from astropy.io import fits
    d = fits.open(<path_to_density_shell>)[1].data
