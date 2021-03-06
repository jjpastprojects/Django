// Generated by CoffeeScript 1.4.0
(function() {
  var __indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  window.Field = Backbone.Model.extend({
    defaults: {
      min: 'N/A',
      max: "N/A",
      mean: "N/A",
      top: "N/A",
      freq: "N/A",
      unique: "N/A",
      std: "N/A"
    },
    initialize: function() {
      if (this.attributes.uniques != null) {
        return this.set('unique', this.attributes.uniques.length);
      }
    },
    isCategorical: function() {
      return __indexOf.call(this.attributes.tags, "categorical") >= 0;
    },
    isMostlyNull: function() {
      return __indexOf.call(this.attributes.tags, "mostly null") >= 0;
    },
    isContinuous: function() {
      return __indexOf.call(this.attributes.tags, "open ended") >= 0;
    },
    isUnique: function() {
      return __indexOf.call(this.attributes.tags, "unique") >= 0;
    },
    isRarelyNull: function() {
      return __indexOf.call(this.attributes.tags, "not null") >= 0;
    },
    isBoolean: function() {
      return __indexOf.call(this.attributes.tags, "boolean") >= 0;
    },
    isTernary: function() {
      return (__indexOf.call(this.attributes.tags, "boolean") >= 0) && (__indexOf.call(this.attributes.tags, "null") >= 0);
    },
    segment: function(classes) {
      var i, k, max, min, step, y, _i, _j, _ref, _results, _results1;
      if (this.isContinuous()) {
        max = this.attributes.max;
        min = this.attributes.min;
        step = (max - min) / classes;
        _results = [];
        for (y = _i = min; min <= max ? _i <= max : _i >= max; y = _i += step) {
          _results.push(y);
        }
        return _results;
      } else if (this.isCategorical()) {
        k = Math.round(this.attributes.uniques.length / classes);
        _results1 = [];
        for (i = _j = 0, _ref = this.attributes.uniques.length; 0 <= _ref ? _j <= _ref : _j >= _ref; i = _j += k) {
          _results1.push(this.attributes.uniques[i]);
        }
        return _results1;
      } else {
        return [];
      }
    }
  });

  window.Schema = Backbone.Collection.extend({
    model: Field
  });

  window.AttributeCharacteristicsItemView = Backbone.Marionette.ItemView.extend({
    template: "#tpl-attribute-characteristics",
    tagName: 'tr'
  });

  window.AttributeReportView = Backbone.Marionette.CompositeView.extend({
    template: "#tpl-attribute-report",
    itemView: AttributeCharacteristicsItemView,
    collection: window.schema,
    itemViewContainer: "tbody",
    tagName: "table",
    className: "table table-striped"
  });

  window.schema = new Schema(window.attributes);

}).call(this);
