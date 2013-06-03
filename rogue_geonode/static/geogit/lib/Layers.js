/*
 * Requires ../GeoGit.js and OpenLayers
 */

GeoGit.Layers = (function(){
	var map, onAddLayer;
	var layers = null;
	
	/*
	 * private function
	 * 
	 * Get the url and the feature type from the layer object passed by the add and remove layer evt
	 */
	var getUrlAndFeatureType = function(evt){
		var eofUrl = evt.layer.url.indexOf("geoserver") + 9;
		var url = evt.layer.url.substring(0, eofUrl);
		console.log("url: " + url);
		
		var featureType = new String(evt.layer.params["LAYERS"]);
		console.log("featureType: " + featureType);
		
		return {
			url: url,
			featureType: featureType
		}
	};
	
	/*
	 * private function
	 * 
	 * Add the layer to the layers hash obj
	 */
	var addLayer = function(info){
		/*
		 * If layers is null, initialize it
		 */
		if(!layers){
			layers = {};
		}
		
		/*
		 * If layers[url] is undefined or null then initialize layers[url]
		 */
		if(!layers[info.url]){
			layers[info.url] = {};
		}
			
		/*
		 * Mark the layer is added
		 */
		layers[info.url][info.featureType] = true;
	};
	
	var removeLayer = function(info){
		if(layers && layers[info.url] && layers[info.url][info.featureType]){
			delete layers[info.url][info.featureType];
		}
	};
	
	return {
		/*
		 * Initialize GeoGit.Layers
		 * @param options: {
		 * 		map - OpenLayers.Map,
		 * 		onAddLayer - function to be executed when a layer is added to the map,
		 * 		
		 * }
		 */
		init: function(options){
			this.setMap(options.map);
			
			
			map.events.register('addlayer', null, this.onAddLayer);
			map.events.register('removelayer', null, this.onRemoveLayer);
		},
		
		/*
		 * Add a layer to the layers hash
		 */
		onAddLayer: function(evt){
			if(evt && evt.layer && evt.layer.url && evt.layer.params && evt.layer.params["LAYERS"]){
				var info = getUrlAndFeatureType(evt);
				
				addLayer(info);
			}
		},
		
		/*
		 * Remove a layer from the layers hash
		 */
		onRemoveLayer: function(evt){
			if(evt && evt.layer && evt.layer.url && evt.layer.params && evt.layer.params["LAYERS"]){
				var info = getUrlAndFeatureType(evt);
				
				removeLayer(info);
			}
		},
		
		setMap: function(_map){
			map = _map;
		},
		
		getLayers: function(){
			return layers;
		}
	};
}());