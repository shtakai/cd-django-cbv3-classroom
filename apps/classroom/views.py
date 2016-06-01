from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Teacher, Student, Subject


class StudentListView(ListView):
    model = Student
    template_name = 'classroom/student_list.html'

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        print('context', context)
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = 'classroom/student_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        print('context', context)
        return context


class TeacherListView(ListView):
    model = Teacher
    template_name = 'classroom/teacher_list.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherListView, self).get_context_data(**kwargs)
        print('context', context)
        return context


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'classroom/teacher_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TeacherDetailView, self).get_context_data(**kwargs)
        print('context', context)
        return context


class SubjectListView(ListView):
    model = Subject
    template_name = 'classroom/subject_list.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectListView, self).get_context_data(**kwargs)
        print('context', context)
        return context


class SubjectTemplateView(TemplateView):
    template_name = 'classroom/subject_template.html'

    def get_context_data(self, **kwargs):
        subjects = Subject.objects.all()
        context = { 'subjects': subjects }
        print('context', context)
        return context


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'classroom/subject_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectDetailView, self).get_context_data(**kwargs)
        print('context', context)
        return context


