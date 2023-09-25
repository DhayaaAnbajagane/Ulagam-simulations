.. _data_access:

***********
Data access
***********

Ulagam contains 4 terabytes of data and is stored in New York (Rusty cluster). The data can be accessed via Globus.

Globus
------

The data can be accessed through `globus <https://www.globus.org/>`__ by clicking in the links from the above table. Note that to download the data to your local machine (e.g. laptop) you will need to install the globus connect personal. For further details see `here <https://github.com/franciscovillaescusa/Quijote-simulations/blob/master/documentation/globus.md>`_. We now provide some simple instructions to use globus.

The simplest way to transfer data is to use the `globus <https://www.globus.org>`_ graphical environment. Just type the above names in collection (e.g. Quijote_simulations for the data in San Diego) or click the associated link. You will need to choose where the data is being moved in the other collection (e.g. your laptop or another supercomputer). Once the collection points are set, select the data you want to transfer and destiny folder and click in Start.

.. image:: Globus.png

In some cases, there are so many files in a given directory, that globus may not be able to list them all and will return an error. If this is the case, it is advisable to use the path line. For instance, if by clicking in Snapshots you get a time out error, you may want to just type in the path line: ``/Snapshots/`` or ``/~/Snapshots/``. This may show you the different content of the data and allow you to navigate it. You can also go to a given directory directly from there. E.g. to access the first realization of the fiducial cosmology, type in path: ``/Snapshots/fiducial/0/`` or ``/~/Snapshots/fiducial/0/``.

In some cases, the above option may not be desirable. For instance, imagine that you want to download all linear matter power spectra of the high-resolution latin-hypercube simulations. One of such files (realization 45) is located in ``/Snapshots/latin_hypercube_HR/45/ICs/Pk_mm_z=0.000.txt``, while the file for the realization 89 is located in ``/Snapshots/latin_hypercube_HR/89/ICs/Pk_mm_z=0.000.txt``.

Thus, to download all those files without involving downloading the full HR latin-hypercube folder, will require that you access each simulation folder, then the ICs folder and then transfer the file individually. For 2,000 files this is unpractical. For these situations, we recommend using the globus `Command Line Interface (CLI) <https://docs.globus.org/cli/>`_. The first step is to install the CLI package, if you don't have it. Next, login into globus by typing in a terminal

.. code-block:: bash

   globus login

Then, the following command allow you to determine the associated endpoint of the Quijote simulations:

.. code-block:: bash
		
   globus endpoint search "Quijote_simulations"

::
   
   ID                                   | Owner                     | Display Name       
   ------------------------------------ | ------------------------- | -------------------
   c42757fe-d570-11e9-98e2-0a63aa6b37da | fvillaescusa@globusid.org | Quijote_simulations


You should do the same to know the endpoint of the machine where you are transfering the data to. You can then explore the filesystem of the Quijote simulations (or your machine) as:

.. code-block:: bash
		
   ep1=c42757fe-d570-11e9-98e2-0a63aa6b37da
   globus ls $ep1:/Snapshots/latin_hypercube_HR/45/ICs/


The above command will list the content in the ``/Snapshots/latin_hypercube_HR/45/ICs/`` directory. A single file can be transfered as:

.. code-block:: bash
   
   ep1=c42757fe-d570-11e9-98e2-0a63aa6b37da
   ep2=ddb59af0-6d04-11e5-ba46-22000b92c6ec
   globus transfer $ep1:/Snapshots/latin_hypercube_HR/45/ICs/Pk_mm_z=0.000.txt $ep2:/Quijote_simulations/linear_Pk/45/Pk_mm_z=0.000.txt --label "single file transfer"


Where ep2 should be the endpoint of the machine where you are transfering the data. Entire folders can be moved as follows:

.. code-block:: bash
		
   ep1=c42757fe-d570-11e9-98e2-0a63aa6b37da
   ep2=ddb59af0-6d04-11e5-ba46-22000b92c6ec
   globus transfer $ep1:/Snapshots/latin_hypercube_HR/45/ICs $ep2:/Quijote_simulations/45/ICs  --recursive --label "single folder transfer"

Many folders can be moved with a single command as

.. code-block:: bash

   ep1=c42757fe-d570-11e9-98e2-0a63aa6b37da
   ep2=ddb59af0-6d04-11e5-ba46-22000b92c6ec
   globus transfer $ep1:/Snapshots/fiducial/ $ep2:/Quijote_simulations/fiducial/ --batch --label "CLI 10 folders" < folders.txt


where folders.txt is a text file containing

.. code-block:: bash
		
    --recursive 0 0
    --recursive 1 1
    --recursive 2 2
    --recursive 3 3
    --recursive 4 4
    --recursive 5 5
    --recursive 6 6
    --recursive 7 7
    --recursive 8 8
    --recursive 9 9

For more options and details see `Command Line Interface (CLI) <https://docs.globus.org/cli/>`_.
