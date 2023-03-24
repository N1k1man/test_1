# Generated by Django 4.1.5 on 2023-01-03 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0002_remove_node_content_type_remove_node_object_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='parent_menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tree_menu.menu'),
        ),
        migrations.AlterField(
            model_name='node',
            name='parent_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tree_menu.node'),
        ),
    ]
