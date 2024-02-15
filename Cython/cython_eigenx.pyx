cimport cython
import cython
import numpy as np
cimport numpy as np
from cython.parallel import prange, parallel

import cython
@cython.boundscheck(False)
@cython.wraparound(False)
#@cython.nonecheck(False)
cpdef np.ndarray runeigen(np.ndarray img, int i, int height, int width):

    cdef unsigned char [:,:] image = img 
    cdef int j, irc, jrc
    ijrc = 4
    cdef list row1col1, row2col2
    cdef unsigned char[:,:] eigen_patch
    
    cdef double[:,:] U, V
    cdef double[:] eigimg
    eigimg = np.zeros(width)
    cdef double[:] s

    for j in range(0, width):

        row1col1 = [i - i, i + ijrc] if i < ijrc else [i - ijrc, height] if i > (height - ijrc) else [i - ijrc, ijrc + i]
        row2col2 = [j - j, j + ijrc] if j < ijrc else [j - ijrc, width] if j > (width - ijrc) else [j - ijrc, ijrc + j]

        #eigen_patch = image[row1col1[0]:row1col1[1] + 1][:,row2col2[0]:row2col2[1] + 1]
        eigen_patch = image[row1col1[0]:row1col1[1] + 1,row2col2[0]:row2col2[1] + 1]

        U,s,V = np.linalg.svd(eigen_patch)
        
        sval = sorted(s)
        eigimg[j] = np.mean(sval[:len(sval) - 1])
            
    return np.asarray(eigimg)


