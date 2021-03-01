angular.module("creater").service("particleJS", function() {
    this.startParticleMotion = function() {
	particlesJS.load("particles-js", '/static/particles.conf.json', function() {
	    console.log('Particle.js config loaded');
	});
    }
});

