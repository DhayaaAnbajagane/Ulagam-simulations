.. _data_products:

***********
Data products
***********

The original release of the Ulagam simulations contain the following data products: (1) Density fields/shells, and (2) 3D matter power spectrum.

The new simulations introduced in Anbajagane & Lee (2025a) and Anbajagane & Lee (2025b) contain a number of products: (1) Full-sky density shells, (2) 3D matter power spectrum, (3) 3D matter bispectrum, (4) 3D density fields, (5) rockstar catalogs.

You can see what simulations are available at `the simulations page <simulations.md>`_


=============
Density field/shell
=============

The primary product of this suite are HEALPix maps of the counts of particles. This can be easily converted to the overdensity delta as

.. code-block:: bash
  
    overdensity = counts/mean(counts) - 1


The maps are provided in the "fits.fz" format, which is a fits file compressed with the `fpack/funpack <https://heasarc.gsfc.nasa.gov/fitsio/fpack/>`_. Since the counts are a discrete (i.e. integer) quantity, they can be losslessly compressed with fpack. These compressed maps do not need to be uncompressed by the user. Instead, the astropy fits class in python can automatically read in fits.fz files as

.. code-block:: bash

    from astropy.io import fits
    import numpy as np

    counts  = fits.open(<path_to_fits_fz>)[1].data
    density = counts/np.mean(counts) - 1

All particles have the same mass, so converting from counts to density can be done using the raw counts (as the mass unit cancels out) and does not need info on the mass per particle. 
For the original Ulagam sims, there are also files of the name "Density_shell.00020" etc. and these are empty files. Normally they are binary files containing all the 3D particle snapshot information. However, since we do not save snapshots these files are empty.


=============
Lensing convergence shells
=============

Instead of providing the raw lensing shells (which cannot be losslessly compressed due to their continuous nature and thus have large storage footprints) we provide scripts that can quickly (<5 min) can construct all lensing shells in the simulation using the density shells mentioned above. We also provide scripts to convert the lensing convergence, "kappa", to the lensing shears "gamma 1, gamma 2".

    1. Convert density to convergence `HERE <https://github.com/DhayaaAnbajagane/Ulagam-simulations/blob/68f29a37de7d650a0dda8c0b4d624331cdb89239/scripts/kappa.py>`__
    2. Convert convergence to shears `HERE <https://github.com/DhayaaAnbajagane/Ulagam-simulations/blob/e68aa1bc3569d4660db0948cd08f7fe888c902ca/scripts/kappa2shear.py>`__


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

    There is also a file of the name "Density_shell.00020" etc. and these are empty files. Normally they are binary files containing all the 3D particle snapshot information. However, since we do not save snapshots these files are empty.




=============
3D Matter bispectrum
=============

We compute the 3D bispectrum for each snapshot using the estimator of Scoccimaro 2015. The units are h/Mpc for k and (Mpc/h)^3 for P(k). The data can be read out as

.. code-block:: bash

    import numpy as np

    Bk = np.load(<path to Bispectrum_estimate.npy file>)
    k  = np.load(<path to Bispectrum_kbin.npy file>) #in h/Mpc
    
.. note::

The quantity Bk has shape (Nlimits, Nk) where Nlimits = 3 are the squeezed, equilateral, and folded limits. See Anbajagane & Lee (2025a) for details.

=============
3D Density field
=============

The density field is also saved for each snapshot, on a grid of 256^3. We save the counts of particles in a cell, and this can be losslely compressed using the npz format. You can read these files out as,

.. code-block:: bash

    import numpy as np

    counts = np.load(<path to DensityField.npz file>)['density']
    rho    = counts / np.mean(counts) - 1

.. note::

=============
Rockstar catalogs
=============

We run mpi-rockstar on each of the 100 snapshots from the simulations. You can read these files out as,

.. code-block:: bash

    import numpy as np

    halos  = np.loadtxt(<path to .rockstar file>)

.. note::

The column names are detailed in the header of this file, which you can view through just opening this like a text file (which it is). 
    
