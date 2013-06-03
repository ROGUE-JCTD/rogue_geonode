/*
 * requires ../GeoGit.js
 */

GeoGit.History = (function(){
	var historyScope,
	historyElement;
	
	return {
		init: function(options){
			 this.setHistoryElement(options.element);
			 this.fetchHistory();
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
		
		fetchHistory: function(){
			var scope = this.getScope();
			
			scope.$apply(function(){
				scope.fetchHistory();
			});
		}
	};
}());