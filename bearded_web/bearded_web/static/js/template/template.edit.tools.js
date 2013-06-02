/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module("TemplateApp", function (TemplateApp, App, Backbone, Marionette, $, _) {
    "use strict";

    TemplateApp.ToolView = Marionette.ItemView.extend({
        tagName: 'li',
        template: '#template-tool-item',
        triggers: {
            'click button': 'tool-click'
        },
        onRender: function(){
//            this.$el.dragdrop({
//                makeClone: true
//                canDropClass: 'can-drop'
//                dropClass: 'flow-region'
//            });
        }
    });

    TemplateApp.ToolListView = Marionette.CompositeView.extend({
        template: '#template-tool-list',
        itemView: TemplateApp.ToolView,
        itemViewContainer: 'ul'
    });

    TemplateApp.ToolController = Marionette.Controller.extend({
        initialize: function(options){
            this.repo = options.repo;
            this.region = options.region;
        },
        show: function(){
            var _this = this;
            var tools = this.repo.getAll();
            var view = new TemplateApp.ToolListView({
                collection: tools
            });
            this.region.show(view);
            this.listenTo(view, 'itemview:tool-click', function(childView, msg){
                _this.trigger('tool-click', childView.model);
            });
        }

    });

});