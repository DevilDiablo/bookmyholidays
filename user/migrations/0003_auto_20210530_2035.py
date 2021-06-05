# Generated by Django 3.2 on 2021-05-30 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210530_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybookings',
            name='mhotle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.hotels'),
        ),
        migrations.AlterField(
            model_name='mybookings',
            name='mvehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.vehicle'),
        ),
    ]
