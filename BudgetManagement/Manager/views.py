from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from .forms import DataForm, IncomeForm, ExpenseForm
from . import models
# Create your views here.

class signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('main')
    template_name = 'signup.html'
'''
def main2(request):
    return render(request, 'main2.html')


def getInfo(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.address = form.cleaned_data.get('address')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def getInfo(request):
    user = DataForm(request.POST or None)
    if user.is_valid():
        user.save()
        return redirect('http://127.0.0.1:8000/main2/')
    return render(request, 'main.html', {'form':user})
'''

class getInfo(generic.CreateView):
    form_class = DataForm
    success_url = reverse_lazy('login')
    template_name = 'main.html'

class setIncome(generic.CreateView):
    form_class = IncomeForm
    success_url = reverse_lazy('main4')
    template_name = 'income.html'

class setExpense(generic.CreateView):
    form_class = ExpenseForm
    success_url = reverse_lazy('main4')
    template_name = 'expense.html'

def view(request):
    users = models.Profile.objects.all()
    incomes = models.Income.objects.all()
    expenses = models.Expense.objects.all()
    for user in users:
        flag=False
        user.total_income=0
        for income in incomes:
            if user.user==income.user:
                user.total_income+=income.income_amount

        user.total_expense=0
        for expense in expenses:
            if user.user==expense.user:
                user.total_expense+=expense.expense_amount

        user.total_savings=0
        user.total_savings=user.total_income-user.total_expense

        if user.total_savings>=0.3*user.total_income:
            flag=True

        user.save()
    return render(request, 'view.html', {'users':users, 'incomes':incomes, 'expenses':expenses, 'flag':flag})