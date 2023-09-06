from django.shortcuts import render, redirect
from django.views.generic import (View,TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from .models import School,Student
# from .forms import HotelForm
 
# Create your views here.
 

# def hotel_image_view(request):
 
#     if request.method == 'POST':
#         form = HotelForm(request.POST, request.FILES)
 
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = HotelForm()
#     return render(request, 'hotel_image_form.html', {'form': form})
 
 
# def success(request):
#     return HttpResponse('successfully uploaded')

# def display_hotel_images(request):
     
#     if request.method == 'GET':
 
#         # getting all the objects of hotel.
#         Hotels = Hotel.objects.all()
#         return render(request, 'display_hotel_images.html',
#                        {'hotel_images': Hotels})

# ---------------- Students related ---------------- #
class StudentCreateView(CreateView):
    model = Student #which model to inhrent from
    fields = ('name', 'age', 'School','profile_pic',) # which fields to create
    template_name = 'schDetails/student_form.html'
    
class StudentListView(ListView):
    model = Student
    template_name = 'schDetails/student_list.html'

class StudentDeleteView(DeleteView):
    model = Student
    success_url =  reverse_lazy('schDetails:listst')
    
class StudentUpdateView(UpdateView):
    model = Student #which model to link to
    fields = ('School', 'profile_pic',) # which fields to update

class StudentDetailView(DetailView):
    model = Student
    template_name = 'schDetails/student_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["st_details"] = self.get_object()
        return context


# ---------------- Schools related ---------------- #
class SchoolCreateView(CreateView):
    model = School #which model to inhrent from
    fields = ('name', 'principal', 'location') # which fields to create
    template_name = "schDetails/school_form.html" # link to the form tamplets
    
class SchoolUpdateView(UpdateView):
    model = School #which model to link to
    fields = ('name', 'principal',) # which fields to update

class SchoolDeleteView(DeleteView):
    model = School
    success_url =  reverse_lazy('schDetails:list')

class SchoolListView(ListView):
    model = School
    template_name = 'schDetails/school_list.html'
    contexe_object_name = 'school_list'
    
class SchoolDetailView(DetailView):
    model = School
    template_name = 'schDetails/school_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question"] = self.get_object()
        return context

class IndexView(TemplateView):
    """def index(request):
    return render(request , 'schDetails/index.html')
    """
    template_name = 'schDetails/index.html'

