.. _data_products:

***********
Data products
***********

The current release of the Ulagam simulations contains the following data products: (1) Density fields/shells, and (2) 3D matter power spectrum. The halo catalogs are not yet publicly available.


=============
Density field/shell
=============

The primary product of this suite are HEALPix maps of the counts of particles. This can be easily converted to the overdensity delta as

.. code-block:: bash
  
    overdensity = counts/mean(counts) - 1


The maps are provided in the "fits.fz" format, which is a fits file compressed with the fpack/unpack (https://heasarc.gsfc.nasa.gov/fitsio/fpack/) These do not need to be unzipped by the user. The astropy fits class in python automatically reads in fits.fz files as

.. code-block:: bash

    from astropy.io import fits
    import numpy as np

    counts  = fits.open(<path_to_fits_fz>)[1].data
    density = counts/np.mean(counts) - 1

All particles have the same mass, so converting from counts to density can be done using the raw counts (as the mass unit cancels out) and does not need info on the mass per particle. 

=============
3D Matter power spectrum
=============

Pkdgrav3 can internally compute the 3D power spectrum of the snapshots. The  ".pk" files are exactly this. The units are h/Mpc for k and (Mpc/h)^3 for P(k). The data can be read out as


.. code-block:: bash

    import numpy as np

    out = np.loadtxt(<path_to_pk_file>)
    k   = out[:, 0] #in h/Mpc
    Pk  = out[:, 1] #in (Mpc/h)^3

.. note::

    There is also a file of the name ``Density_shell.00020'' etc. and these are empty files. Normally they are binary files containing all the 3D particle snapshot information. However, since we do not save snapshots these files are empty.
