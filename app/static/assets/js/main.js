/* ============================================================
 * File: main.js
 * Main Controller to set global scope variables. 
 * ============================================================ */

angular.module('app')
    .controller('AppCtrl', ['$scope','$http', '$rootScope', '$state', function($scope, $http, $rootScope, $state) {
        // App globals
        $scope.app = {
            name: 'please-lunch',
            description: 'Admin Dashboard UI kit',
            layout: {
                menuPin: false,
                menuBehind: false,
                theme: '/static/pages/css/pages.css'
            },
            author: 'jongho'
        }
        // Checks if the given state is the current state
        $scope.is = function(name) {
            return $state.is(name);
        }

        // Checks if the given state/child states are present
        $scope.includes = function(name) {
            return $state.includes(name);
        }

        // Broadcasts a message to pgSearch directive to toggle search overlay
        $scope.showSearchOverlay = function() {
            $scope.$broadcast('toggleSearchOverlay', {
                show: true
            })
        }


    }]);


angular.module('app')
    /*
     Use this directive together with ng-include to include a
     template file by replacing the placeholder element
     */

    .directive('includeReplace', function() {
        return {
            require: 'ngInclude',
            restrict: 'A',
            link: function(scope, el, attrs) {
                el.replaceWith(el.children());
            }
        };
    })