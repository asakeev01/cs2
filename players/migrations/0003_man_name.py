# Generated by Django 4.2.6 on 2023-10-16 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_alter_man_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='man',
            name='name',
            field=models.CharField(default='gerg', max_length=200),
            preserve_default=False,
        ),
    ]
