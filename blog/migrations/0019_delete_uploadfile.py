# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20141129_1539'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadFile',
        ),
    ]
