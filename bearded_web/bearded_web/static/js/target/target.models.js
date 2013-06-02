/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module("TargetApp", function (TargetApp, App, Backbone, Marionette, $, _) {
    "use strict";

    TargetApp.TargetItem = Backbone.Model.extend();

    TargetApp.TargetCollection = Backbone.Collection.extend({
        url: '/api/v1/target/',
        model: TargetApp.TargetItem
    });

    TargetApp.Repository = Marionette.Controller.extend({
        getAll: function () {
            var collection = new TargetApp.TargetCollection();
            collection.fetch();
            return collection;
        }
    });

});