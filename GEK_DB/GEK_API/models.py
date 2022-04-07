from django.db import models

# cd GEK_DB
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# python manage.py createsuperuser # я забыл пароль админа лол
# Test1 #12345678Test
class Users(models.Model):
    surname = models.CharField(db_column='Surname', max_length=60, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)
    patronymic = models.CharField(db_column='Patronymic', max_length=60, blank=True,
                                  null=True)
    password = models.FloatField(db_column='Password', blank=True, null=True)
    def __str__(self):
        return self.surname
############################################################################
# Модули и Темы
############################################################################
class ProfessionalModule(models.Model):
    index_professional_module = models.CharField(db_column='Индекс_ПМ', max_length=60, blank=True, null=True)
    name_professional_module = models.CharField(db_column='Название_ПМ', max_length=60, blank=True, null=True)

    def __str__(self):
        return self.index_professional_module # День костылей

class Theme(models.Model):
    name_theme = models.CharField(db_column='Название_Темы', max_length=45, blank=True, null=True)
    id_professional_module = models.ForeignKey('ProfessionalModule', related_name='ID_ПМ', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_theme
############################################################################
# Специальности, Группы и Студенты
############################################################################
class Speciality(models.Model):
    name_speciality = models.CharField(db_column='Name_Speciality', max_length=60, blank=True, null=True)
    code_speciality = models.CharField(db_column='Code_Speciality', max_length=60, blank=True, null=True)

    def __str__(self):
        return self.name_speciality
class Group(models.Model):
    name_group = models.CharField(db_column='Name_Group', max_length=60, blank=True, null=True)
    id_speciality = models.ForeignKey('Speciality', db_column='ID_Speciality', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_group
class Student(models.Model):
    surname = models.CharField(db_column='Surname', max_length=60, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=60, blank=True, null=True)
    patronymic = models.CharField(db_column='Patronymic', max_length=60, blank=True, null=True)
    average_grade = models.FloatField(db_column='Average_grade', blank=True, null=True)
    id_group = models.ForeignKey('Group', db_column='ID_Group', on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField(db_column='Date_Of_Birth', blank=True, null=True)

    def __str__(self):
        return self.surname
############################################################################
# Преподаватели
############################################################################
class Teacher(models.Model):
    surname = models.CharField(db_column='Surname', max_length=45, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)
    patronymic = models.CharField(db_column='Patronymic', max_length=45, blank=True, null=True)
    date_of_birth = models.DateTimeField(db_column='Date_Of_Birth', blank=True, null=True)

    def __str__(self):
        return self.surname
############################################################################
# Дипломные работы
############################################################################
class DiplomaWork(models.Model):
    id_diploma_work = models.AutoField(db_column='ID_Diploma_Work', primary_key=True)
    id_student = models.ForeignKey('Student', db_column='ID_Student', on_delete=models.CASCADE)
    id_teacher = models.ForeignKey('Teacher', db_column='ID_Teacher', on_delete=models.CASCADE)
    id_themes = models.ForeignKey('Theme', db_column='ID_Themes', on_delete=models.CASCADE)

    def __str__(self):
        return self.id_diploma_work
############################################################################
# Должности Членов ГЭК и Члены ГЭК
############################################################################
class PostMemberGek(models.Model):
    post_member_gek = models.CharField(db_column='Post_Member_GEK', max_length=45, blank=True, null=True)

    def __str__(self):
        return self.post_member_gek
class MemberGek(models.Model):
    surname = models.CharField(db_column='Surname', max_length=45, blank=True, null=True)
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)
    patronymic = models.CharField(db_column='Patronymic', max_length=45, blank=True, null=True)
    id_post_member_gek = models.ForeignKey('PostMemberGek', db_column='ID_Post_Member_GEK', on_delete=models.CASCADE)

    def __str__(self):
        return self.surname
############################################################################
# Темы протоколов
############################################################################
class ThemesOfProrotocol(models.Model):
    theme_of_prorotocol = models.CharField(db_column='Theme_Of_Prorotocol', max_length=45, blank=True, null=True)

    def __str__(self):
        return self.theme_of_prorotocol
############################################################################
# Заседание ГЭК и Список участников
############################################################################
class MeetingGek(models.Model):
    date_meetings_gek = models.DateTimeField(db_column='Date_Meetings_GEK', blank=True, null=True)

    def __str__(self):
        return self.date_meetings_gek


class ParticipantList(models.Model):
    id_participants_list = models.AutoField(db_column='ID_participant_list', primary_key=True)
    id_meeting_gek = models.ForeignKey('MeetingGek', models.DO_NOTHING, db_column='ID_Meeting_GEK', blank=True, null=True)
    id_member_gek = models.ForeignKey('MemberGek', models.DO_NOTHING, db_column='ID_Member_GEK', blank=True, null=True)

    def __str__(self):
        return self.id_participants_list
############################################################################
# Протоколы, Общие протоколы и Общая оценка
############################################################################
class Protocol(models.Model):
    valuation_of_theme = models.CharField(db_column='Valuation_Of_Theme', max_length=45, blank=True, null=True)
    id_meeting_gek = models.ForeignKey('MeetingGek', db_column='ID_Meeting_GEK', on_delete=models.CASCADE)
    id_member_gek = models.ForeignKey('MemberGek', db_column='ID_Member_GEK', on_delete=models.CASCADE)
    id_theme_of_prorotocol = models.ForeignKey('ThemesOfProrotocol', db_column='ID_Theme_Of_Prorotocol', on_delete=models.CASCADE)

    def __str__(self):
        return self.valuation_of_theme



class GeneralProtocol(models.Model):
    id_diploma_work = models.ForeignKey('DiplomaWork', db_column='ID_Diploma_Work', on_delete=models.CASCADE)
    valuation_of_answer = models.CharField(db_column='Valuation_Of_Answer', max_length=45, blank=True, null=True)
    valuation_of_report = models.CharField(db_column='Valuation_Of_Report', max_length=45, blank=True, null=True)
    valuation_of_presentation = models.CharField(db_column='Valuation_Of_Presentation', max_length=45, blank=True, null=True)
    valuation_of_portfolio = models.CharField(db_column='Valuation_Of_Portfolio', max_length=45, blank=True, null=True)
    customer_feedback = models.CharField(db_column='Customer_Feedback', max_length=45, blank=True, null=True)

    def __str__(self):
        return self.valuation_of_answer # КОСТЫЛЬ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class GeneralValuationOfTheme(models.Model):
    id_general_valuation_of_theme = models.AutoField(db_column='ID_General_Valuation_Of_Theme', primary_key=True)
    id_general_protocol = models.ForeignKey('GeneralProtocol', db_column='ID_General_Protocol', on_delete=models.CASCADE)
    id_protocol = models.ForeignKey('Protocol', db_column='ID_Protocol', on_delete=models.CASCADE)
    def __str__(self):
        return self.id_general_valuation_of_theme

