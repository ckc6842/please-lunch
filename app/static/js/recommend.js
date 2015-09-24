angular.module('app')
    .controller('recommendCtrl', ['$scope','$http', function($scope, $http) {

        $scope.check_func = function(){
            $scope.recommend_check = true;
            $scope.re = "다시";
            $http.get(Flask.url_for('MainView:recommend_food'))
                .success(function(response){
                    $scope.recommend_food = response.foodName;
                })
        }

    }]);
