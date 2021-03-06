# Generated by Django 3.0.2 on 2020-03-04 01:44
import os

from django.db import migrations, models
from django.conf import settings


def join(*args):
    return os.path.abspath(os.path.join(*args))


def init_dirs(apps, schema_editor):
    Project = apps.get_model('recipes', 'Project')
    Data = apps.get_model('recipes', 'Data')

    projects = Project.objects.all()
    for prjn in projects:
        prjn.dir = join(settings.MEDIA_ROOT, "projects", f"{prjn.uid}")
        prjn.save()

    data = Data.objects.all()
    for datum in data:
        datum.dir = join(datum.project.dir, f"{datum.uid}")
        datum.toc = join(settings.TOC_ROOT, f"toc-{datum.uid}.txt")
        datum.save()


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_toml'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='dir',
            field=models.FilePathField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='data',
            name='toc',
            field=models.FilePathField(default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='project',
            name='dir',
            field=models.FilePathField(default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='analysis',
            name='security',
            field=models.IntegerField(choices=[(1, 'Trusted users'), (2, 'Admin only')], default=2),
        ),
        migrations.RunPython(init_dirs),
    ]
