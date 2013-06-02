/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module("TemplateApp", function (TemplateApp, App, Backbone, Marionette, $, _) {
    "use strict";

    var appName = 'templateApp';

    TemplateApp.addInitializer(function (options) {
        var repo = new TemplateApp.Repository();
        var layout = new TemplateApp.TemplateLayout();

        TemplateApp.controller = new TemplateApp.Controller({
            appName: appName,
            repo: repo,
            layout: layout
        });
    });

    TemplateApp.addFinalizer(function () {
        if (TemplateApp.controller) {
            TemplateApp.controller.close();
            delete TemplateApp.controller;
        }
    });

});