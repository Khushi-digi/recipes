# Generated by Django 3.1.7 on 2021-03-26 17:42

import cookbook.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cookbook', '0116_auto_20210319_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookmarkletImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', models.TextField()),
                ('url', models.CharField(blank=True, max_length=128, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookbook.space')),
            ],
            bases=(models.Model, cookbook.models.PermissionModelMixin),
        ),
    ]
