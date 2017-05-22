# Run as:
#    python setup.py build_ext --inplace

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext


from numpy.distutils.misc_util import get_numpy_include_dirs
compute_coef = [Extension("ComputeCoef", ["ComputeCoef.pyx", "ComputeCoef.pxd"],                           
                      include_dirs=get_numpy_include_dirs())]

setup(
  name = 'Compute Coefficients',
  cmdclass = {'build_ext': build_ext},
  ext_modules = compute_coef,
)
