.. image:: https://secure.travis-ci.org/ROGUE-JCTD/rogue_geonode.png
    :alt: Build Status
    :target: http://travis-ci.org/ROGUE-JCTD/rogue_geonode

GeoSHAPE
========

Geospatial capabilities for Security, Humanitarian Assistance, Partner Engagement – is designed to
enable collaboration on geospatial information between mission partners in connected and disconnected operations.
GeoSHAPE has been built utilizing open source software and open standards to make it available for partners and
to maximize interoperability. GeoSHAPE is the integration of a geospatial portal (GeoNode), a web mapping
client (MapLoom), and a mobile application (Arbiter), that leverages the infrastructure provided by a geospatial
server and database components (The OpenGeo Suite). GeoSHAPE is the outcome of the Rapid Open Geospatial User-Driven
Enterprise (ROGUE) Joint Capability Technology Demonstration (JCTD).  For more information about GeoSHAPE visit the
project page at [http://geoshape.org](https://geoshape.org/).


What is this?
-------------

A django module that extends [GeoNode](https://github.com/GeoNode/geonode) and adds custom functionality that is required by GeoSHAPE.  Follow
the installation instructions below to try it out.

Installation
------------

A GeoSHAPE build consists of several components including GeoNode, Geoserver, GeoGig, and Arbiter that all have to be properly
configured in order to work together correctly. We have a [Google Doc](https://docs.google.com/document/d/1KMpk6dXuqvwfEi0pfRpaGY62j6ikoYtpYUPU0sJQAmk/edit)
that describes the installation process in detail. The easiest way to install and configure these components is by using
[Vagrant](https://www.vagrantup.com) with [Virtualbox](https://www.virtualbox.org/), where you can build an entire GeoSHAPE VM
in only a few commands.::

    git clone https://github.com/ROGUE-JCTD/rogue-chef-repo.git
    cd rogue-chef-repo
    vagrant up

Contributing
------------
We are currently accepting pull requests for this repository. Please provide a human-readable description of the changes
 in the pull request.
