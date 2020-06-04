/**
 * Bootstrap Table Chinese translation
 * Author: Zhixin Wen<wenzhixin2010@gmail.com>
 */
(function ($) {
    'use strict';

    $.fn.bootstrapTable.locales['zh-CN'] = {
        formatLoadingMessage: function () {
            return 'trying hard loading data，please wait……';
        },
        formatRecordsPerPage: function (pageNumber) {
            return 'show ' + pageNumber + ' data each page';
        },
        formatShowingRows: function (pageFrom, pageTo, totalRows) {
            return 'show number of ' + pageFrom + ' to ' + pageTo + ' piece of info，total of ' + totalRows + ' data';
        },
        formatSearch: function () {
            return 'search';
        },
        formatNoMatches: function () {
            return 'no matched information';
        },
        formatPaginationSwitch: function () {
            return 'hide/show page';
        },
        formatRefresh: function () {
            return 'refresh';
        },
        formatToggle: function () {
            return 'switch view';
        },
        formatColumns: function () {
            return 'column';
        },
        formatExport: function () {
            return 'export data';
        },
        formatClearFilters: function () {
            return 'clear filter';
        }
    };

    $.extend($.fn.bootstrapTable.defaults, $.fn.bootstrapTable.locales['zh-CN']);

})(jQuery);
