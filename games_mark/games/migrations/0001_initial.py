# Generated by Django 4.1.7 on 2023-03-08 11:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.PositiveSmallIntegerField()),
                ('category', models.ManyToManyField(related_name='games', to='games.category')),
            ],
        ),
        migrations.CreateModel(
            name='GameMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('mark', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата добавления')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gamemarks', to='games.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gamemarks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
