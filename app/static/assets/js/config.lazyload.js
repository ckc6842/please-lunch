/* ============================================================
 * File: config.lazyload.js
 * Configure modules for ocLazyLoader. These are grouped by 
 * vendor libraries. 
 * ============================================================ */

angular.module('app')
    .config(['$ocLazyLoadProvider', function($ocLazyLoadProvider) {
        $ocLazyLoadProvider.config({
            debug: true,
            events: true,
            modules: [{
                    name: 'isotope',
                    files: [
                        '/static/asset/plugins/imagesloaded/imagesloaded.pkgd.min.js',
                        '/static/asset/plugins/jquery-isotope/isotope.pkgd.min.js'
                    ]
                }, {
                    name: 'codropsDialogFx',
                    files: [
                        '/static/asset/plugins/codrops-dialogFx/dialogFx.js',
                        '/static/asset/plugins/codrops-dialogFx/dialog.css',
                        '/static/asset/plugins/codrops-dialogFx/dialog-sandra.css'
                    ]
                }, {
                    name: 'metrojs',
                    files: [
                        '/static/asset/plugins/jquery-metrojs/MetroJs.min.js',
                        '/static/asset/plugins/jquery-metrojs/MetroJs.css'
                    ]
                }, {
                    name: 'owlCarousel',
                    files: [
                        '/static/asset/plugins/owl-carousel/owl.carousel.min.js',
                        '/static/asset/plugins/owl-carousel//static/asset/owl.carousel.css'
                    ]
                }, {
                    name: 'noUiSlider',
                    files: [
                        '/static/asset/plugins/jquery-nouislider/jquery.nouislider.min.js',
                        '/static/asset/plugins/jquery-nouislider/jquery.liblink.js',
                        '/static/asset/plugins/jquery-nouislider/jquery.nouislider.css'
                    ]
                }, {
                    name: 'nvd3',
                    files: [
                        '/static/asset/plugins/nvd3/lib/d3.v3.js',
                        '/static/asset/plugins/nvd3/nv.d3.min.js',
                        '/static/asset/plugins/nvd3/src/utils.js',
                        '/static/asset/plugins/nvd3/src/tooltip.js',
                        '/static/asset/plugins/nvd3/src/interactiveLayer.js',
                        '/static/asset/plugins/nvd3/src/models/axis.js',
                        '/static/asset/plugins/nvd3/src/models/line.js',
                        '/static/asset/plugins/nvd3/src/models/lineWithFocusChart.js',
                        '/static/asset/plugins/angular-nvd3/angular-nvd3.js',
                        '/static/asset/plugins/nvd3/nv.d3.min.css'
                    ],
                    serie: true // load in the exact order
                }, {
                    name: 'rickshaw',
                    files: [
                        '/static/asset/plugins/nvd3/lib/d3.v3.js',
                        '/static/asset/plugins/rickshaw/rickshaw.min.js',
                        '/static/asset/plugins/angular-rickshaw/rickshaw.js',
                        '/static/asset/plugins/rickshaw/rickshaw.min.css',
                    ],
                    serie: true
                }, {
                    name: 'sparkline',
                    files: [
                    '/static/asset/plugins/jquery-sparkline/jquery.sparkline.min.js',
                    '/static/asset/plugins/angular-sparkline/angular-sparkline.js'
                    ]
                }, {
                    name: 'mapplic',
                    files: [
                        '/static/asset/plugins/mapplic/js/hammer.js',
                        '/static/asset/plugins/mapplic/js/jquery.mousewheel.js',
                        '/static/asset/plugins/mapplic/js/mapplic.js',
                        '/static/asset/plugins/mapplic/css/mapplic.css'
                    ]
                }, {
                    name: 'skycons',
                    files: ['/static/asset/plugins/skycons/skycons.js']
                }, {
                    name: 'switchery',
                    files: [
                        '/static/asset/plugins/switchery/js/switchery.min.js',
                        '/static/asset/plugins/ng-switchery/ng-switchery.js',
                        '/static/asset/plugins/switchery/css/switchery.min.css',
                    ]
                }, {
                    name: 'menuclipper',
                    files: [
                        '/static/asset/plugins/jquery-menuclipper/jquery.menuclipper.css',
                        '/static/asset/plugins/jquery-menuclipper/jquery.menuclipper.js'
                    ]
                }, {
                    name: 'wysihtml5',
                    files: [
                        '/static/asset/plugins/bootstrap3-wysihtml5/bootstrap3-wysihtml5.min.css',
                        '/static/asset/plugins/bootstrap3-wysihtml5/bootstrap3-wysihtml5.all.min.js'
                    ]
                }, {
                    name: 'stepsForm',
                    files: [
                        '/static/asset/plugins/codrops-stepsform/css/component.css',
                        '/static/asset/plugins/codrops-stepsform/js/stepsForm.js'
                    ]
                }, {
                    name: 'jquery-ui',
                    files: ['/static/asset/plugins/jquery-ui-touch/jquery.ui.touch-punch.min.js']
                }, {
                    name: 'moment',
                    files: ['/static/asset/plugins/moment/moment.min.js',
                        '/static/asset/plugins/moment/moment-with-locales.min.js'
                    ]
                }, {
                    name: 'hammer',
                    files: ['/static/asset/plugins/hammer.min.js']
                }, {
                    name: 'sieve',
                    files: ['/static/asset/plugins/jquery.sieve.min.js']
                }, {
                    name: 'line-icons',
                    files: ['/static/asset/plugins/simple-line-icons/simple-line-icons.css']
                }, {
                    name: 'ionRangeSlider',
                    files: [
                        '/static/asset/plugins/ion-slider/css/ion.rangeSlider.css',
                        '/static/asset/plugins/ion-slider/css/ion.rangeSlider.skinFlat.css',
                        '/static/asset/plugins/ion-slider/js/ion.rangeSlider.min.js'
                    ]
                }, {
                    name: 'navTree',
                    files: [
                        '/static/asset/plugins/angular-bootstrap-nav-tree/abn_tree_directive.js',
                        '/static/asset/plugins/angular-bootstrap-nav-tree/abn_tree.css'
                    ]
                }, {
                    name: 'nestable',
                    files: [
                        '/static/asset/plugins/jquery-nestable/jquery.nestable.css',
                        '/static/asset/plugins/jquery-nestable/jquery.nestable.js',
                        '/static/asset/plugins/angular-nestable/angular-nestable.js'
                    ]
                }, {
                    //https://github.com/angular-ui/ui-select
                    name: 'select',
                    files: [
                        '/static/asset/plugins/bootstrap-select2/select2.css',
                        '/static/asset/plugins/angular-ui-select/select.min.css',
                        '/static/asset/plugins/angular-ui-select/select.min.js'
                    ]
                }, {
                    name: 'datepicker',
                    files: [
                        '/static/asset/plugins/bootstrap-datepicker/css/datepicker3.css',
                        '/static/asset/plugins/bootstrap-datepicker/js/bootstrap-datepicker.js',
                    ]
                }, {
                    name: 'daterangepicker',
                    files: [
                        '/static/asset/plugins/bootstrap-daterangepicker/daterangepicker-bs3.css',
                        '/static/asset/plugins/bootstrap-daterangepicker/daterangepicker.js'
                    ]
                }, {
                    name: 'timepicker',
                    files: [
                        '/static/asset/plugins/bootstrap-timepicker/bootstrap-timepicker.min.css',
                        '/static/asset/plugins/bootstrap-timepicker/bootstrap-timepicker.min.js'
                    ]
                }, {
                    name: 'inputMask',
                    files: [
                        '/static/asset/plugins/jquery-inputmask/jquery.inputmask.min.js'
                    ]
                }, {
                    name: 'autonumeric',
                    files: [
                        '/static/asset/plugins/jquery-autonumeric/autoNumeric.js'
                    ]
                }, {
                    name: 'summernote',
                    files: [
                        '/static/asset/plugins/summernote/css/summernote.css',
                        '/static/asset/plugins/summernote/js/summernote.min.js',
                        '/static/asset/plugins/angular-summernote/angular-summernote.min.js'
                    ],
                    serie: true // load in the exact order
                }, {
                    name: 'tagsInput',
                    files: [
                        '/static/asset/plugins/bootstrap-tag/bootstrap-tagsinput.css',
                        '/static/asset/plugins/bootstrap-tag/bootstrap-tagsinput.min.js'
                    ]
                }, {
                    name: 'dropzone',
                    files: [
                        '/static/asset/plugins/dropzone/css/dropzone.css',
                        '/static/asset/plugins/dropzone/dropzone.min.js',
                        '/static/asset/plugins/angular-dropzone/angular-dropzone.js'
                    ]
                }, {
                    name: 'wizard',
                    files: [
                        '/static/asset/plugins/lodash/lodash.min.js',
                        '/static/asset/plugins/angular-wizard/angular-wizard.min.css',
                        '/static/asset/plugins/angular-wizard/angular-wizard.min.js'
                    ]
                }, {
                    name: 'dataTables',
                    files: [
                        '/static/asset/plugins/jquery-datatable/media/css/jquery.dataTables.css',
                        '/static/asset/plugins/jquery-datatable/extensions/FixedColumns/css/dataTables.fixedColumns.min.css',
                        '/static/asset/plugins/datatables-responsive/css/datatables.responsive.css',
                        '/static/asset/plugins/jquery-datatable/media/js/jquery.dataTables.min.js',
                        '/static/asset/plugins/jquery-datatable/extensions/TableTools/js/dataTables.tableTools.min.js',
                        '/static/asset/plugins/jquery-datatable/extensions/Bootstrap/jquery-datatable-bootstrap.js',
                        '/static/asset/plugins/datatables-responsive/js/datatables.responsive.js',
                        '/static/asset/plugins/datatables-responsive/js/lodash.min.js'
                    ],
                    serie: true // load in the exact order
                }, {
                    name: 'google-map',
                    files: [
                        '/static/asset/plugins/angular-google-map-loader/google-map-loader.js',
                        '/static/asset/plugins/angular-google-map-loader/google-maps.js'
                    ]
                }

            ]
        });
    }]);