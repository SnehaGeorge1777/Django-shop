# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-10 20:52
from __future__ import unicode_literals

from django.db import migrations

def forwards(apps, schema_editor):
    Page = apps.get_model('cms', 'Page')
    for page in Page.objects.filter(application_urls='ProductsListApp'):
        page.application_urls = 'CatalogListApp'
        page.save()


def backwards(apps, schema_editor):
    Page = apps.get_model('cms', 'Page')
    for page in Page.objects.filter(application_urls='CatalogListApp'):
        page.application_urls = 'ProductsListApp'
        page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_unify_address'),
    ]
    operations = [
        migrations.RunPython(forwards, reverse_code=backwards)
    ]
