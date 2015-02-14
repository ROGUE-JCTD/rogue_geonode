'use strict';

(function() {
  angular.module('fireStation', [])

  .config(function($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  
  })

  .controller('fireStationController', function($scope, $window, $http) {
	
	 var thisFirestation = '/api/v1/firestations/'+config.id+'/';
	
    $scope.forms = [{'apparatus':'Engine',
					 'chief_officer':0,
					 'ems_emt':0,
					 'ems_paramedic':0,
					 'ems_supervisor':0,
					 'firefighter':0,
					 'firefighter_emt':0,
					 'firefighter_paramedic':0,
					 'firestation':thisFirestation,
					 'officer':0,
					 'officer_paramedic':0,
					 'name':'Add New Response Form'
					 }];
	$scope.resourceCounters = {'Engine':0,
								'Ladder/Truck/Aerial':0,
								'Quint':0,
								'Ambulance/ALS':0,
								'Ambulance/BLS':0,
								'Heavy':0,
								'Rescue':0,
								'Boat':0,
								'Hazmat':0,
								'Chief':0,
								'Other':0};
					 
	var getUrl = '/api/v1/capabilities/?format=json';
	var fireUrl = thisFirestation + '?format=json';
	var postUrl = getUrl;
	$scope.firestation = $http.get(fireUrl);
	$http.get(getUrl).success(function(data){
		for(var iForm = 0; iForm < data.meta.total_count; iForm++) {
			if(data.objects[iForm].firestation == thisFirestation) {
				$scope.resourceCounters[data.objects[iForm].apparatus]++;
				data.objects[iForm].name = data.objects[iForm].apparatus + $scope.resourceCounters[data.objects[iForm].apparatus];
				$scope.forms.push(data.objects[iForm]);
			}
		}
	});
	
	$scope.selectedForm = $scope.forms[0];
	
    var options = {
        boxZoom: false,
        zoom: 15,
        zoomControl: false,
        //dragging: false,
        attributionControl: false,
        scrollWheelZoom: false,
        doubleClickZoom: false,
        fullscreenControl: false
    };
	
	$scope.choices = 		['Engine',
								'Ladder/Truck/Aerial',
								'Quint',
								'Ambulance/ALS',
								'Ambulance/BLS',
								'Heavy',
								'Rescue',
								'Boat',
								'Hazmat',
								'Chief',
								'Other'];
	
	
    $scope.map = L.map('map', options).setView(config.centroid, 13);
	
	$scope.ClearForm = function(form) {
			form.apparatus = 'Engine';
			form.firefighter = 0;
			form.firefighter_emt = 0;
			form.firefighter_paramedic = 0;
			form.ems_emt = 0;
			form.ems_paramedic = 0;
			form.officer = 0;
			form.officer_paramedic = 0;
			form.ems_supervisor = 0;
			form.chief = 0;
	}
	
	$scope.UpdateOrAddNewRecord = function(selectedForm) {
		if(selectedForm.name == 'Add New Response Form') {
			$scope.action = 'Insert';
		}
		else {
			$scope.action = 'Update';
		}
		
		if($scope.action == 'Insert') {
			$scope.resourceCounters[selectedForm.apparatus]++;
			
			var newForm = angular.copy(selectedForm);
			newForm.name = selectedForm.apparatus + $scope.resourceCounters[selectedForm.apparatus];

			$http.post(postUrl,newForm).success(function(data,status,headers){
				$http.get(headers('Location')+'?format=json').success(function(data){
				data.name = data.apparatus + $scope.resourceCounters[data.apparatus];
				$scope.forms.push(data);
				$scope.ClearForm($scope.selectedForm);
				$scope.selectedForm = data;
			});
			
			});	
		}
		else {
			var updateUrl = '/api/v1/capabilities/'+selectedForm.id+'/?format=json';
			$http.get(updateUrl).success(function(data){
				if(data.apparatus != $scope.selectedForm.apparatus) {
					$scope.resourceCounters[data.apparatus]--;
					$scope.resourceCounters[$scope.selectedForm.apparatus]++;
					$scope.selectedForm.name = $scope.selectedForm.apparatus + $scope.resourceCounters[$scope.selectedForm.apparatus];
				}
				$http.put(updateUrl,selectedForm);
			});
			
			
		}
	}
	
	$scope.DeleteForm = function(selectedForm) {
		
		$http.delete('/api/v1/capabilities/'+selectedForm.id+'/?format=json').success(function(data){
			$scope.resourceCounters[selectedForm.apparatus]--;
			$scope.forms.splice($scope.forms.indexOf(selectedForm),1);
			$scope.selectedForm = $scope.forms[0];
		});
	}
   
   L.marker(config.centroid).addTo($scope.map);
    L.tileLayer('https://{s}.tiles.mapbox.com/v3/examples.map-i87786ca/{z}/{x}/{y}.png', {'attribution': '© Mapbox'})
        .addTo($scope.map);

  });
})();
