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
								'Heavy Rescue',
								'Boat',
								'Hazmat',
								'Chief',
								'Other'];
    $scope.forms = [];
					 
	var getUrl = '/api/v1/capabilities/?firestation='+config.id+'&format=json';
	$http.get(getUrl).success(function(data){
		for(var iForm = 0; iForm < data.meta.total_count; iForm++) {
			data.objects[iForm].name = data.objects[iForm].apparatus + data.objects[iForm].id;
		}
		$scope.forms = data.objects;
	});
	
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
	};
	
	$scope.AddForm = function() {
		var newForm = {'apparatus': 'Engine',
						'chief_officer': 0,
						'ems_emt': 0,
						'ems_paramedic': 0,
						'ems_supervisor': 0,
						'firefighter': 0,
						'firefighter_emt': 0,
						'firefighter_paramedic': 0,
						'firestation': thisFirestation,
						'officer': 0,
						'officer_paramedic': 0
						};
		var postUrl = '/api/v1/capabilities/?format=json';
		$http.post(postUrl, newForm).success(function(data,status,headers){
				$http.get(headers('Location')+'?format=json').success(function(data){
				data.name = data.apparatus + data.id;
				$scope.forms.push(data);
				});
		});
	};
	
	$scope.UpdateForm = function(form) {
			var updateUrl = '/api/v1/capabilities/'+form.id+'/?format=json';
			
			$http.put(updateUrl,form).success(function(data){
				form.name = form.apparatus + form.id;
			});
	};
	
	$scope.DeleteForm = function(form) {
		
		$http.delete('/api/v1/capabilities/'+form.id+'/?format=json').success(function(data){
            $scope.forms.splice($scope.forms.indexOf(form), 1);
		});

        $('.apparatus-tabs li:nth-last-child(2) a').tab('show');
	};
   
   L.marker(config.centroid).addTo($scope.map);
    L.tileLayer('https://{s}.tiles.mapbox.com/v3/examples.map-i87786ca/{z}/{x}/{y}.png', {'attribution': '© Mapbox'})
        .addTo($scope.map);

  });
})();
