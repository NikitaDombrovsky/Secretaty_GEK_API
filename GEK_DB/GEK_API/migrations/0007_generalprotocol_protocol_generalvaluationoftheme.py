# Generated by Django 4.0.3 on 2022-03-21 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GEK_API', '0006_meetinggek_participantlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralProtocol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuation_of_answer', models.CharField(blank=True, db_column='Valuation_Of_Answer', max_length=45, null=True)),
                ('valuation_of_report', models.CharField(blank=True, db_column='Valuation_Of_Report', max_length=45, null=True)),
                ('valuation_of_presentation', models.CharField(blank=True, db_column='Valuation_Of_Presentation', max_length=45, null=True)),
                ('valuation_of_portfolio', models.CharField(blank=True, db_column='Valuation_Of_Portfolio', max_length=45, null=True)),
                ('customer_feedback', models.CharField(blank=True, db_column='Customer_Feedback', max_length=45, null=True)),
                ('id_diploma_work', models.ForeignKey(db_column='ID_Diploma_Work', on_delete=django.db.models.deletion.CASCADE, to='GEK_API.diplomawork')),
            ],
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valuation_of_theme', models.CharField(blank=True, db_column='Valuation_Of_Theme', max_length=45, null=True)),
                ('id_meeting_gek', models.ForeignKey(db_column='ID_Meeting_GEK', on_delete=django.db.models.deletion.CASCADE, to='GEK_API.meetinggek')),
                ('id_member_gek', models.ForeignKey(db_column='ID_Member_GEK', on_delete=django.db.models.deletion.CASCADE, to='GEK_API.membergek')),
                ('id_theme_of_prorotocol', models.ForeignKey(db_column='ID_Theme_Of_Prorotocol', on_delete=django.db.models.deletion.CASCADE, to='GEK_API.themesofprorotocol')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralValuationOfTheme',
            fields=[
                ('id_general_valuation_of_theme', models.AutoField(db_column='ID_General_Valuation_Of_Theme', primary_key=True, serialize=False)),
                ('id_general_protocol', models.ForeignKey(db_column='ID_General_Protocol', on_delete=django.db.models.deletion.CASCADE, to='GEK_API.generalprotocol')),
                ('id_protocol', models.ForeignKey(db_column='ID_Protocol', on_delete=django.db.models.deletion.CASCADE, to='GEK_API.protocol')),
            ],
        ),
    ]
