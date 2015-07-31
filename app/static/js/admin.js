var app = angular.module('app', []);

app.controller("mainCtrl", ['$scope', '$http', function($scope, $http){

    $http.get('http://127.0.0.1:8080/admin/food/dataget')
        .success(
        function(response){ $scope.tabledata = response.food }
        )

    $scope.submitFood = function(temp){

        $http.post('http://127.0.0.1:8080/admin/food/add', angular.fromJson({ foodName : temp }));
        $scope.formData_add_food = '';
        $http.get('http://127.0.0.1:8080/admin/food/dataget')
            .success(
            function(response){ $scope.tabledata = response.food }
            )
    };

    $scope.deleteFood = function(temp){

        $http.post('http://127.0.0.1:8080/admin/food/delete', angular.fromJson({ foodName : temp }));
        $scope.formData_del_food = '';
        $http.get('http://127.0.0.1:8080/admin/food/dataget')
            .success(
            function(response){ $scope.tabledata = response.food }
            )
    };


}])