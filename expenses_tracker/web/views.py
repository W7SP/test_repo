from django.shortcuts import render, redirect


# Create your views here.
from expenses_tracker.web.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateExpenseForm, \
    EditExpenseForm, DeleteExpenseForm
from expenses_tracker.web.models import Profile, Expenses


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]

    return None


def show_index(request):
    profile = get_profile()
    expenses = Expenses.objects.all()
    budget_left = profile.budget - sum(expense.price for expense in expenses)

    if not profile:
        return redirect('create profile')

    context = {
        'profile': profile,
        'expenses': expenses,
        'budget_left': budget_left,
    }

    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateExpenseForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expenses.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditExpenseForm()

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expenses.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteExpenseForm()

    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-delete.html', context)


def show_profile(request):
    profile = get_profile()
    expenses = Expenses.objects.all()
    budget_left = profile.budget - sum(expense.price for expense in expenses)

    context = {
        'profile': profile,
        'expenses': expenses,
        'expenses_count': len(expenses),
        'budget_left': budget_left,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-delete.html', context)

