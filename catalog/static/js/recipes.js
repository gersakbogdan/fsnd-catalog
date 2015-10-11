/**
 * Custom javascript code for Recipes Catalog
 * jQuery library is required
 */

if (typeof jQuery === 'undefined') {
  throw new Error('Bootstrap\'s JavaScript requires jQuery')
}

+function ($) {
    'use strict';

    /* Confirm category delete action */
    $('.deleteCategoryAnchor').on('click', function (evt) {
        evt.preventDefault();

        if (confirm('Are you sure you want to delete this category?')) {
            $.post($(this).attr('href'), function (response) {
                location.reload();
            });
        }
        return false;
    });
}(jQuery);
