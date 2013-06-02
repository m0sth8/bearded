/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module("Progressbar", function (Progressbar, App, Backbone, Marionette) {
    "use strict";

    Progressbar.Item = Backbone.Model.extend({

    });

    Progressbar.View = Marionette.ItemView.extend({
        template: "#template-progressbar"
    });

});