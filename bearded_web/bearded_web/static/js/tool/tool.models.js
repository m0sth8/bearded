/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module("ToolApp", function (ToolApp, App, Backbone, Marionette, $) {
    "use strict";

    ToolApp.ToolItem = Backbone.Model.extend({

    });

    ToolApp.ToolCollection = Backbone.Collection.extend({
        url: '/api/v1/tool/',
        model: ToolApp.ToolItem
    });

    ToolApp.Repository = Marionette.Controller.extend({
        getAll: function () {
            var collection = new ToolApp.ToolCollection();
            collection.fetch();
            return collection;
        }
    });

});