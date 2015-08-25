try:
    from celery_app import app as celery_app # flake8: noqa
except ImportError:
    pass

__version__ = (1, 5, 0, 'final', 0)

def get_version():
    import geoshape.version
    return geoshape.version.get_version(__version__)
