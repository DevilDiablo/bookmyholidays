# Generated by Django 3.2 on 2021-06-10 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210610_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='pak',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.package'),
        ),
    ]
