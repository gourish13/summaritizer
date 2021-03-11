angular.module("contentForm", [
    "ngRoute",
]);

angular.module("contentForm").component("createForm", {
    templateUrl: '/static/app/templates/form.template.html',
    controller: ['$element', '$location', '$http', '$httpParamSerializerJQLike', 'simpleMdE',  function($element, $location, $http, $httpParamSerializerJQLike, simpleMdE) {

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

	this.timeInvalid = function() {
	    return (
		this.hours === 0 && this.minutes === 0 ||
		this.hours === 24 && this.minutes !== 0 
	    );
	}

	this.validateHrsMins = function() {
	    if (this.hours === "" && this.minutes === "") return "input is-normal is-primary"
	    return "input is-normal " + ((this.timeInvalid()) ? "is-danger" : "is-success");   
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

	    let data = {};
	    data.author = this.author;
	    data.hours = this.hours;
	    data.minutes = this.minutes;
	    data.email = this.email;
	    data.content = simpleMdE.getValue();

	    let postReq = {
		method: 'POST',
		url: '/create',
		headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' },
		data: $httpParamSerializerJQLike(data)
	    };

	    $http(postReq)
		.then(function(response) {
		    $location.path(`/update/${response.data.id}/${response.data.uuid}`);
		})
		.catch(console.log)
	}
    }]
});
