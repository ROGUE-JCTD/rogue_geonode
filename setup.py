import os
from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

# Tell distutils not to put the data_files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
walk_dir = 'geoshape'

excluded_folders = ['uploaded']

for dirpath, dirnames, filenames in os.walk(walk_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.') or dirname in excluded_folders: del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

install_requires = [
        "geoshape-geonode==1.0",
        "django-classification-banner>=0.1.4",
        "django-maploom==1.0",
        "psycopg2==2.4.5"
]

tests_requires = [
    "lxml==3.3.1",
]

docs_requires = [
    "sphinx-rtd-theme==0.1.5",
    "Sphinx==1.2.2",
]

setup(
    name="geoshape",
    version="1.0",
    author="LMN Solutions",
    author_email="rogue@lmnsolutions.com",
    description="geoshape, based on GeoNode",
    long_description=(read('README.rst')),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
    ],
    license="BSD",
    keywords="geoshape geonode django",
    url='https://github.com/ROGUE-JCTD/rogue_geonode',
    packages=packages,
    data_files=data_files,
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'tests': install_requires + tests_requires,
        'docs':  docs_requires
    },
    zip_safe=False,
)
