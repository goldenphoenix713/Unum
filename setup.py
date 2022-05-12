from setuptools import setup


__version_info__ = (5, 0, 2)
__version__ = '.'.join([str(v) for v in __version_info__])

setup(
    name="Unum",
    version=__version__,
    description="Units in Python",
    author="Chris MacLeod, Pierre Denis, Leszek Trzemecki",
    author_email="leszek.trzemecki@gmail.com",
    url="https://github.com/trzemecki/Unum",
    license="LGPL",
    install_requires=[
        'six',
        'inflect',
    ],
    test_suite="tests",
    packages=[
        'unum',
        'unum.units',
        'unum.units.custom',
        'unum.units.others',
        'unum.units.si',
        'unum.units.imp_UK',
        'unum.units.US_Customary',
        'tests',
    ]
)
