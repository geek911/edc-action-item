# Generated by Django 2.0 on 2017-12-04 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edc_action_item', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalactionitem',
            old_name='parent_action',
            new_name='parent_action_item',
        ),
        migrations.RemoveField(
            model_name='actionitem',
            name='parent_action',
        ),
        migrations.AddField(
            model_name='actionitem',
            name='parent_action_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='edc_action_item.ActionItem'),
        ),
        migrations.AlterField(
            model_name='actionitem',
            name='parent_reference_identifier',
            field=models.CharField(help_text='e.g. tracking identifier from source model that opened the item.', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalactionitem',
            name='parent_reference_identifier',
            field=models.CharField(help_text='e.g. tracking identifier from source model that opened the item.', max_length=50, null=True),
        ),
    ]
