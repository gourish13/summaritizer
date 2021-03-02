angular.module("contentForm", [
    "ngRoute",
]);

angular.module("contentForm").component("createForm", {
    templateUrl: '/static/app/templates/form.template.html',
    controller: ['$element', '$location', 'simpleMdE',  function($element, $location, simpleMdE) {

	simpleMdE.initEditor($element.find('textarea')[0]);
	this.author = '';
	this.hours ='';
	this.minutes = '';
	this.email = '';
	this.update = false;
	this.msg = "";
	this.loaded = true;

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
	
	this.saveContent = function() {
	    if (simpleMdE.getValue().length === 0) {
		this.msg = "No content to save";
		return
	    }
	    this.msg = "";
	    $location.path('/update/1/3');
	}
    }]
});
