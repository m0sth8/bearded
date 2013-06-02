/* global Bearded */
/* global Marionette */
/* global Backbone */

Bearded.module("TargetApp", function (TargetApp, App, Backbone, Marionette, $, _) {
    "use strict";

    TargetApp.TargetView = Marionette.ItemView.extend({
        tagName: 'tr',
        ui: {
            progressbar: '#target-progressbar'
        },
        template: function (serialized_model) {
            return _.template($('#template-target-item').text(), serialized_model, {variable: 'target'});
        },
        onRender: function() {
            if (!this.model.get('infoRaw')){
//                var progressData = new Bearded.Progressbar.Item();
//                var progressView = new Bearded.Progressbar.View();
//                progressView.setElement(this.ui.progressbar);
//                progressView.render();
            }

        }
    });

    TargetApp.TargetListView = Marionette.CompositeView.extend({
        template: '#template-target-list',
        itemView: TargetApp.TargetView,
        itemViewContainer: 'tbody'
    });

    TargetApp.TargetLayout = Marionette.Layout.extend({
        template: '#template-target-layout',
        regions: {
            mainRegion: '#target-list-view',
            actionsRegion: '#target-actions'
        }
    });

    TargetApp.TargetActions = Marionette.ItemView.extend({
        template: '#template-target-actions',
        ui: {
            newTargetAction: '#new-target-action'
        },
        triggers: {
            'click #new-target-action': 'target:new'
        }
    });


    var NewTargetView = Marionette.ItemView.extend({
        template: '#template-target-new'

    });

    TargetApp.Controller = Bearded.AppController.extend({
        initialize: function (options) {
            this.repo = options.repo;
        },
        index: function () {
            Backbone.history.navigate('target/', {'trigger': true});
        },
        onShow: function () {
        },
        _showNewModal: function(targets) {
            var newForm = new NewTargetView();
            var modal = new Backbone.BootstrapModal({
                content: newForm,
                title: 'New target'
            });
            modal.on('ok', function(){
                var isValid = true;
                var $form = modal.$el.find('form');
                var $targetName = $form.find('input[name=targetName]');
                var $targetDomain = $form.find('input[name=targetDomain]');

                // cleaning
                $targetName.parents('.control-group').removeClass('error');
                $targetName.siblings('span.help-inline').text('');
                $targetDomain.parents('.control-group').removeClass('error');
                $targetDomain.siblings('span.help-inline').text('');

                var targetName = $targetName.val();
                var targetDomain = $targetDomain.val();

                // validation
                if (!targetName){
                    $targetName.parents('.control-group').addClass('error');
                    $targetName.siblings('span.help-inline').text('Should not be empty');
                    isValid = false;
                }
                if (!targetDomain){
                    $targetDomain.parents('.control-group').addClass('error');
                    $targetDomain.siblings('span.help-inline').text('Should not be empty');
                    isValid = false;
                }
                // check domain validation
                if (!isValid){
                    modal.preventClose();
                } else {
                    var target = new TargetApp.TargetItem({name: targetName, host: targetDomain});
                    targets.create(target, {wait: true, at: 1});
                }
            }, this);
            modal.open();
        },
        showTargets: function () {
            var targets = this.repo.getAll();
            var view = new TargetApp.TargetListView({
                    collection: targets
                });
            this.layout.mainRegion.show(view);
            var actions = new TargetApp.TargetActions();
            this.layout.actionsRegion.show(actions);
            this.listenTo(actions, 'target:new', function(){
                this._showNewModal(targets);
            }, this);
            Backbone.history.navigate('target/');
        }

    });


});