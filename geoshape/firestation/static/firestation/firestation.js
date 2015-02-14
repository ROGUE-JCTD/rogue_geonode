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
					 
	var getUrl = '/api/v1/capabilities/?format=json';
	var fireUrl = thisFirestation + '?format=json';
	var postUrl = getUrl;
	
	$scope.firestation = $http.get(fireUrl);
	$http.get(getUrl).success(function(data){
		for(var iForm = 0; iForm < data.meta.total_count; iForm++) {
			if(data.objects[iForm].firestation == thisFirestation) {
				
				data.objects[iForm].name = data.objects[iForm].apparatus + data.objects[iForm].id;
				$scope.forms.push(data.objects[iForm]);
			}
		}
	});
	
	$scope.selectedForm = $scope.forms[0];
	
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
		
			$http.post(postUrl,selectedForm).success(function(data,status,headers){
				$http.get(headers('Location')+'?format=json').success(function(data){
				data.name = data.apparatus + data.id;
				$scope.forms.push(data);
				$scope.ClearForm($scope.selectedForm);
				$scope.selectedForm = data;
			});
			
			});	
		}
		else {
			var updateUrl = '/api/v1/capabilities/'+selectedForm.id+'/?format=json';
			
			$http.put(updateUrl,selectedForm).success(function(data){
				selectedForm.name = selectedForm.apparatus + selectedForm.id;
			});
			
			
		}
	}
	
	$scope.DeleteForm = function(selectedForm) {
		
		$http.delete('/api/v1/capabilities/'+selectedForm.id+'/?format=json').success(function(data){
			$scope.forms.splice($scope.forms.indexOf(selectedForm),1);
			$scope.selectedForm = $scope.forms[0];
		});
	}
   
   L.marker(config.centroid).addTo($scope.map);
    L.tileLayer('https://{s}.tiles.mapbox.com/v3/examples.map-i87786ca/{z}/{x}/{y}.png', {'attribution': '© Mapbox'})
        .addTo($scope.map);

  });
})();
