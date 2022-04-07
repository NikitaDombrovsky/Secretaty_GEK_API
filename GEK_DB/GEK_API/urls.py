# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'PM', views.ProfessionalModuleSet)
router.register(r'Themes', views.ThemeSet)
router.register(r'Speciality', views.SpecialitySet)
router.register(r'Group', views.GroupSet)
router.register(r'Student', views.StudentSet)
router.register(r'Teacher', views.TeacherSet)
router.register(r'DiplomaWork', views.DiplomaWorkSet)
router.register(r'PostMemberGek', views.PostMemberGekSet)
router.register(r'MemberGek', views.MemberGekSet)
router.register(r'ThemesOfProrotocol', views.ThemesOfProrotocolSet)
router.register(r'MeetingGek', views.MeetingGekSet)
router.register(r'ParticipantList', views.ParticipantListSet)
router.register(r'Protocol', views.ProtocolSet)
router.register(r'GeneralProtocol', views.GeneralProtocolSet)
router.register(r'GeneralValuationOfTheme', views.GeneralValuationOfThemeSet)
router.register(r'Users', views.UsersSet)
# router.register(r'users', views.UserList)
# router.register(r'users/<int:pk>/', views.UserDetail)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('users/', views.UserList.as_view()),
    #path('users/<int:pk>/', views.UserDetail.as_view()),

]


# urlpatterns = format_suffix_patterns(urlpatterns)