# Generated by Django 4.0.3 on 2022-03-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GEK_API', '0004_postmembergek_membergek'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemesOfProrotocol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_of_prorotocol', models.CharField(blank=True, db_column='Theme_Of_Prorotocol', max_length=45, null=True)),
            ],
        ),
    ]
