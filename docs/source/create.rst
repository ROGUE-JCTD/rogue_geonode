.. _maps.create:

Create a map 
==============

New maps can be created from the Maps tab or from a layer.

**Create a new map**
--------------------
In the Maps tab, click on the "Create a New Map" button.

   .. figure:: img/en_createnewmap.png

      *Create a New Map*


**Create a new map from a layer**
----------------------------------
In the Layers tab, click on the "Create a map" button next to a layer

   .. figure:: img/en_createmapfromlayer.png

      *Create a Map from a Layer*

A new map will open with the layer as part of the map.


**Add layers to a map**
-----------------------
Once you have created a map, or opened an existing map, you can add additional layers.

#. Click on the Add Layers button by "Layers"

   .. figure:: img/en_addlayerpopup.png

      *Add layer*

#. The Add Layers dialog will open.  

   .. figure:: img/en_addlayers.png

#. Click on the checkbox for the layer(s) you want to add to the map.

#. Click the Add button.


**Add layers from another server**
-----------------------------------
You can add layers from other servers besides the GeoNode you're working with.  These servers include web mapping servers (WMS) and tile servers.

#. Click on the Add Layers button by "Layers"

   .. figure:: img/en_addlayerpopup.png

      *Add layer*

#. In the Add Layers dialog, click on the drop down for the server list

   .. figure:: img/en_addnewserver.png

      *Add new server*

#. Click on Add New Server

#. In the Add Server dialog enter the type of server (WMS or TMS), a name for the server, and the URL.

   .. figure:: img/en_addserverdialog.png

      *Server details*

#. Click Add to save the server.  Once you have added the server, you can select it and add layers to the map.


**Change layer order**
-----------------------
Layers are drawn on the map from bottom to top.  The top layer in your layer list will also be on top in the map.  Sometimes you need to reorder layers.  The following steps explain how.

#. Click on the name of the layer you want to move.

#. Drag the layer up or down to change it's position in the drawing order.

   .. figure:: img/en_movelayer.png

      *Change layer order*

#. Release the mouse button to finish moving the layer.


**Toggle layer visibility**
----------------------------
You can turn on and off the visibility for layers in the map.  This allows you to "hide" a layer without having to remove it from the map.

#. Click on the :guilabel:`Toggle Visibility` button to turn a layer off.

   .. figure:: img/en_visibilityon.png

#. Click on the :guilabel:`Toggle Visibility` button again to turn it back on.

   .. figure:: img/en_visibilityoff.png

**Zoom to data**
----------------
The :guilabel:`Zoom to data` button give you a convenient way to center the map on a layer.  Clicking the :guilabel:`Zoom to data` button zooms the map to the extent of the data currently in that layer.

#. Click on the layer name in the layer list in the map.  The menu will expand to display additional tools.

#. Click on the :guilabel:`Zoom to data` button.  The map will zoom to the extent of the data for that layer.  

   .. figure:: img/en_zoomtodata.png

      *Zoom to data button*

Note: if a layer's visibility is dependent on scale, and the data extent is at a smaller scale, you will have to zoom in to be able to view the data.


**Show layer info**
--------------------
You can view information about a layer in the map.  Layer information will include information about the server, basic metadata, and the projection (SRS).  

#. Click on the layer name in the layer list to expand the layer options.

#. Click on the :guilabel:`Show layer info` button.  The Layer Info window will appear.

   .. figure:: img/en_showlayerinfo.png

      *Show layer info button*

   .. figure:: img/en_layerinfo.png

      *Layer info*


**Remove a layer from the map**
--------------------------------
You can remove a layer from the map.

#. Click on the name of the layer you want to remove.  The menu will expand to show all of the options for that layer

#. Click on the :guilabel:`Remove Layer` button.

   .. figure:: img/en_removelayer.png

      *Remove layer button*

#. In the confirmation box, click :guilabel:`Yes` to remove the layer.

   .. figure:: img/en_confirmremovelayer.png

      *Remove layer confirmation*


**Get feature information**
----------------------------
In order to get information for features in a vector layer, simply click on the feature in the map.

#. Click on the feature you want information about.  The feature info window will appear.

   .. figure:: img/en_featureinfo.png


**Change attribute visibility**
--------------------------------
You can control the attributes that appear in the feature info window.  This is useful when a layer has a large number of fields.

#. Click on the the layer name in the layer list in the map.  The layer will expand to show additional options.

   .. figure:: img/en_layerdetails.png

      *Layer attributes*

#. Click on the visibility icon for the attributes to toggle their visibility.

   .. figure:: img/en_attribvisibility.png

      *Layer visibility options*

#. Click on a feature in that layer. You will see that the attribute fields are now hidden.

   .. figure:: img/en_featureinfo2.png

      *Feature info with hidden fields*


**Using the Legend**
----------------------
The legend displays the symbols used for vector layers in the map (not for imagery).  It can be closed to gain screen space and opened when needed.  In addition, you can collapse the legend as desired.

#. Toggle the legend by clicking on the :guilabel:`Toggle Legend` button.

   .. figure:: img/en_togglelegend.png

      *Click the Toggle Legend button to open and close the legend*

#. To collapse or expand a layer in the legend, simply click on the layer name in the Legend window.

   .. figure:: img/en_legendcollapse.png

      *Legend with one layer collapsed*

**Save a map**
-------------------
Saving a map preserves your preferences and makes it available for other GeoNode users.

#. Click on the :guilabel:`Save Map` button in the toolbar.

   .. figure:: img/en_savemaptooltip.png

      *Save map button*

#. Enter a title and abstract for your map.

   .. figure:: img/en_savethismap.png

      *Save map dialog*

#. Click :guilabel:`Save`. Notice that the link on the top right of the page changed to reflect the map's name.

   .. figure:: img/en_savedmap.png

      *Saved map name*

The map is now saved in the list of maps on the Maps page.


**Create a copy of a map**
---------------------------
You can also use a map as a starting point for another map.  This allows you to build on the work of others without changing their maps.

#. Click on the :guilabel:`Save Map` button in the toolbar.

   .. figure:: img/en_savemaptooltip.png

      *Save map button*

#. Enter a title and abstract for your map.

   .. figure:: img/en_savethismap.png

      *Save map dialog*

#. Click :guilabel:`Save Copy`. Notice that the link on the top right of the page changed to reflect the map's name.

   .. figure:: img/en_savemapcopy.png

      *Saved map name*

The map is now saved in the list of maps on the Maps page.

