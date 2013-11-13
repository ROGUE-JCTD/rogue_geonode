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
walk_dir = 'rogue_geonode'

excluded_folders = ['uploaded']

for dirpath, dirnames, filenames in os.walk(walk_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.') or dirname in excluded_folders: del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)))
    elif filenames:
        data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

setup(
    name="rogue_geonode",
    version="0.1.1",
    author="LMN Solutions",
    author_email="rogue@lmnsolutions.com",
    description="rogue_geonode, based on GeoNode",
    long_description=(read('README.rst')),
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="rogue_geonode geonode django",
    url='https://github.com/ROGUE-JCTD/rogue_geonode',
    packages=packages,
    data_files=data_files,
    include_package_data=True,
    install_requires=[
        "geonode==2.0c5",
        "gsconfig==0.6.5a1", # This is a custom version of gsconfig.
        "django-classification-banner>=0.1.2",
    ],
    dependency_links=['https://github.com/ROGUE-JCTD/gsconfig.py/tarball/data_store_type#egg=gsconfig-0.6.5a1',
                      ],
    zip_safe=False,
)
