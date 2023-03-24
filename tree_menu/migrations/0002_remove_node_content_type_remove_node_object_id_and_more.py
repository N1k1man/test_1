# Generated by Django 4.1.5 on 2023-01-03 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='node',
            name='object_id',
        ),
        migrations.AddField(
            model_name='node',
            name='parent_menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tree_menu.menu'),
        ),
        migrations.AddField(
            model_name='node',
            name='parent_node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tree_menu.node'),
        ),
    ]
