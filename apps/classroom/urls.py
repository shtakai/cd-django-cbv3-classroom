from django.conf.urls import url, include
from django.contrib import admin
from .views import StudentListView, StudentDetailView, TeacherListView, TeacherDetailView, SubjectListView, SubjectDetailView, SubjectTemplateView

urlpatterns = [
    url(r'^student/$', StudentListView.as_view()),
    url(r'^student/(?P<pk>\d+)/$', StudentDetailView.as_view()),
    url(r'^teacher/$', TeacherListView.as_view()),
    url(r'^teacher/(?P<pk>\d+)/$', TeacherDetailView.as_view()),
    url(r'^subject/$', SubjectTemplateView.as_view()),
    url(r'^subject/(?P<pk>\d+)/$', SubjectDetailView.as_view()),
    url(r'^admin/', admin.site.urls),
]
