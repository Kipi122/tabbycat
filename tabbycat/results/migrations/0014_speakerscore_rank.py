# Generated by Django 4.1.4 on 2022-12-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0013_teamscore_has_ghost'),
    ]

    operations = [
        migrations.AddField(
            model_name='speakerscore',
            name='rank',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='rank'),
        ),
    ]
