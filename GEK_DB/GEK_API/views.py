from django.shortcuts import render
# views.py
from rest_framework import viewsets

from .serializers import ProfessionalModuleSerializer, ThemeSerializer, SpecialitySerializer, GroupSerializer, StudentSerializer, TeacherSerializer, DiplomaWorkSerializer, PostMemberGekSerializer, MemberGekSerializer, ThemesOfProrotocolSerializer, MeetingGekSerializer, ParticipantListSerializer, ProtocolSerializer, GeneralProtocolSerializer, GeneralValuationOfThemeSerializer, UsersSerializer
from .models import ProfessionalModule, Theme, Speciality, Group, Student, Teacher, DiplomaWork, PostMemberGek, MemberGek, ThemesOfProrotocol, MeetingGek, ParticipantList, Protocol, GeneralProtocol, GeneralValuationOfTheme, Users

from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ProfessionalModuleSet(viewsets.ModelViewSet):
    queryset = ProfessionalModule.objects.all().order_by('index_professional_module')
    serializer_class = ProfessionalModuleSerializer


class ThemeSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all().order_by('name_theme')
    serializer_class = ThemeSerializer


class SpecialitySet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all().order_by('name_speciality')
    serializer_class = SpecialitySerializer


class GroupSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name_group')
    serializer_class = GroupSerializer


class StudentSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('surname')
    serializer_class = StudentSerializer

class TeacherSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('surname')
    serializer_class = TeacherSerializer

class DiplomaWorkSet(viewsets.ModelViewSet):
    queryset = DiplomaWork.objects.all().order_by('id_diploma_work')
    serializer_class = DiplomaWorkSerializer

class PostMemberGekSet(viewsets.ModelViewSet):
    queryset = PostMemberGek.objects.all().order_by('post_member_gek')
    serializer_class = PostMemberGekSerializer

class MemberGekSet(viewsets.ModelViewSet):
    queryset = MemberGek.objects.all().order_by('surname')
    serializer_class = MemberGekSerializer

class ThemesOfProrotocolSet(viewsets.ModelViewSet):
    queryset = ThemesOfProrotocol.objects.all().order_by('theme_of_prorotocol')
    serializer_class = ThemesOfProrotocolSerializer

class MeetingGekSet(viewsets.ModelViewSet):
    queryset = MeetingGek.objects.all().order_by('date_meetings_gek')
    serializer_class = MeetingGekSerializer

class ParticipantListSet(viewsets.ModelViewSet):
    queryset = ParticipantList.objects.all().order_by('id_participants_list')
    serializer_class = ParticipantListSerializer

class ProtocolSet(viewsets.ModelViewSet):
    queryset = Protocol.objects.all().order_by('valuation_of_theme')
    serializer_class = ProtocolSerializer

class GeneralProtocolSet(viewsets.ModelViewSet):
    queryset = GeneralProtocol.objects.all().order_by('valuation_of_answer') ### КОСТЫЛЬ
    serializer_class = GeneralProtocolSerializer

class GeneralValuationOfThemeSet(viewsets.ModelViewSet):
    queryset = GeneralValuationOfTheme.objects.all().order_by('id_general_valuation_of_theme')
    serializer_class = GeneralValuationOfThemeSerializer
class UsersSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('surname')
    serializer_class = UsersSerializer