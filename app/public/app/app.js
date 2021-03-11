angular.module("Summaritizer", [
    'ngRoute',
    'creater',
    'updater',
]);


angular.module("Summaritizer").config(['$routeProvider', function($routeProvider) {
    $routeProvider
	.when('/', {
	    template: '<home></home>',
	    title: "Home"
	})
	.when('/view/:id/:uuid', {
	    template: '<h1>Viewer</h1>',
	    title: "View"
	})
    .when('/update/:id/:uuid', {
	    template: '<update></update>',
	    title: "Update"
	})
        .otherwise('/');
}]);


angular.module("Summaritizer").config(['$locationProvider', function($locationProvider) {
    $locationProvider.html5Mode(true);
}]);

angular.module("Summaritizer").run(['$rootScope', '$route', function($rootScope, $route) {
    $rootScope.$on("$routeChangeSuccess", function(currentRoute, previousRoute) {
	$rootScope.title = $route.current.title;
    });
}]);
