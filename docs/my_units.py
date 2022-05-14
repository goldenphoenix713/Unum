# Example of a custom units file. To use, just place in your path
# and type::
#    from my_units import *

from unum.units import *
from unum import new_unit

SPAM = new_unit('spam')
KSPAM = new_unit('kilospam', 1000 * SPAM)
MSPAM = new_unit('millispam', 0.001 * SPAM)
SPS = new_unit('sps', SPAM / S)
