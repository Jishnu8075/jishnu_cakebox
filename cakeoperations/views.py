from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,TemplateView,ListView,UpdateView,DeleteView,DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout


from cakeoperations.models import User,Cakes,Category,CakeVarients,Offer
from cakeoperations.forms import RegistrationForm,LoginForm,CakeCreateForm,CategoryCreateForm,CakeVarientForm,\
OfferCreateForm




# Create your views here.
class SignUpView(CreateView):
    template_name='cake/register.html'
    form_class=RegistrationForm
    model=User
    success_url=reverse_lazy('login.html')

    def form_valid(self, form):
        messages.success(self.request,'registration successfully')
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,'registration failed')
        return super().form_invalid(form)
    
class SignInView(FormView):
    template_name=('cake/login.html')
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login successfully")
                return redirect("index")
            else:
                messages.error(request,"invalid creadential")
                return render(request,self.template_name,{"form":form})
            
class IndexView(TemplateView):
    template_name='cake/index.html'

class CakeCreateView(CreateView):
    template_name='cake/cake_add.html'
    model=Cakes
    form_class=CakeCreateForm
    success_url=reverse_lazy('cake-add')

    def form_valid(self, form):
        messages.success(self.request,'cake added succesfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.errors(self.request,'failed')
        return super().form_invalid(form)
    
class CategoryCreateView(CreateView):
    template_name="cake/category_add.html"
    form_class=CategoryCreateForm
    model=Category
    context_object_name="categories"
    success_url=reverse_lazy("category-add")
    def form_valid(self,form):
        messages.success(self.request,"category added successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"category adding failed")
        return super().form_invalid(form)


class CakeListView(ListView):
    template_name="cake/cake_list.html"
    model=Cakes
    context_object_name="cakes"

class CakeUpdateView(UpdateView):
    template_name="cake/update.html"
    model=Cakes
    form_class=CakeCreateForm
    success_url=reverse_lazy("cake-list")

    def form_valid(self, form):
        messages.success(form,"updated successfully")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(form,"updation failed!!!")
        return super().form_invalid(form)
    
def remove_cakeview(request,*args,**kwargs):
    id=kwargs.get("pk")
    Cakes.objects.filter(id=id).delete()
    return redirect('cake-list')

class CakeDetailView(DetailView):
    template_name="cake/detail.html"
    model=Cakes
    context_object_name="cake"

class CakeVarientCreateView(CreateView):
    template_name="cake/cakevarient_add.html"
    form_class=CakeVarientForm
    model=CakeVarients
    success_url=reverse_lazy("cake-list")   

    def form_valid(self, form):
        id=self.kwargs.get("pk")
        obj=Cakes.objects.get(id=id)
        form.instance.cake=obj
        messages.success(self.request,"varient has been added")
        return super().form_valid(form)
    
class CakeVarientUpdateView(UpdateView):
    template_name='cake/cakevarient_update.html'
    form_class=CakeVarientForm
    model=CakeVarients
    success_url=reverse_lazy("cake-list")

    def form_valid(self,form):
        messages.success(self.request,"successfully updated")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,"updation failed")
        return super().form_invalid(form)
    

def remove_varient(request,*args,**kwargs):
    id=kwargs.get("pk")
    Cakes.objects.get(id=id).delete()
    return redirect('cake-list')

class OfferCreateView(CreateView):
    template_name="cake/offer.html"
    model=Offer
    form_class=OfferCreateForm
    success_url=reverse_lazy('cake-list')

    def form_valid(self,form):
        id=self.kwargs.get("pk")
        obj=CakeVarients.objects.get(id=id)  #error
        form.instance.cakevarient=obj
        messages.success(self.request,"offer has been added successfully")
        return super().form_valid(form)
    
def offer_delete_view(request,*args,**kwargs):
    id=kwargs.get('pk')
    offer_object=Offer.objects.get(id=id)
    cake_id=offer_object.cakevarient.cake.id  #error
    offer_object.delete()
    return redirect('cake-detail',pk=cake_id)

def sign_out_view(request,*args,**kwargs):
    logout(request)
    return redirect('signin')