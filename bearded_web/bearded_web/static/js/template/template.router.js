/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module("TemplateApp", function(TemplateApp, App) {
    "use strict";

    var Router = Marionette.AppRouter.extend({
        appRoutes: {
            'template/': 'showTemplates',
            'template/new/': 'newTemplate'
        },

        // route filter before method
        // https://github.com/boazsender/backbone.routefilter
        before: function() {
            TemplateApp.controller.show();
        }
    });

    TemplateApp.addInitializer(function() {
        var router = new Router({controller: TemplateApp.controller});
    });

});
