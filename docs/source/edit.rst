.. editing.edit:

Edit Features
=================
Vector layers can be set up so that they're editable.  If you have permissions to edit a layer, the editing tools will be available in the map.
If a layer is a GeoGit layer, then you can work with the edit history as well.

Add a simple point feature to a layer
--------------------------------------
If a layer is editable, then the :guilabel:`Add Feature` button will be available next to the layer name.

   .. figure:: img/en_addfeaturebutton.png

      *Add feature button*  

#. Click the :guilabel:`Add Feature` button.  The :guilabel:`Drawing Geometry` dialog will appear at the top of the map.

   .. figure:: img/en_drawinggeometrypoint.png

#. Click on the map to add the geometry.  A simple point is placed with one click.  The sections below provide additional detail on editing different types of features.

   .. figure:: img/en_newpoint.png

#. Click on the :guilabel:`Accept Feature` button to keep the geometry.  If you don't want to keep the feature, click the X for the :guilabel:`Cancel Feature` button.

   .. figure:: img/en_acceptfeature.png

#. Once you click on :guilabel:`Accept Feature` the :guilabel:`Edit Attributes` window will open.  Type in the fields or select values from the dropdowns to add attribute values.

   .. figure:: img/en_editattributes.png

#. Click the :guilabel:`Save` button at the bottom of the form to save the feature to the layer.


Add a multipoint feature to a layer
-------------------------------------
Multipoint features can have more than one point per feature.  

#. Click the :guilabel:`Add Feature` button.  The :guilabel:`Drawing Geometry` dialog will appear at the top of the screen.

   .. figure:: img/en_addnewmultipoint.png

#. Click on the map to add the first point.  Click on the :guilabel:`Add Geometry` button to add another point.  Continue to add points for the feature as needed.

   .. figure:: img/en_addtofeaturemultipoint.png 

#. Click on the :guilabel:`Accept Feature` button to keep the geometries.

   .. figure:: img/en_acceptfeaturemulti.png 

#. Once you click on :guilabel:`Accept Feature` the :guilabel:`Edit Attributes` window will open.  Type in the fields or select values from the dropdowns to add attribute values.
   .. figure:: img/en_editattribmulti.png

#. Click the :guilabel:`Save` button at the bottom of the form to save the feature to the layer.


Add a polygon feature to a layer
---------------------------------
A simple polygon layer has a single polygon per feature.

#. Click on the :guilabel:`Add Feature` button.  The :guilabel:`Drawing Geometry` dialog will appear at the top of the screen.

   .. figure:: img/en_addfeaturebutton.png

#. Click on the map to begin adding the polygon.  Continue to click to add all of the vertices.  To finalize the polygon, close the geometry by clicking on the first vertice again.

   .. figure:: img/en_newpolygon.png 

#. If you want the polygon to have right angle corners, you can click on the right angle button.

   .. figure::  img/en_rightanglesmultipolygon.png

#. Click on the :guilabel:`Accept Feature` button to keep the geometry.  If you don't want to keep the feature, click the X for the :guilabel:`Cancel Feature` button.

   .. figure:: img/en_acceptfeature.png

#. Once you click on :guilabel:`Accept Feature` the :guilabel:`Edit Attributes` window will open.  Type in the fields or select values from the dropdowns to add attribute values.

   .. figure:: img/en_editattribpolygon.png

#. Click the :guilabel:`Save` button at the bottom of the form to save the feature to the layer.

Add a multipoylgon feature to a layer
--------------------------------------
A multipolygon layer has one or more polygons per feature.  A couple of examples of multipoygons are the U.S. States of Michigan and Hawaii.

#. Click on the :guilabel:`Add Feature` button.  The :guilabel:`Drawing Geometry` dialog will appear at the top of the screen.

   .. figure:: img/en_addnewmultipolygon.png 

#. Click on the map to begin adding the polygon.  Continue to click to add all of the vertices.  To finalize the polygon, close the geometry by clicking on the first vertice again.  To add another polygon, click on the :guilabel:`Add Geometry` button.  Repeat the process to add polygons as needed.

   .. figure:: img/en_addtofeaturemultipolygon.png 

#. If you want the polygon to have square corners, you can click on the right angle button.  

   .. figure:: img/en_rightanglesmultipolygon.png 

#. Click on the :guilabel:`Accept Feature` button to keep the geometries.  

   .. figure:: img/en_acceptfeaturemultipolygon.png 

#. Once you click on :guilabel:`Accept Feature` the :guilabel:`Edit Attributes` window will open.  Type in the fields or select values from the dropdowns to add attribute values.
   .. figure:: img/en_editattribmulti.png

#. Click the :guilabel:`Save` button at the bottom of the form to save the feature to the layer.


