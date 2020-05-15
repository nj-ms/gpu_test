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


from datetime import datetime


def now(fmt="%a %Y-%m-%d %H:%M:%S Z"):
    return datetime.utcnow().strftime(fmt)


