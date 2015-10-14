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
    $('.deleteAnchor').on('click', function (evt) {
        evt.preventDefault();

        if (confirm('Are you sure you want to delete this ' + $(this).attr('data-type') +' ?')) {
            $.post($(this).attr('href'), {_csrf_token: $(this).attr('data-csrf')}, function (response) {
                location.reload();
            }).error(function () {
                // csrf error
                alert('An error occured, please try again later!');
            });
        }
        return false;
    });

    /* Setup carousel */
    $('.carousel').carousel({
        interval: 5000
    });
}(jQuery);
