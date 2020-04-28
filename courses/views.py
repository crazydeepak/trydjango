from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import Course
from .forms import CourseModelForm
from django.views.generic import(CreateView,DetailView,ListView,UpdateView,DeleteView)

# Create your views here.
class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj 


class CourseView(CourseObjectMixin,View):
    template_name = "courses/course_detail.html"
    def get(self,request,id=None,*args,**kwargs):
        context={'object':self.get_object()}
        #if id is not None:
            #obj=get_object_or_404(Course,id= id)
            # context['object']=obj
            # print(context)
        return render(request,self.template_name,context)   

class CourseCreateView(View):
    template_name = "courses/course_create.html" # DetailView
    def get(self, request, *args, **kwargs):
        # GET method
        form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = "courses/course_list.html"
    queryset= Course.objects.all()
    
    def get_queryset(self):
        return self.queryset
    
    def get(self,request,*args,**kwargs):
        # context={'object_list':self.query_set}
        context={'object_list':self.get_queryset()}
        return render(request,self.template_name,context)

# class MyListView(CourseListView):
#     query_set1=Course.objects.filter(id=1)

class CourseUpdateView(CourseObjectMixin,View):
    template_name = "courses/course_update.html" # DetailView
    # def get_object(self):
    #     id = self.kwargs.get('id')
    #     obj = None
    #     if id is not None:
    #         obj = get_object_or_404(Course, id=id)
    #     return obj

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

# class CourseUpdateView(UpdateView):
#     template_name = "courses/course_update.html"
#     form_class = CourseModelForm
#     #queryset = Article.objects.all()
    
#     def get_object(self,**kwargs):
#         print(self.kwargs)
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Course, id=id_)

#     def form_valid(self,form):
#         print(form.cleaned_data)
#         return super().form_valid(form)

class CourseDeleteView(CourseObjectMixin,View):
    template_name = "courses/course_delete.html" # DetailView
    # def get_object(self):
    #     id = self.kwargs.get('id')
    #     obj = None
    #     if id is not None:
    #         obj = get_object_or_404(Course, id=id)
    #     return obj

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('../../')
        return render(request, self.template_name, context)

def my_fbv(request,*args,**kwargs):
    return render(request,"about.html",{})    