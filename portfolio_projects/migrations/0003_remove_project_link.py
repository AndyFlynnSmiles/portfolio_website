# Generated by Django 5.1.7 on 2025-03-21 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_projects', '0002_alter_project_description_alter_project_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
    ]
