angular.module('ajenti.cpu_temp_widget').controller 'Demo5WidgetController', ($scope) ->
    # $scope.widget is our widget descriptor here
    $scope.$on 'widget-update', ($event, id, data) ->
        if id != $scope.widget.id
            return
        $scope.value = data
