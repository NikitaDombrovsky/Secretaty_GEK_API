# Generated by Django 4.0.3 on 2022-03-21 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GEK_API', '0003_teacher_diplomawork'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostMemberGek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_member_gek', models.CharField(blank=True, db_column='Post_Member_GEK', max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberGek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(blank=True, db_column='Surname', max_length=45, null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=45, null=True)),
                ('patronymic', models.CharField(blank=True, db_column='Patronymic', max_length=45, null=True)),
                ('id_post_member_gek', models.ForeignKey(db_column='ID_Post_Member_GEK', on_delete=django.db.models.deletion.CASCADE, to='GEK_API.postmembergek')),
            ],
        ),
    ]
