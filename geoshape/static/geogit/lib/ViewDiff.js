/*
 * requires ../GeoGit.js and History.js
 */
GeoGit.ViewDiff = (function(){
	var history;
	
	return {
		/*
		 * options: {
		 * 		history
		 * }
		 */
		init: function(options){
			history = GeoGit.History;
		},
		getLastCommitId: function(commitId){
			var scope = history.getScope();
			
			var commits = scope.history;
			
			for(i = 0; i < commits.length; i++){
				if(commits[i].id === commitId){
					break;
				}
			}
			
			if((i + 1) === commits.length){
				return -1;
			}
			
			return commits[i+1].id;
		},
		fetchDiff: function(commitId){
			var newRefSpec = commitId;
			
			var oldRefSpec = this.getLastCommitId(newRefSpec);
			
			if(oldRefSpec === -1){
				return -1;
			}
			
			var scope = history.getScope();
				
			scope.$apply(function(){
				scope.fetchDiff(oldRefSpec, newRefSpec);
			});
		}
	};
}());