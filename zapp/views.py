from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Company, Customer_Assistant
from .forms import CompanyAddForm, UserEditForm, CustomerAssistEditForm, UserRegistrationForm, CompanyEditForm

@login_required
def start(request):
    return render(request,'zapp/start.html',{'customer_assistant':request.user.customer_assistant})

@login_required
def companies(request):
    if request.user.username == 'admin':
        companies_list = Company.objects.all()
    else:
        companies_list = Company.objects.filter(customer_assistant=request.user.customer_assistant)
    return render(request,'zapp/companies.html',{'section':'companies','companies':companies_list})

@login_required
def company_details(request, slug):
    company = get_object_or_404(Company, slug = slug)
    return render(request,'zapp/company_details.html',{'section':'companies','company' : company})

@login_required
def company_add(request):
    if request.method == 'POST':
        form = CompanyAddForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            new_company = form.save(commit=False)
            slug = slugify(cd['name'])
            new_company.slug = slug
            new_company.customer_assistant = request.user.customer_assistant
            new_company.save()
            messages.success(request,'Dodawanie zakończone sukcesem')
            return redirect(reverse('company_details', args=[slug]))
        else:
            form = CompanyAddForm()
            return render(request, 'zapp/company_add.html', {'section': 'companies', 'form': form})
    else:
        form = CompanyAddForm()
        return render(request,'zapp/company_add.html', {'section':'companies','form' : form})

@login_required
def users(request):
    if request.user.username == 'admin':
        ca_list = Customer_Assistant.objects.all()
    else:
        ca_list = Customer_Assistant.objects.all().exclude(user=request.user)
    return render(request,'zapp/users.html',{'section':'users','users':ca_list})

@login_required
def user_details(request, username):
    user = Customer_Assistant.objects.get(user__username=username)
    return render(request,'zapp/user_details.html',{'section':'users','user' : user})

@login_required
def user_edit(request, username):
    user = User.objects.get(username=username)
    ca = Customer_Assistant.objects.get(user__username=username)
    if request.method == 'POST':
        user_form = UserEditForm(instance=user, data=request.POST)
        ca_form = CustomerAssistEditForm(instance=ca, data=request.POST, files=request.FILES)
        if user_form.is_valid() and ca_form.is_valid():
            user_form.save()
            ca_form.save()
            messages.success(request, 'Edycja zakończona sukcesem')
            return redirect(reverse('user_details', args=[user.username]))
        messages.warning(request, 'Niektóre pola zostały niewłaściwie wypełnione.')
    else:
        user_form = UserEditForm(instance=user)
        ca_form = CustomerAssistEditForm(instance=ca)
    return render(request, 'zapp/user_edit.html', {'section':'users','user_form': user_form, 'ca_form': ca_form, 'user': ca})


@login_required
def company_edit(request, company):
    comp = Company.objects.get(slug=company)
    if request.method == 'POST':
        comp_form = CompanyEditForm(instance=comp, data=request.POST)
        if comp_form.is_valid():
            comp_form.save()
            messages.success(request, 'Edycja zakończona sukcesem.')
            return redirect(reverse('company_details', args=[comp.slug]))
        messages.warning(request, 'Niektóre pola zostały niewłaściwie wypełnione.')
    else:
        comp_form = CompanyEditForm(instance=comp)
    return render(request, 'zapp/company_edit.html', {'section':'companies','comp_form': comp_form, 'company': company})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            ca = Customer_Assistant.objects.create(user=new_user)
            return render(request,
                          'zapp/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'zapp/register.html',
                  {'user_form': user_form})

