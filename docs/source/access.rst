.. _data_access:

***********
Data access
***********

Ulagam contains 4 terabytes of data and is stored in New York (Rusty cluster). The data can be accessed via Globus at `THIS LINK <https://app.globus.org/file-manager?origin_id=e0eae0aa-5bca-11ea-9683-0e56c063f437&origin_path=%2FUlagam%2F>`__.

Globus
------

*Based on the data access documentation from* `Quijote <https://quijote-simulations.readthedocs.io/en/latest/access.html>`__

The data can be accessed through `globus <https://www.globus.org/>`__ at the publicly accessible link above. Note that to download the data to your local machine (e.g. laptop) you will need to install the globus connect personal. For further details see `here <https://github.com/franciscovillaescusa/Quijote-simulations/blob/master/documentation/globus.md>`_. We now provide some simple instructions to use globus.

The simplest way to transfer data is to use the `globus <https://www.globus.org>`_ graphical environment. Just type the above names in collection (e.g. Quijote_simulations for the data in San Diego) or click the associated link. You will need to choose where the data is being moved in the other collection (e.g. your laptop or another supercomputer). Once the collection points are set, select the data you want to transfer and destination folder and click on Start.

In some cases, there are so many files in a given directory, that globus may not be able to list them all and will return an error. If this is the case, it is advisable to use the path line. For instance, if by clicking one of the subfolders you get a timeout error, you may want to just type in the path line: ``/EQ_m/0`` to access an individual simulation. This may be particularly true for the "fiducial" sims, of which there are 2000.

The globus `Command Line Interface (CLI) <https://docs.globus.org/cli/>`_ also provides additional, more flexible ways to use globus and transfer data. The first step is to install the CLI package, if you don't have it. Next, login into globus by typing in a terminal

.. code-block:: bash

   globus login

Then, the following command allows you to determine the associated endpoint:

.. code-block:: bash
		
   globus endpoint search "Quijote_simulations"

::
   
   ID                                   | Owner                     | Display Name       
   ------------------------------------ | ------------------------- | -------------------
   c42757fe-d570-11e9-98e2-0a63aa6b37da | fvillaescusa@globusid.org | Quijote_simulations


You should do the same to know the endpoint of the machine to which you are transferring the data to. You can then explore the filesystem of the Quijote simulations (or your machine) as:

.. code-block:: bash
		
   ep1=c42757fe-d570-11e9-98e2-0a63aa6b37da
   globus ls $ep1:/Ulagam/EQ_m/0/pkdgrav_output/


The above command will list the content in the ``/Ulagam/EQ_m/0/pkdgrav_output/`` directory. A single file can be transfered as:

.. code-block:: bash
   
   ep1=c42757fe-d570-11e9-98e2-0a63aa6b37da
   ep2=ddb59af0-6d04-11e5-ba46-22000b92c6ec
   globus transfer $ep1:/Ulagam/EQ_m/0/pkdgrav_output/Density_shell.log $ep2:/My_data/EQ_m/0/pkdgrav_output/Density_shell.log --label "single file transfer"


Where ep2 should be the endpoint of the machine where you are transfering the data. Entire folders can be moved as follows:

.. code-block:: bash
		
   ep1=c42757fe-d570-11e9-98e2-0a63aa6b37da
   ep2=ddb59af0-6d04-11e5-ba46-22000b92c6ec
   globus transfer $ep1:/Ulagam/EQ_m/0/ $ep2:/My_data/EQ_m/0/  --recursive --label "single folder transfer"

Many folders can be moved with a single command as

.. code-block:: bash

   ep1=c42757fe-d570-11e9-98e2-0a63aa6b37da
   ep2=ddb59af0-6d04-11e5-ba46-22000b92c6ec
   globus transfer $ep1:/Ulagam/fiducial/ $ep2:/Ulagam/fiducial/ --batch --label "CLI 10 folders" < folders.txt


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
