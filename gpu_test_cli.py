#!/usr/bin/env python3


"""
Simple tests to prove that Python / TensorFlow have access to one or more GPUs
"""


__status__ = "Development"
__date__ = "2020-05-15"
__version__ = "0.1"
__author__ = "Nick Jensen"
__email__ = "nijen@microsoft.com"
__copyright__ = "Copyright 2020 Nick Jensen"
__credits__ = (
    "Nick Jensen",
)
__maintainer__ = __credits__[-1]


from gpu_test import gpu_md_table


print(gpu_md_table())


