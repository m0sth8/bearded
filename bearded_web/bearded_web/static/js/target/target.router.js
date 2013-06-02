/* global Bearded */
/* global Marionette */
/* global Backbone */


Bearded.module("TargetApp", function (TargetApp, App, Backbone, Marionette) {
    "use strict";

    var Router = Marionette.AppRouter.extend({
        appRoutes: {
            "target/": "showTargets",
            "": "showTargets"
        },

        // route filter before method
        // https://github.com/boazsender/backbone.routefilter
        before: function () {
            TargetApp.controller.show();
        }
    });

    // Initializer
    // -----------
    //
    TargetApp.addInitializer(function () {
        var router = new Router({controller: TargetApp.controller});
    });

});
