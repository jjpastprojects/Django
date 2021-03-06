# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Application.left_sidebar_html'
        db.add_column(u'ga_applications_application', 'left_sidebar_html',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.right_sidebar_html'
        db.add_column(u'ga_applications_application', 'right_sidebar_html',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.left_sidebar_columns'
        db.add_column(u'ga_applications_application', 'left_sidebar_columns',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Application.right_sidebar_columns'
        db.add_column(u'ga_applications_application', 'right_sidebar_columns',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Application.header_html'
        db.add_column(u'ga_applications_application', 'header_html',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Application.footer_html'
        db.add_column(u'ga_applications_application', 'footer_html',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Application.left_sidebar_html'
        db.delete_column(u'ga_applications_application', 'left_sidebar_html')

        # Deleting field 'Application.right_sidebar_html'
        db.delete_column(u'ga_applications_application', 'right_sidebar_html')

        # Deleting field 'Application.left_sidebar_columns'
        db.delete_column(u'ga_applications_application', 'left_sidebar_columns')

        # Deleting field 'Application.right_sidebar_columns'
        db.delete_column(u'ga_applications_application', 'right_sidebar_columns')

        # Deleting field 'Application.header_html'
        db.delete_column(u'ga_applications_application', 'header_html')

        # Deleting field 'Application.footer_html'
        db.delete_column(u'ga_applications_application', 'footer_html')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ga_applications.application': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Application', '_ormbases': [u'pages.Page']},
            'application_css': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'application_script': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'default_base_map': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'default_includes': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'footer_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'header_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'left_sidebar_columns': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'left_sidebar_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'link_tags': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'renderedlayers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ga_resources.RenderedLayer']", 'symmetrical': 'False', 'through': u"orm['ga_applications.ApplicationLayer']", 'blank': 'True'}),
            'right_sidebar_columns': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'right_sidebar_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'script_tags': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'ga_applications.applicationlayer': {
            'Meta': {'ordering': "('-weight',)", 'object_name': 'ApplicationLayer'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ga_applications.Application']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'renderedlayer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ga_resources.RenderedLayer']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ga_resources.dataresource': {
            'Meta': {'ordering': "['title']", 'object_name': 'DataResource', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'driver': ('django.db.models.fields.CharField', [], {'default': "'ga_resources.drivers.shapefile'", 'max_length': '255'}),
            'last_change': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_refresh': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'md5sum': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'metadata_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'metadata_xml': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'next_refresh': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'refresh_every': ('timedelta.fields.TimedeltaField', [], {'null': 'True', 'blank': 'True'}),
            'resource_config': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resource_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'resource_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'spatial_metadata': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ga_resources.SpatialMetadata']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'ga_resources.renderedlayer': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'RenderedLayer', '_ormbases': [u'pages.Page']},
            'cache_seconds': ('django.db.models.fields.PositiveIntegerField', [], {'default': '60'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'data_resource': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ga_resources.DataResource']"}),
            'default_style': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'default_for_layer'", 'to': u"orm['ga_resources.Style']"}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'styles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ga_resources.Style']", 'symmetrical': 'False'})
        },
        u'ga_resources.spatialmetadata': {
            'Meta': {'object_name': 'SpatialMetadata'},
            'bounding_box': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'native_bounding_box': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True'}),
            'native_srs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'three_d': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'ga_resources.style': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Style', '_ormbases': [u'pages.Page']},
            'legend': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'legend_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'legend_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'stylesheet': ('django.db.models.fields.TextField', [], {})
        },
        u'generic.assignedkeyword': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'AssignedKeyword'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignments'", 'to': u"orm['generic.Keyword']"}),
            'object_pk': ('django.db.models.fields.IntegerField', [], {})
        },
        u'generic.keyword': {
            'Meta': {'object_name': 'Keyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'pages.page': {
            'Meta': {'ordering': "('titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "'object_pk'", 'to': u"orm['generic.AssignedKeyword']", 'frozen_by_south': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['ga_applications']