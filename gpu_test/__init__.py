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


import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1" # disable tensorflow info logs

from tensorflow.python.client import device_lib

from gpu_test.jupyter_utils import p
from gpu_test.timestamp import now


def get_tf_gpus():
    """
    List of GPUs from TensorFlow
    :return: list
    """
    r = []
    devices = device_lib.list_local_devices()
    for i in filter(lambda x: x.device_type == "GPU", devices):
        gpu = dict()
        for j in i.physical_device_desc.split(", "):
            k, v = j.split(": ")
            gpu[k] = v
        gpu["memory limit"] = "{:.1f} GiB".format(i.memory_limit / 1024**3)
        r.append(gpu)
    return r


def count_gpus():
    """
    Return the count of GPUs that TensorFlow can "see"
    :return: int
    """
    return len(get_tf_gpus())


def have_gpu():
    """
    Return True if TensorFlow "sees" the GPU
    :return: bool
    """
    return count_gpus() > 0


def gpu_md_table():
    """
    List of GPUs from TensorFlow in a Markdown table
    :return: str
    """
    k2header = {
        "device": "ID",
        "name": "Type",
        "compute capability": "CC",
        "memory limit": "Memory",
        "pci bus id": "PCI",
    }
    r = [
        "# GPU Test\n",
        f"{now()}\n",
        " | ".join(k2header.values()),
        "|".join([":---"] * len(k2header)),
    ]
    for gpu in get_tf_gpus():
        r.append(" | ".join([gpu[k] for k in k2header]))
    r.append("")
    return "\n".join(r)


def gpu_md_table_jupyter(raw=False):
    """
    Print GPU(s) in Markdown Table in Jupyter

    If raw is True, print the Markdown source from `gpu_md_table`.

    :param raw: bool
    """
    p(gpu_md_table(), raw)


