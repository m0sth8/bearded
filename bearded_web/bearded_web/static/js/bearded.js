/* JSHint options */
/* global Backbone */
/* global Marionette */


var Bearded = (function(Backbone, Marionette){
    "use strict";

    var App = new Marionette.Application();
    App.addRegions({
        'menuRegion': "#dashboard-menu",
        'mainRegion': "#dashboard-main"
    });

    App.on("initialize:after", function(){
        csrfSetup(Backbone);
        if (Backbone.history){
            Backbone.history.start({pushState: true, root: '/dashboard/'});
        }
    });

//    App.startSubApp = function(appName, args){
//        var currentApp = App.module(appName);
//        if (App.currentApp === currentApp){ return; }
//
//        App.currentApp = currentApp;
//        currentApp.start(args);
//    };
    return App;

})(Backbone, Marionette);
