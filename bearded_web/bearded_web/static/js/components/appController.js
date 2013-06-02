// AppController
// --------------
//
// A base controller object to hide a lot of the
// guts and implementation detail of showing the
// lists and individual items

/* global Bearded */
/* global Marionette */

Bearded.AppController = (function (App, Marionette) {
    "use strict";

    var AppController = Marionette.Controller.extend({
        constructor: function (options) {
            this.appName = options.appName;
            this.layout = options.layout;
            this.layout.setElement(App.Dashboard.controller.getAppBody(this.appName));
            this.layout.render();
            Marionette.Controller.prototype.constructor.call(this, options);
            var that = this;
            App.vent.on('app:show', function(appName){ if (that.appName === appName){ that.show(); }});
        },

        // show this component in the app
        show: function () {
            Marionette.triggerMethod.call(this, "show");
            App.vent.trigger("app:showed", this.appName);
        },
        close: function() {
            Marionette.triggerMethod.call(this, "close");
            App.vent.off('app:show');
        }

    });

    return AppController;
})(Bearded, Marionette);
