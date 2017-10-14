# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('id2', '0015_auto_20171008_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonne',
            name='derniere_modif',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 14, 17, 0, 35, 487044, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abonne',
            name='inscription',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 14, 17, 0, 35, 487001, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visite',
            name='date_arrivee',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 14, 17, 0, 35, 485599, tzinfo=utc), verbose_name=b'Heure Arriv\xc3\xa9e', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='visiteprof',
            name='date_arrivee',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 14, 17, 0, 35, 486139, tzinfo=utc), verbose_name=b'Heure Arriv\xc3\xa9e', auto_now_add=True),
            preserve_default=True,
        ),
    ]
