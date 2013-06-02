/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module("TargetApp", function (TargetApp, App, Backbone, Marionette, $, _) {
    "use strict";

    var appName = 'targetApp';


    TargetApp.addInitializer(function () {
        var repo = new TargetApp.Repository();
        var layout = new TargetApp.TargetLayout();

        TargetApp.controller = new TargetApp.Controller({
            appName: appName,
            layout: layout,
            repo: repo
        });
    });

    TargetApp.addFinalizer(function () {
        if (TargetApp.controller) {
            TargetApp.controller.close();
            delete TargetApp.controller;
        }
    });

});