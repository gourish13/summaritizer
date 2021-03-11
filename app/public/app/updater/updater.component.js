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
    controller: ['$element', '$location', '$http', '$routeParams', '$httpParamSerializerJQLike', 'simpleMdE', function($element, $location, $http , $routeParams, $httpParamSerializerJQLike, simpleMdE) {

	this.loaded = false;
	simpleMdE.initEditor($element.find('textarea')[0]);
	this.author = '';
        this.content = '';
	this.update = true;
	this.msg = "";
	this.key = "";
        this.id = $routeParams.id;
        this.uuid = $routeParams.uuid;

        let self = this;

	$http.post(`/read/${this.id}/${this.uuid}`)
            .then(function(response) {
                self.author = response.data.author;
                self.content = response.data.content;
                simpleMdE.setValue(response.data.content);
                self.loaded = true;
            })
            .catch(console.log);
	
	//simpleMdE.setValue("# Hello, Gopal");
	
	this.anyFieldEmpty = function() {
	    return (
		this.author === "" ||
		this.key === ""
	    );
	}

	this.validEmail = function(valid) {
	    if (this.email === "") return "input is-primary";
	    if (valid) return "input is-success";
	    else return "input is-danger";
	}

	this.updateContent = function() {
	    if (simpleMdE.getValue().length === 0) {
		this.msg = "No content to save";
		return
	    }
	    if (simpleMdE.getValue() === this.content) {
		this.msg = "No new content to update";
		return
	    }
	    this.msg = "";
	    this.key = "";
	    $location.path('/update/1/3');
	}

	this.deleteContent = function() {
	    $location.path('/');
	}
    }],
    
});
