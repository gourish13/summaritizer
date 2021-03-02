angular.module('updater').service("simpleMdE", function() {
    var simplemde;
    this.initEditor =  function(element) {
	simplemde = new SimpleMDE({
		element: element,
	        spellChecker: true,
	        hideIcons: ["guide"],
	        renderingConfig: {
		        singleLineBreaks: false,
		        codeSyntaxHighlighting: true,
		},
	});
    }
    this.getValue = function() {
	console.log(simplemde.value())
	return simplemde.value();
    }
    this.setValue = function(mdContent) {
	simplemde.value(mdContent);
    }
})
