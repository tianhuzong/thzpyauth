from setuptools import setup,find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy
extensions = [
    Extension("utils.string", ["./utils/string/verify.pyx","./utils/string/verify_c.cpp"], language='c++'),
    Extension("utils.captcha",["./utils/captcha/generator.pyx"],language="c++"),
    Extension("utils.libhash",["./utils/libhash/hash.pyx"],language="c++"),
    Extension("utils.encrypt",["./utils/encrypt/encrypt.pyx"],language="c++"),
    Extension("utils.emailer",["./utils/emailer/emailer.pyx"],language="c++"),
    
]
setup(name="utils",ext_modules=cythonize(extensions),packages=find_packages(),package_data={'': ['__init__.py']},include_dirs = [numpy.get_include()],include_package_data=True)
