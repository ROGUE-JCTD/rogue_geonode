/*
 * requires ../GeoGit.js
 */

GeoGit.History = (function(){
	var historyScope,
	historyElement;

	return {
		init: function(options){
			 this.setHistoryElement(options.element);
			 this.getNativeName();
		}, 
		setHistoryElement: function(_historyElement){
			historyElement = document.getElementById(_historyElement);
		},
		getScope: function(){
			if(historyScope){
				return historyScope;
			}
			
			if(historyElement){
				historyScope = angular.element(historyElement).scope();
				return historyScope;
			}
			
			throw "GeoGit.History requires an existing element id";
		},
		getNativeName: function(){
                	if(GeoGit.url && GeoGit.workspace && GeoGit.store && GeoGit.layername){
                        	var request = GeoGit.url + "rest/workspaces/" + GeoGit.workspace +
                                	"/datastores/" + GeoGit.store + "/featuretypes/" + GeoGit.layername + ".json";
				
	        		OpenLayers.Request.GET({
        	        		url: request,
                	        	success: function(results){
                        			var jsonFormatter = new OpenLayers.Format.JSON();
                                		var featureTypeInfo = jsonFormatter.read(results.responseText);
                                       		GeoGit.nativename = featureTypeInfo.featureType.nativeName;
                                    		GeoGit.History.fetchHistory();
                                	},
                                	failure: function(err){
                               			throw "GeoGit - HistoryController error";
                               		}
                        	});
        		}
		},
		fetchHistory: function(){
			var scope = this.getScope();
			
			scope.$apply(function(){
				scope.fetchHistory();
			});
		}
	};
}());
