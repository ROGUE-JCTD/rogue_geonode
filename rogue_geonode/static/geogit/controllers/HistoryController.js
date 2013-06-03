GeoGit.geogitApp.controller("HistoryController", function($scope, $http){
	$scope.fetchHistory = function(){
		if(GeoGit.url && GeoGit.workspace && GeoGit.store){
			var request = GeoGit.url + "/" + GeoGit.workspace + ":" + GeoGit.store + "/log?";
			
			if(GeoGit.layername){
				request += "path=" + GeoGit.layername + "&";
			}
			
			request += "output_format=JSON&callback=JSON_CALLBACK";
			
			$http.jsonp(request).success(function(data, status){
				var commit = data.response.commit;
				
				// If the commit object isn't an array, put it into an array
				if(Object.prototype.toString.call(commit) !== '[object Array]'){
					$scope.history = [commit];
				}else{
					$scope.history = commit;
				}
				
			}).error(function(data, status){
				throw "GeoGit - HistoryController ERROR";
			});
		}
	};
	
	$scope.getDate = function(timestamp){
		return ((new Date(timestamp)).toLocaleDateString());
	};
	
	$scope.getTime = function(timestamp){
		return ((new Date(timestamp)).toLocaleTimeString());
	};
});