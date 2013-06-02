/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module("TemplateApp", function (TemplateApp, App, Backbone, Marionette, $, _) {
    "use strict";

    TemplateApp.TemplateView = Marionette.ItemView.extend({
        tagName: 'tr',
        template: function (serialized_model) {
            return _.template($('#template-template-item').text(), serialized_model, {variable: 'template'});
        }
    });

    TemplateApp.TemplateListView = Marionette.CompositeView.extend({
        template: '#template-template-list',
        itemView: TemplateApp.TemplateView,
        itemViewContainer: 'tbody'
    });

    TemplateApp.TemplateLayout = Marionette.Layout.extend({
        template: '#template-template-layout',
        regions: {
            mainRegion: '#template-list-view',
            actionsRegion: '#template-actions'
        }
    });

    TemplateApp.TemplateActions = Marionette.ItemView.extend({
        template: '#template-template-actions',
        ui: {
            newTemplateAction: '#new-template-action'
        },
        triggers: {
            'click #new-template-action': 'template:new'
        }
    });

    TemplateApp.Controller = Bearded.AppController.extend({
        initialize: function (options) {
            this.repo = options.repo;
        },
        onShow: function () {
        },
        showTemplates: function () {
            var templates = this.repo.getRoot();
            var view = new TemplateApp.TemplateListView({
                    collection: templates
                });
            this.layout.mainRegion.show(view);
            var actions = new TemplateApp.TemplateActions();
            this.layout.actionsRegion.show(actions);
            this.listenTo(actions, 'template:new', function(){
                Backbone.history.navigate('template/new/', {trigger: true});
            });

            Backbone.history.navigate('template/');
        },
        newTemplate: function() {
            var template = this.repo.getNewTemplate();
            this.layout.actionsRegion.close();
            var editTemplateController = new TemplateApp.EditController({
                template: template,
                mainRegion: this.layout.mainRegion
            });
            editTemplateController.show();
        }

    });



});