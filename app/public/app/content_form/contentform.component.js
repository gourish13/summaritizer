angular.module("contentForm", [
    "ngRoute",
]);

angular.module("contentForm").component("createForm", {
    templateUrl: '/static/app/templates/form.template.html',
    controller: ['$element', '$location', 'simpleMdE',  function($element, $location, simpleMdE) {

	simpleMdE.initEditor($element.find('textarea')[0]);
	this.author = '';
	this.hours='';
	this.minutes= '';
	this.update = false;
	this.msg = "";

	this.anyFieldEmpty = function() {
	    return (
		this.author === "" ||
		this.hours === "" ||
		this.minutes === ""
		    
	    );
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
