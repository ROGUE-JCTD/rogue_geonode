try:
    from .celery import app as celery_app # flake8: noqa
except ImportError:
    pass

__version__ = (0, 1, 1, 'alpha', 0)

def get_version():
    import geoshape.version
    return geoshape.version.get_version(__version__)
