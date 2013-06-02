




/* global Bearded */
/* global Marionette */

Bearded.EmptyView = (function (App, Marionette) {
    "use strict";

    var EmptyView = Marionette.ItemView.extend({
      template: "#template-empty-view"
    });

    return EmptyView;
})(Bearded, Marionette);
