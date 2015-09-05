angular.module('app')
    .controller('startCtrl', ['$scope','$http', '$rootScope', '$state', function($scope, $http, $rootScope, $state) {

        $http.get('http://pleaselunch.tk/start/getfoodlist/')
        .success(function(response){
            $scope.foodlist = response.foodlist;
        });

        $scope.sendrating = function(rating, foodName, userId){
            $http.post('http://pleaselunch.tk/start/getfoodlist/', angular.fromJson({userId : userId, foodName : foodName, rating : rating}))
            alert(foodName + " is " +rating +"점 " + userId);
        }

    }]);
