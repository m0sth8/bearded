/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module("TemplateApp", function (TemplateApp, App, Backbone, Marionette, $) {
    "use strict";

    TemplateApp.TemplateItem = Backbone.RelationalModel.extend({
        relations: [
            {
                type: Backbone.HasOne,
                key: 'plugin',
                relatedModel: 'PluginItem',
                collectionType: 'PluginCollection'
//                autoFetch: true
////            reverseRelation: {
////                key: 'livesIn'
////                includeInJSON: 'id'
//                // 'relatedModel' is automatically set to 'Zoo'; the 'relationType' to 'HasOne'.
//            }
            },
            {
                type: Backbone.HasMany,
                key: 'sequence',
                relatedModel: 'TemplateItem',
                collectionType: 'TemplateCollection',
//                autoFetch: true,
                reverseRelation: {
                    key: 'livesIn',
                    includeInJSON: 'id'
                }
            }

        ]
    });

    TemplateApp.TemplateCollection = Backbone.Collection.extend({
        url: '/api/v1/template/',
        model: TemplateApp.TemplateItem
    });

    Backbone.Relational.store.addModelScope(TemplateApp);

    TemplateApp.Repository = Marionette.Controller.extend({
        getRoot: function(){
            var collection = new TemplateApp.TemplateCollection();
            collection.fetch({data: {is_root: true}});
            return collection;
        },

        getNewTemplate: function(){
            var template = new TemplateApp.TemplateItem({});
            return template;
        }
    });

});