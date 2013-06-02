// Application Selector
// --------------------
//
// Display the list of applications to choose from
// and move to that application when the selection is changed

/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module("Dashboard", function (Dashboard, App, Backbone, Marionette) {
    "use strict";


    var DashboardMenuItem = Backbone.Model.extend({
        defaults: {
            active: false
        },
        getUrl: function(){
            return this.get('url').replace(Backbone.history.root, '');
        }
    });

    var DashboardMenuCollection = Backbone.Collection.extend({
        model: DashboardMenuItem
    });


    var DashboardItemView = Marionette.ItemView.extend({
        template: '#template-dashboard-item',
        model: DashboardMenuItem,
        initialize: function () {
            this._setActive();
            this.listenTo(this.model, "change:active", this._setActive);
        },
        _setActive: function () {
            this.$el.toggle(this.model.get('active'));
        }
    });

    var DashboardListView = Marionette.CollectionView.extend({
        itemView: DashboardItemView
    });

    var DashboardMenuItemView = Marionette.ItemView.extend({
        tagName: 'li',
        template: '#template-dashboard-menu-item',
        model: DashboardMenuItem,
        events: {
            "click a": 'menu_click'
        },

        menu_click: function (e) {
            e.preventDefault();
            Backbone.history.navigate(this.model.getUrl(), {trigger: true});
//            App.vent.trigger('app:show', this.model.get('appName'));
        },
        initialize: function () {
            this.listenTo(this.model, "change:active", this._setActive);
        },
        _setActive: function () {
            this.$el.toggleClass('active', this.model.get('active'));
        }

    });

    var DashboardMenuView = Marionette.CollectionView.extend({
        tagName: 'ul',
        className: 'nav',
        itemView: DashboardMenuItemView,
        itemViewEventPrefix: 'dashboard:menu'
    });

    var DashboardController = Marionette.Controller.extend({
        initialize: function (options) {
            this.menuView = options.menuView;
            this.listView = options.listView;
            this.collection = this.menuView.collection;
            App.vent.on("app:showed", this.setApp, this);
        },
        onClose: function(){
            App.vent.off("app:showed", this.setApp, this);
        },
        setApp: function (appName) {
            this.collection.each(function (item) {
                if (item.get('appName') === appName) {
                    if (!item.get('active')) {
                        item.set('active', true);
                    }
                } else {
                    if (item.get('active')) {
                        item.set('active', false);
                    }
                }
            });
        },
        getAppBody: function(appName) {
            var itemView = this.listView.children.find(function (itemView) {
                if (itemView.model.get('appName') === appName) {
                    return true;
                }
            });
            if (itemView) {
                return itemView.$el;
            }else{
                return null;
            }

        }


    });

    Dashboard.addInitializer(function (options) {
        var menuCollection = new DashboardMenuCollection(options.dashboard);
        var menuView = new DashboardMenuView({collection: menuCollection});
        var listView = new DashboardListView({collection: menuCollection});
        App.menuRegion.show(menuView);
        App.mainRegion.show(listView);
        Dashboard.controller = new DashboardController({"menuView": menuView, "listView": listView});
    });

});