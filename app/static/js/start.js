angular.module('app')
    .controller('startCtrl', ['$scope','$http', '$rootScope', '$state', function($scope, $http, $rootScope, $state) {

        $http.get('http://127.0.0.1:8080/start/getfoodlist')
        .success(function(response){
            $scope.foodlist = response.foodlist;
        });

        $scope.sendrating = function(rating, foodName, userId){
            alert(foodName + " is " +rating +"점 " + userId);
        }

    }]);