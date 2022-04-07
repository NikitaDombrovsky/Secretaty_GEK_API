from rest_framework import serializers

from .models import ProfessionalModule, Theme, Speciality, Group, Student, Teacher, DiplomaWork, PostMemberGek, MemberGek, ThemesOfProrotocol, MeetingGek, ParticipantList, Protocol, GeneralProtocol, GeneralValuationOfTheme, Users

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ProfessionalModuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProfessionalModule
        fields = ('id', 'index_professional_module', 'name_professional_module')


class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'name_theme', 'id_professional_module')


class SpecialitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speciality
        fields = ('id', 'name_speciality', 'code_speciality')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name_group', 'id_speciality')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'surname', 'name', 'patronymic', 'average_grade', 'id_group', 'date_of_birth')

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'surname', 'name', 'patronymic', 'date_of_birth')

class DiplomaWorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiplomaWork
        fields = ('id_diploma_work', 'id_student', 'id_teacher', 'id_themes')
class PostMemberGekSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostMemberGek
        fields = ('id', 'post_member_gek')

class MemberGekSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MemberGek
        fields = ('id', 'surname', 'name', 'patronymic', 'id_post_member_gek')

class ThemesOfProrotocolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThemesOfProrotocol
        fields = ('id', 'theme_of_prorotocol')

class MeetingGekSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MeetingGek
        fields = ('id', 'date_meetings_gek')

class ParticipantListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParticipantList
        fields = ('id_participants_list', 'id_meeting_gek', 'id_member_gek')


class ProtocolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Protocol
        fields = ('id', 'valuation_of_theme', 'id_meeting_gek', 'id_member_gek', 'id_theme_of_prorotocol')

class GeneralProtocolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneralProtocol
        fields = ('id', 'id_diploma_work', 'valuation_of_answer', 'valuation_of_report', 'valuation_of_presentation', 'valuation_of_portfolio', 'customer_feedback')

class GeneralValuationOfThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeneralValuationOfTheme
        fields = ('id_general_valuation_of_theme', 'id_general_protocol', 'id_protocol')
class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'surname', 'name', 'patronymic', 'password')

