"""Define the seven SI base units.

Source : http://physics.nist.gov/cuu/Units/units.html)
"""
from unum.core import new_unit

__all__ = [
    'A', 'AA', 'ACD', 'AG', 'AK', 'AM', 'AMOL', 'CA', 'CCD', 'CD', 'CG', 'CK',
    'CM', 'CMOL', 'DA', 'DAA', 'DACD', 'DAG', 'DAK', 'DAM', 'DAMOL', 'DCD',
    'DG', 'DK', 'DM', 'DMOL', 'EA', 'ECD', 'EG', 'EK', 'EM', 'EMOL', 'Ecd',
    'Eg', 'Em', 'Emol', 'Es', 'FA', 'FCD', 'FG', 'FK', 'FM', 'FMOL', 'GA',
    'GCD', 'GG', 'GK', 'GM', 'GMOL', 'Gcd', 'Gg', 'Gm', 'Gmol', 'Gs', 'HA',
    'HCD', 'HG', 'HK', 'HM', 'HMOL', 'K', 'KA', 'KCD', 'KG', 'KK', 'KM',
    'KMOL', 'M', 'MA', 'MCD', 'MG', 'MK', 'MM', 'MMOL', 'MOL', 'Mcd', 'Mg',
    'Mm', 'Mmol', 'Ms', 'NA', 'NG', 'NK', 'NM', 'NMOL', 'PA', 'PCD', 'PG',
    'PK', 'PM', 'PMOL', 'Pcd', 'Pg', 'Pm', 'Pmol', 'Ps', 'TA', 'TCD', 'TG',
    'TK', 'TM', 'TMOL', 'Tcd', 'Tg', 'Tm', 'Tmol', 'Ts', 'UA', 'UCD', 'UG',
    'UK', 'UM', 'UMOL', 'YA', 'YCD', 'YG', 'YK', 'YM', 'YMOL', 'Ycd', 'Yg',
    'Ym', 'Ymol', 'Ys', 'ZA', 'ZCD', 'ZG', 'ZK', 'ZM', 'ZMOL', 'Zcd', 'Zg',
    'Zm', 'Zmol', 'Zs', 'aA', 'aK', 'acd', 'ag', 'am', 'amol', 'cA', 'cK',
    'ccd', 'cd', 'cg', 'cm', 'cmol', 'cs', 'dA', 'dK', 'daA', 'daK', 'dacd',
    'dag', 'dam', 'damol', 'das', 'dcd', 'dg', 'dm', 'dmol', 'ds', 'fA', 'fK',
    'fcd', 'fg', 'fm', 'fmol', 'fs', 'g', 'hA', 'hK', 'hcd', 'hg', 'hm',
    'hmol', 'hs', 'kA', 'kK', 'kcd', 'kg', 'km', 'kmol', 'ks', 'm', 'mA',
    'mK', 'mcd', 'mg', 'mm', 'mmol', 'mol', 'ms', 'nA', 'nK', 'ncd', 'ng',
    'nm', 'nmol', 'ns', 'pA', 'pK', 'pcd', 'pg', 'pm', 'pmol', 'ps', 's',
    'uA', 'uK', 'ucd', 'ug', 'um', 'umol', 'us', 'yA', 'yK', 'ycd', 'yg',
    'ym', 'ymol', 'ys', 'zA', 'zK', 'zcd', 'zg', 'zm', 'zmol', 'zs',
]

m = M = new_unit("m", 0, "meter")
Ym = YM = new_unit("Ym", 10 ** 24 * m, "yottameter")
Zm = ZM = new_unit("Zm", 10 ** 21 * m, "zettameter")
Em = EM = new_unit("Em", 10 ** 18 * m, "exameter")
Pm = PM = new_unit("Pm", 10 ** 15 * m, "petameter")
Tm = TM = new_unit("Tm", 10 ** 12 * m, "terameter")
Gm = GM = new_unit("Gm", 10 ** 9 * m, "gigameter")
Mm = MM = new_unit("Mm", 10 ** 6 * m, "megameter")
km = KM = new_unit("km", 10 ** 3 * m, "kilometer")
hm = HM = new_unit("hm", 10 ** 2 * m, "hectometer")
dam = DAM = new_unit("dam", 10 ** 1 * m, "decameter")
ym = new_unit("ym", 10 ** -24 * m, "yoctometer")
zm = new_unit("zm", 10 ** -21 * m, "zeptometer")
am = AM = new_unit("am", 10 ** -18 * m, "attometer")
fm = FM = new_unit("fm", 10 ** -15 * m, "femtometer")
pm = new_unit("pm", 10 ** -12 * m, "picometer")
nm = NM = new_unit("nm", 10 ** -9 * m, "nanometer")
um = UM = new_unit("um", 10 ** -6 * m, "micrometer")
mm = new_unit("mm", 10 ** -3 * m, "millimeter")
cm = CM = new_unit("cm", 10 ** -2 * m, "centimeter")
dm = DM = new_unit("dm", 10 ** -1 * m, "decimeter")

