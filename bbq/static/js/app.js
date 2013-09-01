'use strict';

// Declare app level module which depends on filters, and services
var BBQApp = angular.module('bbqapp', ['ngCookies']);

BBQApp.run(function ($http, $cookies) {
  $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});

BBQApp.config(function($routeProvider) {
  $routeProvider.when('/home', {
    templateUrl: '/static/partials/home.html',
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


