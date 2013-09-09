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
    url='https://github.com/ROGUE-JCTD/rogue_geonode',
    packages=['rogue_geonode',],
    include_package_data=True,
    install_requires=[
        #"geonode==2.0b10"

        # Override the PyPI gsconfig with the rogue_geonode fork until 0.6.4 is released.
        "gsconfig>=0.6.4a1"
    ],
    dependency_links=['https://github.com/ROGUE-JCTD/gsconfig.py/tarball/master#egg=gsconfig-0.6.4a1'],
    zip_safe=False,
)
