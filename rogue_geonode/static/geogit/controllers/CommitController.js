/*
 * Controller for the list of features in a commit
 * 
 * Used for displaying the details of the affected features
 */
GeoGit.geogitApp.controller("CommitController", function($scope, $http){
	
	$scope.toggleDivs = function(){
		$('.geogit-commit-wrapper').toggle();
		$('.geogit-history-wrapper').toggle();
	};
	
	$scope.parsePath = function(path){
		var slashIndex = path.indexOf('/');
		
		var featureType = path.substring(0, slashIndex);
		
		var featureId = path.substr(slashIndex + 1);
		
		return {
			"featureType": featureType,
			"featureId": featureId
		};
	};
	
	$scope.getFeatureId = function(diff){
		var featureInfo = null;
		if(diff.changeType === "REMOVED"){
			featureInfo = $scope.parsePath(diff.path);
		}else{
			featureInfo = $scope.parsePath(diff.newPath);
		}
		
		return featureInfo.featureId;
	};
	
	$scope.getFeatureType = function(diff){
		var featureInfo = null;
		if(diff.changeType === "REMOVED"){
			featureInfo = $scope.parsePath(diff.path);
		}else{
			featureInfo = $scope.parsePath(diff.newPath);
		}
		
		return featureInfo.featureType;
	};
});