# Uppercase S is Siements; seconds can only use lowercase s
s = new_unit("s", 0, "second")
Ys = new_unit("Ys", 10 ** 24 * s, "yottasecond")
Zs = new_unit("Zs", 10 ** 21 * s, "zettasecond")
Es = new_unit("Es", 10 ** 18 * s, "exasecond")
Ps = new_unit("Ps", 10 ** 15 * s, "petasecond")
Ts = new_unit("Ts", 10 ** 12 * s, "terasecond")
Gs = new_unit("Gs", 10 ** 9 * s, "gigasecond")
Ms = new_unit("Ms", 10 ** 6 * s, "megasecond")
ks = new_unit("ks", 10 ** 3 * s, "kilosecond")
hs = new_unit("hs", 10 ** 2 * s, "hectosecond")
das = new_unit("das", 10 ** 1 * s, "decasecond")
ys = new_unit("ys", 10 ** -24 * s, "yoctosecond")
zs = new_unit("zs", 10 ** -21 * s, "zeptosecond")
# as = new_unit("as", 10**-18 * s, "attosecond") # as is a reserved word
fs = new_unit("fs", 10 ** -15 * s, "femtosecond")
ps = new_unit("ps", 10 ** -12 * s, "picosecond")
ns = new_unit("ns", 10 ** -9 * s, "nanosecond")
us = new_unit("us", 10 ** -6 * s, "microsecond")
ms = new_unit("ms", 10 ** -3 * s, "millisecond")
cs = new_unit("cs", 10 ** -2 * s, "centisecond")
ds = new_unit("ds", 10 ** -1 * s, "decisecond")


A = new_unit("A", 0, "ampere")
YA = new_unit("YA", 10 ** 24 * A, "yottaampere")
ZA = new_unit("ZA", 10 ** 21 * A, "zettaampere")
EA = new_unit("EA", 10 ** 18 * A, "exaampere")
PA = new_unit("PA", 10 ** 15 * A, "petaampere")
TA = new_unit("TA", 10 ** 12 * A, "teraampere")
GA = new_unit("GA", 10 ** 9 * A, "gigaampere")
MA = new_unit("MA", 10 ** 6 * A, "megaampere")
kA = KA = new_unit("kA", 10 ** 3 * A, "kiloampere")
hA = HA = new_unit("hA", 10 ** 2 * A, "hectoampere")
daA = DAA = new_unit("daA", 10 ** 1 * A, "decaampere")
yA = new_unit("yA", 10 ** -24 * A, "yoctoampere")
zA = new_unit("zA", 10 ** -21 * A, "zeptoampere")
aA = AA = new_unit("aA", 10 ** -18 * A, "attoampere")
fA = FA = new_unit("fA", 10 ** -15 * A, "femtoampere")
pA = new_unit("pA", 10 ** -12 * A, "picoampere")
nA = NA = new_unit("nA", 10 ** -9 * A, "nanoampere")
uA = UA = new_unit("uA", 10 ** -6 * A, "microampere")
mA = new_unit("mA", 10 ** -3 * A, "milliampere")
cA = CA = new_unit("cA", 10 ** -2 * A, "centiampere")
dA = DA = new_unit("dA", 10 ** -1 * A, "deciampere")


K = new_unit("K", 0, "kelvin")
YK = new_unit("YK", 10 ** 24 * K, "yottakelvin")
ZK = new_unit("ZK", 10 ** 21 * K, "zettakelvin")
EK = new_unit("EK", 10 ** 18 * K, "exakelvin")
PK = new_unit("PK", 10 ** 15 * K, "petakelvin")
TK = new_unit("TK", 10 ** 12 * K, "terakelvin")
GK = new_unit("GK", 10 ** 9 * K, "gigakelvin")
MK = new_unit("MK", 10 ** 6 * K, "megakelvin")
kK = KK = new_unit("kK", 10 ** 3 * K, "kilokelvin")
hK = HK = new_unit("hK", 10 ** 2 * K, "hectokelvin")
daK = DAK = new_unit("daK", 10 ** 1 * K, "decakelvin")
yK = new_unit("yK", 10 ** -24 * K, "yoctokelvin")
zK = new_unit("zK", 10 ** -21 * K, "zeptokelvin")
aK = AK = new_unit("aK", 10 ** -18 * K, "attokelvin")
fK = FK = new_unit("fK", 10 ** -15 * K, "femtokelvin")
pK = new_unit("pK", 10 ** -12 * K, "picokelvin")
nK = NK = new_unit("nK", 10 ** -9 * K, "nanokelvin")
uK = UK = new_unit("uK", 10 ** -6 * K, "microkelvin")
mK = new_unit("mK", 10 ** -3 * K, "millikelvin")
cK = CK = new_unit("cK", 10 ** -2 * K, "centikelvin")
dK = DK = new_unit("dK", 10 ** -1 * K, "decikelvin")