Add a line to a layer
----------------------
A line layer consists of lines that represent features - such as roads, powerlines, and other features.  

#. Click on the :guilabel:`Add Feature` button.  The :guilabel:`Drawing Geometry` dialog will appear at the top of the screen.

   .. figure:: img/en_addfeaturebutton.png

#. Click on the map to begin adding the linear feature.  Continue to click to add all of the vertices.  To finalize the line, double-click on the last vertice.  

   .. figure:: img/en_newline.png

#. Click on the :guilabel:`Accept Feature` button to keep the geometries.  

   .. figure:: img/en_acceptfeature.png

#. Once you click on :guilabel:`Accept Feature` the :guilabel:`Edit Attributes` window will open.  Type in the fields or select values from the dropdowns to add attribute values.

   .. figure:: img/en_editattribline.png 

#. Click the :guilabel:`Save` button at the bottom of the form to save the feature to the layer.


Add a multiline to a layer
-----------------------------
A multiline layer has one or more polygons per feature.  

#. Click on the :guilabel:`Add Feature` button.  The :guilabel:`Drawing Geometry` dialog will appear at the top of the screen.

   .. figure:: img/en_addnewmultiline.png 

#. Click on the map to begin adding the linear feature.  Continue to click to add all of the vertices.  To finalize the line, double-click on the last vertice.  To add another polygon, click on the :guilabel:`Add Geometry` button.  Repeat the process to add polygons as needed.

   .. figure:: img/en_addtofeaturemultipolyline.png

#. Click on the :guilabel:`Accept Feature` button to keep the geometries.  

   .. figure:: img/en_acceptfeaturemulti.png 

#. Once you click on :guilabel:`Accept Feature` the :guilabel:`Edit Attributes` window will open.  Type in the fields or select values from the dropdowns to add attribute values.

   .. figure:: img/en_editattribmulti.png

#. Click the :guilabel:`Save` button at the bottom of the form to save the feature to the layer.


Edit attributes
-------------------
You can edit the attributes for any features in an editable layer.

#. Click on the feature on the map.  The feature info box will appear.

   .. figure:: img/en_featureinfobox.png

#. Click on the :guilabel:`Edit Attibutes` button.  The :guilabel`Edit Attributes` window will appear.

   .. figure:: img/en_editattribpopup.png

#. Type in the fields or select dropdown values for the fields you want to edit.

   .. figure:: img/en_editattributes.png

#. Click the :guilabel:`Save` button at the bottom of the form to save the attribute updates.


Edit point geometries on the map
------------------------------------
Point layers can be one of two types:  simple points and multipoints.  For simple points, there is one point per feature.  Multipoints can have one or more points per feature.

#. Click on the point feature on the map.  The feature info box will appear.

   .. figure:: img/en_featureinfobox.png

#. Click on the :guilabel:`Edit Geometry` button.  The :guilabel:`Drawing Geometry` dialog will appear at the top of the screen, and the selected feature will be highlighted in blue.

#. Click on the feature and drag it to the new location.

#. Click on the :guilabel:`Accept Feature` button to keep the feature.  To cancel the edit, click on the :guilabel:`Cancel Feature` button.

   .. figure:: img/en_acceptfeature.png


Edit point geometry manually
-----------------------------
With point geometries, you can also manually edit the coordinates.  This is useful when you have the coordinates from another source (such as a report).

#. Click on the point feature on the map.  The feature info box will appear.

   .. figure:: img/en_featureinfobox.png

#. Click on the :guilabel:`Edit Attributes` button.  The :guilabel:`Edit Attributes` window will appear.

   .. figure:: img/en_editattribpopup.png

#. Click on the coordinates field to edit the point coordinates.

   .. figure:: img/en_editcoordinates.png

#. Click the :guilabel:`Save` button at the bottom of the form to save the attribute updates.


Edit polygon and line geometries
------------------------------------
Any existing features in an editable layer can be modified.  If it is a GeoGit layer, the history of all of the edits will be maintain to ensure the provenance of the data.

#. Click on the feature you want to edit.  The feature info box will appear.

   .. figure:: img/en_featureinfobox.png

#. Click on the :guilabel:`Edit Geometry` button.  The :guilabel:`Drawing Geometry` dialog will appear at the top of the screen.

   .. figure:: img/en_editgeompolygon.png

#. Move the mouse over the geometry to highlight the vertice you want to edit.  To move the vertice, click and drag it.  Repeat this process until you have completed editing.

   .. figure:: img/en_movevertice.png

#. Click on the :guilabel:`Accept Feature` button to keep the feature.  To cancel the edit, click on the :guilabel:`Cancel Feature` button.

   .. figure::  img/en_acceptfeature.png



