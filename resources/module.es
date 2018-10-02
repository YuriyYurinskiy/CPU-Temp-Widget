// the module should depend on 'core' to use the stock services & components
angular.module('example.cpu_temp_widget', [
    'core',
]);

angular.module('example.cpu_temp_widget').config(($routeProvider) => {
    $routeProvider.when('/view/cpu_temp_widget', {
        template: '<cpu-temp-widget></cpu-temp-widget>',
    });
});

angular.module('example.cpu_temp_widget').component('cpuTempWidget', {
    templateUrl: '/cpu_temp_widget:resources/index.html',
    controller: function (notify, pageTitle) {
        let ctrl = this;

        pageTitle.set('Cpu Temp Widget');

        ctrl.counter = 0;

        ctrl.click = () => {
            ctrl.counter += 1;
            notify.info('+1');
        };

        return this;
    }
});
