import healpy as hp
import numpy as np

ell, emm = hp.Alm.getlm(lmax=2048)

kappaE = map_that_I_use
kappaB = np.zeros_like(kappaE) #This is zero

with np.errstate(invalid = 'ignore', divide = 'ignore'):
    alms   = hp.map2alm(kappaE, lmax = 2048, pol=False, use_pixel_weights = True, iter = 0)
    kalmsE = alms/(ell * (ell + 1.) / (ell + 2.) / (ell - 1)) ** 0.5

    alms   = hp.map2alm(kappaB, lmax = 2048, pol=False, use_pixel_weights = True, iter = 0)  # Spin transform!
    kalmsB = alms/(ell * (ell + 1.) / (ell + 2.) / (ell - 1)) ** 0.5

#Set monopole terms to 0
kalmsE[ell == 0] = 0.0
kalmsB[ell == 0] = 0.0

#First entry of kalmsE is a dummy entry. Just need 2nd two entries of E and B modes
_, gamma1, gamma2 = hp.alm2map([kalmsE,kalmsE,kalmsB],
                               nside = 1024,
                               lmax  = 2048,
                               pol=True)

#gamma1 and gamma2 are the shear fields corresponding to kappaE
