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
    $scope.forms = [{'apparatus':'Engine'}];
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
    $scope.map = L.map('map', options).setView(config.centroid, 13);
    L.marker(config.centroid).addTo($scope.map);
    L.tileLayer('https://{s}.tiles.mapbox.com/v3/examples.map-i87786ca/{z}/{x}/{y}.png', {'attribution': '© Mapbox'})
        .addTo($scope.map);

  });
})();
