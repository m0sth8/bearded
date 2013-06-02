/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module("PluginApp", function (PluginApp, App, Backbone, Marionette, $, _) {
    "use strict";

    PluginApp.Controller = Marionette.Controller.extend({
        initialize: function (options) {
            this.defaultToolPluginName = options.defaultToolPluginName || 'cl';
            this.repo = options.repo;
            this.toolPlugins = options.toolPlugins;
        },
        getToolPlugin: function(name) {
            var plugins = this.toolPlugins.where({name: name});
            if (!plugins.length){
                plugins = this.toolPlugins.where({name: this.defaultToolPluginName});
            }
            return plugins[0];
        }
    });

    PluginApp.addInitializer(function (options) {
        var repo = new PluginApp.Repository();
        var toolPlugins = new PluginApp.PluginCollection(options.toolPlugins);
        this.controller = new PluginApp.Controller({
            repo: repo,
            toolPlugins: toolPlugins
        });

    });

    PluginApp.addFinalizer(function () {
        if (PluginApp.controller) {
            PluginApp.controller.close();
            delete PluginApp.controller;
        }
    });

});