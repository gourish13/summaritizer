angular.module('contentForm').service("simpleMdE", function() {
    var simplemde;
    this.initEditor =  function(element) {
	simplemde = new SimpleMDE({
		element: element,
		spellChecker: true,
	        renderingConfig: {
		        singleLineBreaks: false,
		        codeSyntaxHighlighting: true,
		},
	});
    }
    this.value = function() {
	return simplemde.value();
    }
    this.value = function(mdContent) {
	simplemde.value(mdContent);
    }
})
