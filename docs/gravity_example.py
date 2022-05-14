from __future__ import print_function

from unum.units import *
from unum import new_unit

# Constants
G = 6.6720E-11 * N * m ** 2 / kg ** 2
earth_mass = 5.980E24 * kg
c = 299792458 * m / s
earth_radius = 6.37E+06 * m

ly = new_unit('ly', c * 365 * d, 'light year')

# Input data
distances = (5 * cm, earth_radius, ly)
masses = (5 * g, earth_mass, 1000 * earth_mass)

# -- Processing and display

print("G            = %s" % G)

print("Earth mass   = %s" % earth_mass)

print("Earth radius = %s" % earth_radius.cast_unit(KM))

print("distances    = %s" % str(distances))

print("masses       = %s" % str(masses))

print()

for m1 in masses:
    for m2 in masses:
        if m1 >= m2:
            for d in distances:
                force = G * m1 * m2 / d ** 2

                a1 = force / m1
                a2 = force / m2

                print("m1 = %s, m2 = %s, d = %s" % (m1, m2, d))

                print("f = %s, a1 = %s, a2 = %s\n" % (
                    force, a1.cast_unit(m / s ** 2), a2.cast_unit(m / s ** 2)
                ))
