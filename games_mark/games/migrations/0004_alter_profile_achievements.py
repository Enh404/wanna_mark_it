# Generated by Django 4.1.7 on 2023-03-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0001_initial'),
        ('games', '0003_alter_profile_achievements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='achievements',
            field=models.ManyToManyField(null=True, related_name='profiles', to='achievements.achievement'),
        ),
    ]
