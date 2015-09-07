angular.module('app')
    .controller('startCtrl', ['$scope','$http', '$rootScope', '$state', function($scope, $http, $rootScope, $state) {
        var url = "http://pleaselunch.tk"+Flask.url_for("StartView:getfoodlist");

        $http.get('http://127.0.0.1:8080/getfoodlist/')
        .success(function(response){
            $scope.foodlist = response.foodlist;
        });

        $scope.sendrating = function(rating, foodName, userId){
            $http.post('http://127.0.0.1:8080/getfoodlist/', angular.fromJson({userId : userId, foodName : foodName, rating : rating}))
            alert(foodName + " is " +rating +"점 " + userId);
        }

    }]);
