var app = angular.module('app', []);

app.controller("subCtrl", ['$scope', '$http', function($scope, $http){
    var users = [];
    $scope.tempData = {};
    $scope.tempData.users = users;
    $scope.submitData = function(temp){
        $http.post('http://127.0.0.1:8080/admin/', angular.fromJson({ foodName : temp }))
        users.push(angular.fromJson({ name : temp }));
    };
}])