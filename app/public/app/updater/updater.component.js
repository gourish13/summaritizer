angular.module("updater", [
    'ngRoute',
]);

angular.module("updater").component("update", {
    template: "<navbar></navbar><update-form></update-form>"
});

angular.module("updater").component("navbar", {
    templateUrl: "/static/app/templates/navbar.template.html",
    controller: ['$location', '$document', function($location, $document) {
	this.id = "1";
	this.uuid = "3";
	this.goToRoute = function(nextRoute) {
	    if (nextRoute !== "view") return;
	    $location.path("/view/" + this.id + "/" + this.uuid);	
	}
	this.toggleNavMenu = function() {
	    angular.element($document[0].querySelectorAll('.navbar-menu')[0]).toggleClass('is-active');
	    angular.element($document[0].querySelectorAll('.navbar-burger')[0]).toggleClass('is-active');	    
	}
    }],
});

angular.module("updater").component("updateForm", {
    templateUrl: '/static/app/templates/form.template.html',
    controller: ['$element', '$location', 'simpleMdE', function($element, $location, simpleMdE) {

	this.loaded = true;
	simpleMdE.initEditor($element.find('textarea')[0]);
	this.author = 'Gourish Sadhu';
	this.hours = 1;
	this.minutes = 13;
	this.email = 'gust.coders@gmail.com';
	this.update = true;
	this.msg = "";


	//simpleMdE.setValue("# Hello, Gopal");
	
	this.anyFieldEmpty = function() {
	    return (
		this.author === "" ||
		this.hours === "" ||
		this.minutes === "" ||
		this.email === ""    
	    );
	}

	this.validEmail = function(valid) {
	    if (this.email === "") return "input is-primary";
	    if (valid) return "input is-success";
	    else return "input is-danger";
	}
    }],
    
});
