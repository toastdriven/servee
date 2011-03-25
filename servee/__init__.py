VERSION = (0, 6, 0, "a", 1)  # following PEP 386
DEV_N = "5"

# cribbed from pinax
# https://github.com/pinax/pinax/raw/master/LICENSE
def get_version():
    version = "%s.%s" % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = "%s.%s" % (version, VERSION[2])
    if VERSION[3] != "f":
        version = "%s%s%s" % (version, VERSION[3], VERSION[4])
        if DEV_N:
            version = "%s.dev%s" % (version, DEV_N)
    return version


__version__ = get_version()