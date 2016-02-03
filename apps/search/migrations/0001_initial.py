# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


# Auto created django migration for search initial model
# Adjust to your own DB such that search_text will support full text index
# Custom sql requires sqlparse (sudo pip install sqlparse)
"""
class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_name', models.CharField(max_length=255)),
                ('search_text', models.CharField(max_length=1024)),
                ('model_name', models.CharField(max_length=128)),
                ('object_pk', models.IntegerField()),
            ],
        ),
    ]
"""

# InnoDB supports full text from MySQL 5.7
MySQL_5_7 = """
CREATE TABLE `search_searchitems` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    `object_name` varchar(255) NOT NULL,
    `search_text` varchar(1024) NOT NULL,
    `model_name` varchar(128) NOT NULL,
    `object_pk` integer NOT NULL,
    FULLTEXT KEY `name_info_search` (`object_name`,`search_text`)
    ) DEFAULT CHARSET=utf8
"""

# Befor MySQL 5.7, full text only with MyISAM
MySQL_5_6 = """
CREATE TABLE `search_searchitems` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    `object_name` varchar(255) NOT NULL,
    `search_text` varchar(1024) NOT NULL,
    `model_name` varchar(128) NOT NULL,
    `object_pk` integer NOT NULL,
    FULLTEXT KEY `name_info_search` (`object_name`,`search_text`)
    ) ENGINE=MyISAM DEFAULT CHARSET=utf8
"""

mig_sql = MySQL_5_6

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(sql=mig_sql,
                          reverse_sql="`search_searchitems`"),
    ]