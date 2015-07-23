var app = angular.module('app', []);

app.controller("subCtrl", ['$scope', '$http', function($scope, $http){

    $scope.submitData = function(temp){
        $http.post('http://127.0.0.1:8080/admin/',
            angular.fromJson({
            foodName : temp
        }))
        $http.get('http://127.0.0.1:8080/admin/').success(
			function(data)
			{
				$scope.foodlist = data;
			});

    };

}])