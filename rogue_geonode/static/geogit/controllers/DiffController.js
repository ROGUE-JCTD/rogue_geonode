/*
 * Controller for getting the features affected in a commit
 * 
 * fetchDiffs gets called when a commit gets clicked on
 */
GeoGit.geogitApp.controller("DiffController", function($scope, $http){
	/*
	 * oldRefSpec: id of old commit
	 * newRefSpec: id of new commit
	 * afterFetch: function to be called after the diff is fetched
	 */
	$scope.fetchDiff = function(oldRefSpec, newRefSpec, afterFetch){
		if(GeoGit.url && GeoGit.workspace && GeoGit.store){
			var request = GeoGit.url + "/" + GeoGit.workspace + ":" + GeoGit.store + "/diff?";
			
			$http.jsonp(request + "output_format=json&newRefSpec=" + newRefSpec + "&oldRefSpec=" + oldRefSpec + "&callback=JSON_CALLBACK").success(function(data, status){
				console.log(data);
				var diff = data.response.diff;
				
				if(Object.prototype.toString.call(diff) !== '[object Array]'){
					$scope.diffs = [diff];
				}else{
					$scope.diffs = diff;
				}
				
				if(afterFetch){
					afterFetch();
				}
			}).error(function(error, status){
				throw error;
			});
		}
	};
});