angular.module('app')
    .controller('startCtrl', ['$scope','$http', '$rootScope', '$state', function($scope, $http, $rootScope, $state) {

        $http.get(Flask.url_for('StartView:getFoodList'))
        .success(function(response){
            $scope.foodlist = response.foodlist;
        });

        $http.get(Flask.url_for('StartView:evalcount'))
            .success(function(response){
                $scope.UserEvalCount = response.UserEvalCount;
                $scope.UserLeftCount = 10 - response.UserEvalCount
            })

        $scope.sendrating = function(rating, foodName, userId, $index){
            $http.post(Flask.url_for('StartView:post'), angular.fromJson({userId : userId, foodName : foodName, rating : rating}));
            alert(foodName + " is " +rating +"점 " + userId);
            $scope.foodlist.splice ($index, 1);

            $http.get(Flask.url_for('StartView:evalcount'))
            .success(function(response){
                $scope.UserEvalCount = response.UserEvalCount;
                $scope.UserLeftCount = 10 - response.UserEvalCount
            })
        }

    }]);
