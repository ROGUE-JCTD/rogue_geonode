from setuptools import setup, find_packages

install_requires = [
        "geoshape-geonode==1.4",
        "django-classification-banner>=0.1.4",
        "django-maploom==1.4.2",
        "psycopg2==2.4.5",
        "django-tilebundler==0.1-beta1",
        "django-gsschema==0.1-beta2",
        "django-cors-headers>=1.1.0",
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
    version=__import__('geoshape').get_version(),
    author="Prominent Edge",
    author_email="geoshape.org@gmail.com",
    description="geoshape, based on GeoNode and contains additional changes and services",
    #long_description=(read('README.md')),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
    ],
    license="BSD",
    keywords="geoshape geonode django",
    url='https://github.com/ROGUE-JCTD/rogue_geonode',
    packages=find_packages('geoshape'),
    package_dir={'': 'geoshape'},
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'tests': install_requires + tests_requires,
        'docs':  docs_requires
    },
    zip_safe=False,
)
