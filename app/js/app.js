'use strict';

// Declare app level module which depends on filters, and services
angular.module('bbqapp', ['bbqapp.controllers']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/home', {templateUrl: 'partials/home.html', controller: 'home'});
    $routeProvider.otherwise({redirectTo: '/home'});
  }]);
