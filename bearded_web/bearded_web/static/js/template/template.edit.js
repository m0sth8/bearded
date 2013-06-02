/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module('TemplateApp', function(TemplateApp, App, Backbone, Marionette) {
    'use strict';

    var ToolApp = App.module('ToolApp');
    var PluginApp = App.module('PluginApp');

    var TemplateLayout = Marionette.Layout.extend({
        template: '#template-template-edit-layout',
        regions: {
            flowRegion: '#flow-region',
            elementsRegion: '#elements-region'
        }
    });

    var ElementsLayout = Marionette.Layout.extend({
        template: '#template-elements-layout',
        regions: {
            toolRegion: '#tools'
        }
    });


    TemplateApp.EditController = Marionette.Controller.extend({

        initialize: function(options) {
            this.rootTemplate = options.template;
            this.mainRegion = options.mainRegion;
            this.layout = new TemplateLayout();
        },

        showFlow: function(region) {
            this.flowController = new TemplateApp.FlowController({
                rootTemplate: this.rootTemplate,
                region: region
            });
            this.flowController.show();
        },

        show: function() {
            var elementsLayout = new ElementsLayout();
            this.mainRegion.show(this.layout);

            this.showFlow(this.layout.flowRegion);

            this.layout.elementsRegion.show(elementsLayout);
            this.showTools(elementsLayout.toolRegion);

        },
        showTools: function(region) {
            this.toolController = new TemplateApp.ToolController({
                repo: new ToolApp.Repository(),
                region: region
            });
            this.toolController.show();
            var _this = this;
            this.toolController.listenTo(this.toolController, 'tool-click', function(model){
                _this.flowController.addTool(model);
            });
        },

        onClose: function() {
            this.flowController.close();
            this.toolController.close();

        }
    });


});