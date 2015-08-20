/* ============================================================
 * File: config.js
 * Configure routing
 * ============================================================ */

angular.module('app')
    .config(['$stateProvider', '$urlRouterProvider', '$ocLazyLoadProvider',

        function($stateProvider, $urlRouterProvider, $ocLazyLoadProvider) {

            $stateProvider
                .state('app', {
                    abstract: true,
                    url: "/app",
                    templateUrl: "/static/tpl/app.html"
                })
                .state('app.dashboard', {
                    url: "/dashboard",
                    templateUrl: "/static/tpl/dashboard.html",
                    controller: 'DashboardCtrl',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'nvd3',
                                    'mapplic',
                                    'rickshaw',
                                    'metrojs',
                                    'sparkline',
                                    'skycons',
                                    'switchery'
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load([
                                        '/static/assets/js/controllers/dashboard.js'
                                    ]);
                                });
                        }]
                    }
                })

            // Email app
            .state('app.email', {
                    abstract: true,
                    url: '/email',
                    templateUrl: '/static/tpl/apps/email/email.html',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'menuclipper',
                                    'wysihtml5'
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load([
                                        '/static/assets/js/apps/email/service.js',
                                        '/static/assets/js/apps/email/email.js'
                                    ])
                                });
                        }]
                    }
                })
                .state('app.email.inbox', {
                    url: '/inbox/:emailId',
                    templateUrl: '/static/tpl/apps/email/email_inbox.html'
                })
                .state('app.email.compose', {
                    url: '/compose',
                    templateUrl: '/static/tpl/apps/email/email_compose.html'
                })
                // Social app
                .state('app.social', {
                    url: '/social',
                    templateUrl: '/static/tpl/apps/social/social.html',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'isotope',
                                    'stepsForm'
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load([
                                        '/static/pages/js/pages.social.min.js',
                                        '/static/assets/js/apps/social/social.js'
                                    ])
                                });
                        }]
                    }
                })
                //Calendar app
                .state('app.calendar', {
                    url: '/calendar',
                    templateUrl: '/static/tpl/apps/calendar/calendar.html',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'switchery',
                                    'jquery-ui',
                                    'moment',
                                    'hammer'
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load([
                                        '/static/pages/js/pages.calendar.min.js',
                                        '/static/assets/js/apps/calendar/calendar.js'
                                    ])
                                });
                        }]
                    }
                })
                .state('app.builder', {
                    url: '/builder',
                    template: '<div></div>',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                '/static/assets/js/controllers/builder.js',
                            ]);
                        }]
                    }
                })

            // UI Elements 
            .state('app.ui', {
                    url: '/ui',
                    template: '<div ui-view></div>'
                })
                .state('app.ui.color', {
                    url: '/color',
                    templateUrl: '/static/tpl/ui_color.html'
                })
                .state('app.ui.typo', {
                    url: '/typo',
                    templateUrl: '/static/tpl/ui_typo.html'
                })
                .state('app.ui.icons', {
                    url: '/icons',
                    templateUrl: '/static/tpl/ui_icons.html',
                    controller: 'IconsCtrl',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'sieve',
                                    'line-icons'
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load([
                                        'assets/js/controllers/icons.js'
                                    ])
                                });
                        }]
                    }
                })
                .state('app.ui.buttons', {
                    url: '/buttons',
                    templateUrl: '/static/tpl/ui_buttons.html'
                })
                .state('app.ui.notifications', {
                    url: '/notifications',
                    templateUrl: '/static/tpl/ui_notifications.html',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                'assets/js/controllers/notifications.js'
                            ]);
                        }]
                    }
                })
                .state('app.ui.modals', {
                    url: '/modals',
                    templateUrl: '/static/tpl/ui_modals.html',
                    controller: 'ModalsCtrl',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                'assets/js/controllers/modals.js'
                            ]);
                        }]
                    }
                })
                .state('app.ui.progress', {
                    url: '/progress',
                    templateUrl: '/static/tpl/ui_progress.html'
                })
                .state('app.ui.tabs', {
                    url: '/tabs',
                    templateUrl: '/static/tpl/ui_tabs.html'
                })
                .state('app.ui.sliders', {
                    url: '/sliders',
                    templateUrl: '/static/tpl/ui_sliders.html',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                'noUiSlider',
                                'ionRangeSlider'
                            ], {
                                insertBefore: '#lazyload_placeholder'
                            });
                        }]
                    }
                })
                .state('app.ui.treeview', {
                    url: '/treeview',
                    templateUrl: '/static/tpl/ui_treeview.html',
                    controller: 'TreeCtrl',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'navTree'
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load('assets/js/controllers/treeview.js');
                                });
                        }]
                    }
                })
                .state('app.ui.nestables', {
                    url: '/nestables',
                    templateUrl: '/static/tpl/ui_nestable.html',
                    controller: 'NestableCtrl',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'nestable'
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load('assets/js/controllers/nestable.js');
                                });
                        }]
                    }
                })

            // Form elements
            .state('app.forms', {
                    url: '/forms',
                    template: '<div ui-view></div>'
                })
                .state('app.forms.elements', {
                    url: '/elements',
                    templateUrl: '/static/tpl/forms_elements.html',
                    controller: 'FormElemCtrl',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'switchery',
                                    'select',
                                    'moment',
                                    'datepicker',
                                    'daterangepicker',
                                    'timepicker',
                                    'inputMask',
                                    'autonumeric',
                                    'wysihtml5',
                                    'summernote',
                                    'tagsInput',
                                    'dropzone'
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load('assets/js/controllers/forms_elements.js');
                                });
                        }]
                    }
                })
                .state('app.forms.layouts', {
                    url: '/layouts',
                    templateUrl: '/static/tpl/forms_layouts.html',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'datepicker',
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load('assets/js/controllers/forms_layouts.js');
                                });
                        }]
                    }
                })
                .state('app.forms.wizard', {
                    url: '/wizard',
                    templateUrl: '/static/tpl/forms_wizard.html',
                    controller: 'FormWizardCtrl',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'wizard'
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load('assets/js/controllers/forms_wizard.js');
                                });
                        }]
                    }
                })

            // Portlets
            .state('app.portlets', {
                url: '/portlets',
                templateUrl: '/static/tpl/portlets.html',
                controller: 'PortletCtrl',
                resolve: {
                    deps: ['$ocLazyLoad', function($ocLazyLoad) {
                        return $ocLazyLoad.load([
                            'assets/js/controllers/portlets.js'
                        ]);
                    }]
                }
            })

            // Tables
            .state('app.tables', {
                    url: '/tables',
                    template: '<div ui-view></div>'
                })
                .state('app.tables.basic', {
                    url: '/basic',
                    templateUrl: '/static/tpl/tables_basic.html',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'dataTables'
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load('assets/js/controllers/tables.js');
                                });
                        }]
                    }
                })
                .state('app.tables.dataTables', {
                    url: '/dataTables',
                    templateUrl: '/static/tpl/tables_dataTables.html',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'dataTables'
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load('assets/js/controllers/dataTables.js');
                                });
                        }]
                    }
                })

            // Maps
            .state('app.maps', {
                    url: '/maps',
                    template: '<div class="full-height full-width" ui-view></div>'
                })
                .state('app.maps.google', {
                    url: '/google',
                    templateUrl: '/static/tpl/maps_google_map.html',
                    controller: 'GoogleMapCtrl',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'google-map'
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load('assets/js/controllers/google_map.js')
                                        .then(function() {
                                            return loadGoogleMaps();
                                        });
                                });
                        }]
                    }
                })
                .state('app.maps.vector', {
                    url: '/vector',
                    templateUrl: '/static/tpl/maps_vector_map.html',
                    controller: 'VectorMapCtrl',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'mapplic',
                                    'select'
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load('assets/js/controllers/vector_map.js');
                                });
                        }]
                    }
                })

            // Charts
            .state('app.charts', {
                url: '/charts',
                templateUrl: '/static/tpl/charts.html',
                controller: 'ChartsCtrl',
                resolve: {
                    deps: ['$ocLazyLoad', function($ocLazyLoad) {
                        return $ocLazyLoad.load([
                                'nvd3',
                                'rickshaw',
                                'sparkline'
                            ], {
                                insertBefore: '#lazyload_placeholder'
                            })
                            .then(function() {
                                return $ocLazyLoad.load('assets/js/controllers/charts.js');
                            });
                    }]
                }
            })

            // Extras
            .state('app.extra', {
                    url: '/extra',
                    template: '<div ui-view></div>'
                })
                .state('app.extra.invoice', {
                    url: '/invoice',
                    templateUrl: '/static/tpl/extra_invoice.html'
                })
                .state('app.extra.blank', {
                    url: '/blank',
                    templateUrl: '/static/tpl/extra_blank.html'
                })
                .state('app.extra.gallery', {
                    url: '/gallery',
                    templateUrl: '/static/tpl/extra_gallery.html',
                    resolve: {
                        deps: ['$ocLazyLoad', function($ocLazyLoad) {
                            return $ocLazyLoad.load([
                                    'isotope',
                                    'codropsDialogFx',
                                    'metrojs',
                                    'owlCarousel',
                                    'noUiSlider'
                                ], {
                                    insertBefore: '#lazyload_placeholder'
                                })
                                .then(function() {
                                    return $ocLazyLoad.load('assets/js/controllers/gallery.js');
                                });
                        }]
                    }
                })
                .state('app.extra.timeline', {
                    url: '/timeline',
                    templateUrl: '/static/tpl/extra_timeline.html'
                })

            // Extra - Others
            .state('access', {
                    url: '/access',
                    template: '<div class="full-height" ui-view></div>'
                })
                .state('access.404', {
                    url: '/404',
                    templateUrl: '/static/tpl/extra_404.html'
                })
                .state('access.500', {
                    url: '/500',
                    templateUrl: '/static/tpl/extra_500.html'
                })
                .state('access.login', {
                    url: '/login',
                    templateUrl: '/static/tpl/extra_login.html'
                })
                .state('access.register', {
                    url: '/register',
                    templateUrl: '/static/tpl/extra_register.html'
                })
                .state('access.lock_screen', {
                    url: '/lock_screen',
                    templateUrl: '/static/tpl/extra_lock_screen.html'
                })

        }
    ]);