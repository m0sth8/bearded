/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module('TemplateApp', function(TemplateApp, App, Backbone, Marionette, $, _) {
    'use strict';

    var ToolApp = App.module('ToolApp');
    var PluginApp = App.module('PluginApp');

    var ToolSettingsView = Marionette.ItemView.extend({
        template: '#template-tool-settings',
        initialize: function(){

        }

    });

    var FlowItemView = Marionette.ItemView.extend({
        tagName: 'li',
        template: '#template-flow-item',
        events: {
            'click button': 'showModal'
        },
        showModal: function(){
            var view = new ToolSettingsView();
            var modal = new Backbone.BootstrapModal({content: view}).open();
        }
    });


    var FlowLayout = Marionette.Layout.extend({
        template: '#template-flow-layout',
        regions: {
            serialRegion: '.serial-region'
//            dropRegion: '.drop-region'
        }
    });

    var FlowSerialView = Marionette.CollectionView.extend({
        tagName: 'ul',
        itemView: FlowItemView,
        initialize: function(){

        }
    });



    TemplateApp.FlowController = Marionette.Controller.extend({
        initialize: function(options) {
            this.region = options.region;
            this.rootTemplate = options.rootTemplate;
            this.templates = new TemplateApp.TemplateCollection();
//            this.tools = new ToolApp.ToolCollection();
        },
        show: function() {
            var flowLayout =  new FlowLayout();
            var flowSerial = new FlowSerialView({collection: this.templates});
            this.region.show(flowLayout);
            flowLayout.serialRegion.show(flowSerial);
        },
        addTool: function(tool){
            var plugin = PluginApp.controller.getToolPlugin(tool.name);
            var template = new TemplateApp.TemplateItem({
                plugin: plugin
            });
            console.log(template.toJSON());
            this.templates.add(template);
//            this.plugins.add(tool);
        }
    });

});