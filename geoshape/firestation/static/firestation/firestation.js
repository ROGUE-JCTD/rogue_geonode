'use strict';

(function() {
  angular.module('fireStation', [])

  .config(function($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  })

  .controller('fireStationController', function($scope, $window) {
    $scope.forms = [{'name':'Add New Response Form',
					 'apparatus':'Engine',
					 'firefighter':0,
					 'firefighter_emt':0,
					 'firefighter_paramedic':0,
					 'ems_emt':0,
					 'ems_paramedic':0,
					 'officer':0,
					 'officer_paramedic':0,
					 'ems_supervisor':0,
					 'chief':0}];
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
	$scope.selectedForm = $scope.forms[0];
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
	
	$scope.UpdateOrAddNewRecord = function(selectedForm) {
		if(selectedForm.name == 'Add New Response Form') {
			$scope.action = 'Insert';
		}
		else {
			$scope.action = 'Update';
		}
		
	}
    L.marker(config.centroid).addTo($scope.map);
    L.tileLayer('https://{s}.tiles.mapbox.com/v3/examples.map-i87786ca/{z}/{x}/{y}.png', {'attribution': '© Mapbox'})
        .addTo($scope.map);

  });
})();
