var app = angular.module('app', []);

app.controller("mainCtrl", ['$scope', '$http','$location','$window',function($scope, $http ,$location, $window){

    $scope.select_cook=[];
    $scope.select_nation=[];
    $scope.current_foodName="";
    $scope.current_EnumName="";
    $scope.current_targetName="";
    $scope.current_score="";
    var current_foodName = "";


    $scope.toggleSelection = function toggleSelection(select, Name) {
    // Array 안에 있으면 지우고 없으면 넣음
     var idx = select.indexOf(Name);
     if (idx > -1) { select.splice(idx, 1);}
     else { select.push(Name); }
    };


    $http.get('http://127.0.0.1:8080/admin/foodscore/getdata')
        .success(function(response){
            $scope.foodscore_cook_table = response.foodscore_cook;
            $scope.foodscore_taste_table = response.foodscore_taste;
            $scope.foodscore_nation_table = response.foodscore_nation;
        });


    $http.get('http://127.0.0.1:8080/admin/getdata')
        .success(
        function(response){
            $scope.food_tabledata = response.food;
            $scope.cook_tabledata = response.cook;
            $scope.nation_tabledata = response.nation;
            $scope.taste_tabledata = response.taste;
            $scope.user_tabledata = response.user;
            $scope.time_tabledata = response.time;
        });


    $scope.open_foodscore = function(temp){
        current_foodName = temp;
        $http.get('http://127.0.0.1:8080/admin/foodscore/'+ current_foodName)
            .success(function(response){
                $window.location.href = 'http://127.0.0.1:8080/admin/foodscore/' + current_foodName;
            });
    };

    $scope.update_foodscore = function(current_foodName, current_targetEnum, current_targetId, current_score){
        $http.post('http://127.0.0.1:8080/admin/foodscore/',
            angular.fromJson({ foodName : current_foodName,
                               targetEnum : current_targetEnum,
                               targetId : current_targetId,
                               score : current_score }))
            .success(function(response){
                alert('update')
            });
    };

    $scope.submitScore = function(){
        $http.post($location.absUrl(),
            angular.fromJson({ cookName : $scope.select_cook,
                                nationName : $scope.select_nation,
                                tasteScore : $scope.taste_tabledata }))
            .success(function(response){
                alert("submit");
            });
        $window.location.href = 'http://127.0.0.1:8080/admin/food'
    };

    $scope.delete_foodscore = function(current_foodName, current_targetEnum, current_targetId, current_score) {
        $http.post('http://127.0.0.1:8080/admin/foodscore/delete/',
            angular.fromJson({
                foodName: current_foodName,
                targetEnum: current_targetEnum,
                targetId: current_targetId,
                score: current_score
            }))
            .success(function (response) {
                alert('delete')
            });
        $http.get('http://127.0.0.1:8080/admin/foodscore/getdata')
        .success(function(response){
            $scope.foodscore_cook_table = response.foodscore_cook;
            $scope.foodscore_taste_table = response.foodscore_taste;
            $scope.foodscore_nation_table = response.foodscore_nation;
        });
    };

    $scope.submitFood = function(temp){
        if (temp == null){
            return alert('공백있음');
        }
        $http.post('http://127.0.0.1:8080/admin/food/add/', angular.fromJson({ foodName : temp }));
        $scope.formData_add_food = '';
        $http.get('http://127.0.0.1:8080/admin/getdata')
            .success(
            function(response){ $scope.food_tabledata = response.food }
            )
    };

    $scope.deleteFood = function(temp){
        if (temp == null){
            return alert('공백있음');
        }
        $http.post('http://127.0.0.1:8080/admin/food/delete/', angular.fromJson({ foodName : temp }));
        $scope.formData_del_food = '';
        $http.get('http://127.0.0.1:8080/admin/getdata')
            .success(
            function(response){ $scope.food_tabledata = response.food }
            )
    };

    $scope.submitCook = function(temp){
        if (temp == null){
            return alert('공백있음');
        }
        $http.post('http://127.0.0.1:8080/admin/cook/add/', angular.fromJson({ cookName : temp }));
        $scope.formData_add_cook = '';
        $http.get('http://127.0.0.1:8080/admin/getdata')
            .success(
            function(response){ $scope.cook_tabledata = response.cook }
            )
    };

    $scope.deleteCook = function(temp){
        if (temp == null){
            return alert('공백있음');
        }
        $http.post('http://127.0.0.1:8080/admin/cook/delete/', angular.fromJson({ cookName : temp }));
        $scope.formData_del_cook = '';
        $http.get('http://127.0.0.1:8080/admin/getdata')
            .success(
            function(response){ $scope.cook_tabledata = response.cook }
            )
    };

    $scope.submitNation = function(temp){
        if (temp == null){
            return alert('공백있음');
        }
        $http.post('http://127.0.0.1:8080/admin/nation/add/', angular.fromJson({ nationName : temp }));
        $scope.formData_add_nation = '';
        $http.get('http://127.0.0.1:8080/admin/getdata')
            .success(
            function(response){ $scope.nation_tabledata = response.nation }
            )
    };

    $scope.deleteNation = function(temp){
        if (temp == null){
            return alert('공백있음');
        }
        $http.post('http://127.0.0.1:8080/admin/nation/delete/', angular.fromJson({ nationName : temp }));
        $scope.formData_del_nation = '';
        $http.get('http://127.0.0.1:8080/admin/getdata')
            .success(
            function(response){ $scope.nation_tabledata = response.nation }
            )
    };

    $scope.submitTaste = function(temp){
        if (temp == null){
            return alert('공백있음');
        }
        $http.post('http://127.0.0.1:8080/admin/taste/add/', angular.fromJson({ tasteName : temp }));
        $scope.formData_add_taste = '';
        $http.get('http://127.0.0.1:8080/admin/getdata')
            .success(
            function(response){ $scope.taste_tabledata = response.taste }
            )
    };

    $scope.deleteTaste = function(temp){
        if (temp == null){
            return alert('공백있음');
        }
        $http.post('http://127.0.0.1:8080/admin/taste/delete/', angular.fromJson({ tasteName : temp }));
        $scope.formData_del_taste = '';
        $http.get('http://127.0.0.1:8080/admin/getdata')
            .success(
            function(response){ $scope.taste_tabledata = response.taste }
            )
    };

    $scope.submitTime = function(timeName, startTime){
        if (timeName == null || startTime == null){
            return alert('공백있음');
        }
        $http.post('http://127.0.0.1:8080/admin/time/add/', angular.fromJson({ timeName : timeName, startTime : startTime }));
        $scope.formData_add_time.timeName = '';
        $scope.formData_add_time.startTime = '';
        $http.get('http://127.0.0.1:8080/admin/getdata')
            .success(
            function(response){ $scope.time_tabledata = response.time }
            )
    };

    $scope.deleteTime = function(timeName){
        if (timeName == null){
            return alert('공백있음');
        }
        $http.post('http://127.0.0.1:8080/admin/time/delete/', angular.fromJson({ timeName : timeName }));
        $scope.formData_del_time.timeName = '';
        $scope.formData_del_time.startTime = '';
        $http.get('http://127.0.0.1:8080/admin/getdata')
            .success(
            function(response){ $scope.time_tabledata = response.time }
            )
    };

}]);