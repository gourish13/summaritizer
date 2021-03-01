angular.module("creater", [
    'ngRoute',
    'contentForm',
]);

angular.module("creater").component("homeIntro", {
    templateUrl: '/static/app/templates/intro.template.html',
    controller: ['particleJS', function(particleJS) {
	console.log("In intro controller");
	particleJS.startParticleMotion();
    }]
});

angular.module("creater").component("home", {
    template: "<home-intro></home-intro><create-form></create-form>"
})
