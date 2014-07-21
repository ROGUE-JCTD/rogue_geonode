__version__ = (0, 1, 0, 'alpha', 0)


def get_version():
    import rogue_geonode.version
    return rogue_geonode.version.get_version(__version__)