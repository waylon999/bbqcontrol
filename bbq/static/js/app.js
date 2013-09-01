'use strict';

// Declare app level module which depends on filters, and services
var BBQApp = angular.module('bbqapp', []);

BBQApp.config(function($routeProvider) {
  $routeProvider.when('/home', {
    templateUrl: 'static/partials/home.html',
    resolve: {
      data: function () {
      }
    },
    controller: 'home'
  });
  $routeProvider.when('/away', {
    templateUrl: 'static/partials/home.html',
    controller: 'away'
  });
  $routeProvider.otherwise({redirectTo: '/home'});
});


