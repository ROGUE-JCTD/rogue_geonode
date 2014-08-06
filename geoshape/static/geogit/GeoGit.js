var GeoGit = (function() {	
	return {
		geogitApp: null,
		url: "",
		workspace: "",
		store: "",
		layername: "",
		
		/*
		 * GeoGit.History
		 */
		History: null,
		ViewDiff: null,
		/*
		 * options: {
		 * 		historyOptions: {
		 * 			element,
		 * 			url,
		 * 			workspace,
		 *			store, 
		 *			layername
		 * 		}
		 * }
		 */
		init: function(options){
			this.url = options.url;
			this.workspace = options.workspace;
			this.store = options.store;
			this.layername = options.layername;
			
			if(this.History){
				this.History.init(options.historyOptions);
			}
			
			if(this.ViewDiff){
				this.ViewDiff.init();
			}	
		}
	};
}());

if(typeof angular !== "undefined"){
	GeoGit.geogitApp = angular.module('geogitApp', []);
}