mol = MOL = new_unit("mol", 0, "mole")
Ymol = YMOL = new_unit("Ymol", 10 ** 24 * mol, "yottamole")
Zmol = ZMOL = new_unit("Zmol", 10 ** 21 * mol, "zettamole")
Emol = EMOL = new_unit("Emol", 10 ** 18 * mol, "examole")
Pmol = PMOL = new_unit("Pmol", 10 ** 15 * mol, "petamole")
Tmol = TMOL = new_unit("Tmol", 10 ** 12 * mol, "teramole")
Gmol = GMOL = new_unit("Gmol", 10 ** 9 * mol, "gigamole")
Mmol = MMOL = new_unit("Mmol", 10 ** 6 * mol, "megamole")
kmol = KMOL = new_unit("kmol", 10 ** 3 * mol, "kilomole")
hmol = HMOL = new_unit("hmol", 10 ** 2 * mol, "hectomole")
damol = DAMOL = new_unit("damol", 10 ** 1 * mol, "decamole")
ymol = new_unit("ymol", 10 ** -24 * mol, "yoctomole")
zmol = new_unit("zmol", 10 ** -21 * mol, "zeptomole")
amol = AMOL = new_unit("amol", 10 ** -18 * mol, "attomole")
fmol = FMOL = new_unit("fmol", 10 ** -15 * mol, "femtomole")
pmol = new_unit("pmol", 10 ** -12 * mol, "picomole")
nmol = NMOL = new_unit("nmol", 10 ** -9 * mol, "nanomole")
umol = UMOL = new_unit("umol", 10 ** -6 * mol, "micromole")
mmol = new_unit("mmol", 10 ** -3 * mol, "millimole")
cmol = CMOL = new_unit("cmol", 10 ** -2 * mol, "centimole")
dmol = DMOL = new_unit("dmol", 10 ** -1 * mol, "decimole")


cd = CD = new_unit("cd", 0, "candela")
Ycd = YCD = new_unit("Ycd", 10 ** 24 * cd, "yottacandela")
Zcd = ZCD = new_unit("Zcd", 10 ** 21 * cd, "zettacandela")
Ecd = ECD = new_unit("Ecd", 10 ** 18 * cd, "exacandela")
Pcd = PCD = new_unit("Pcd", 10 ** 15 * cd, "petacandela")
Tcd = TCD = new_unit("Tcd", 10 ** 12 * cd, "teracandela")
Gcd = GCD = new_unit("Gcd", 10 ** 9 * cd, "gigacandela")
Mcd = MCD = new_unit("Mcd", 10 ** 6 * cd, "megacandela")
kcd = KCD = new_unit("kcd", 10 ** 3 * cd, "kilocandela")
hcd = HCD = new_unit("hcd", 10 ** 2 * cd, "hectocandela")
dacd = DACD = new_unit("dacd", 10 ** 1 * cd, "decacandela")
ycd = new_unit("ycd", 10 ** -24 * cd, "yoctocandela")
zcd = new_unit("zcd", 10 ** -21 * cd, "zeptocandela")
acd = ACD = new_unit("acd", 10 ** -18 * cd, "attocandela")
fcd = FCD = new_unit("fcd", 10 ** -15 * cd, "femtocandela")
pcd = new_unit("pcd", 10 ** -12 * cd, "picocandela")
ncd = NCD = new_unit("ncd", 10 ** -9 * cd, "nanocandela")
ucd = UCD = new_unit("ucd", 10 ** -6 * cd, "microcandela")
mcd = new_unit("mcd", 10 ** -3 * cd, "millicandela")
ccd = CCD = new_unit("ccd", 10 ** -2 * cd, "centicandela")
dcd = DCD = new_unit("dcd", 10 ** -1 * cd, "decicandela")


kg = KG = new_unit("kg", 0, "kilogram")
Yg = YG = new_unit("Yg", 10 ** 21 * kg, "yottagram")
Zg = ZG = new_unit("Zg", 10 ** 18 * kg, "zettagram")
Eg = EG = new_unit("Eg", 10 ** 15 * kg, "exagram")
Pg = PG = new_unit("Pg", 10 ** 12 * kg, "petagram")
Tg = TG = new_unit("Tg", 10 ** 9 * kg, "teragram")
Gg = GG = new_unit("Gg", 10 ** 6 * kg, "gigagram")
Mg = MG = new_unit("Mg", 10 ** 3 * kg, "megagram")
hg = HG = new_unit("hg", 10 ** -1 * kg, "hectogram")
dag = DAG = new_unit("dag", 10 ** -2 * kg, "decagram")
yg = new_unit("yg", 10 ** -27 * kg, "yoctogram")
zg = new_unit("zg", 10 ** -24 * kg, "zeptogram")
ag = AG = new_unit("ag", 10 ** -21 * kg, "attogram")
fg = FG = new_unit("fg", 10 ** -18 * kg, "femtogram")
pg = new_unit("pg", 10 ** -15 * kg, "picogram")
ng = NG = new_unit("ng", 10 ** -12 * kg, "nanogram")
ug = UG = new_unit("ug", 10 ** -9 * kg, "microgram")
mg = new_unit("mg", 10 ** -6 * kg, "milligram")
cg = CG = new_unit("cg", 10 ** -5 * kg, "centigram")
dg = DG = new_unit("dg", 10 ** -4 * kg, "decigram")
g = new_unit("g", 10 ** -3 * kg, "gram")
