# To Build: python setup.py build_ext --inplace

import numpy as np
import sys
import os
import shutil

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# clean previous build
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if (name.startswith("myext") and not(name.endswith(".pyx") or name.endswith(".pxd"))):
            os.remove(os.path.join(root, name))
    for name in dirs:
        if (name == "build"):
            shutil.rmtree(name)

# build "myext.so" python extension to be added to "PYTHONPATH" afterwards...
setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [
        Extension("cython_eigenx",
                  sources=["cython_eigenx.pyx"
                       ],
                  extra_compile_args=["-O3", "-ffast-math"],
                  include_dirs=[np.get_include()], define_macros = [('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')]
             )
        ]
)
