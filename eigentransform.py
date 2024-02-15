
from multiprocessing import shared_memory
import numpy as np
import cython_eigenx
import logging
import os

def runcol(row, ij = 4):
    i , bfrname, width, height = row
    existing_shm = shared_memory.SharedMemory(name=bfrname)
    simg = np.ndarray((height, width), dtype=np.uint8, buffer=existing_shm.buf)
    existn_eigshm = shared_memory.SharedMemory(name=f'{bfrname}-2')
    eimgbuff = np.ndarray((height, width), dtype=np.uint8, buffer=existn_eigshm.buf)
    eigen_cols = cython_eigenx.runeigen(simg, i, height, width, rc = ij)
    eimgbuff[i] = eigen_cols
    existing_shm.close()
    existn_eigshm.close()


