/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module("PluginApp", function (PluginApp, App, Backbone, Marionette, $, _) {
    "use strict";

    PluginApp.PluginItem = Backbone.RelationalModel.extend({
        TYPE: {
            SEQUENCE: 1,
            TOOL: 3,
            COMPOSITE: 5
        },
        isTool: function(){
            return this.get('type') === this.TYPE.TOOL;
        },
        isSequence: function(){
            return this.get('type') === this.TYPE.SEQUENCE;
        }
    });


    PluginApp.PluginCollection = Backbone.Collection.extend({
        url: '/api/v1/plugin/',
        model: PluginApp.PluginItem
    });

    Backbone.Relational.store.addModelScope(PluginApp);

    PluginApp.Repository = Marionette.Controller.extend({
        getAll: function () {
            var collection = new PluginApp.PluginCollection();
            collection.fetch();
            return collection;
        }
    });

});