import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="rogue_geonode",
    version="0.1",
    author="",
    author_email="",
    description="rogue_geonode, based on GeoNode",
    long_description=(read('README.rst')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="rogue_geonode geonode django",
    url='https://github.com/rogue_geonode/rogue_geonode',
    packages=['rogue_geonode',],
    include_package_data=True,
    zip_safe=False,
)
