#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.package import parse_package_for_distutils

d = parse_package_for_distutils()
d['packages'] = ['calibration_estimation', 'urdf_python']
d['package_dir'] = {'': 'src'}
d['install_requires'] = ['genpy', 'numpy', 'rosgraph', 'roslib', 'rospkg']

setup(**d)