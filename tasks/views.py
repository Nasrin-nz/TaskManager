
from .forms import ReferralForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Action, Task
from .forms import ActionForm
from django.contrib.auth.decorators import login_required


# @login_required
def create_referral(request):
    if request.method == 'POST':
        form = ReferralForm(request.POST)
        if form.is_valid():
            referral = form.save(commit=False)
            referral.referring_user = request.user
            referral.registration_time = timezone.now()  # Set the registration time to the current time
            referral.save()
            return redirect('referral_success')  # Redirect to a success page or another view
    else:
        form = ReferralForm()

    return render(request, 'tasks/create_referral.html', {'form': form})

def referral_success(request):
    return render(request, 'tasks/referral_success.html')



# @login_required
def create_action(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = ActionForm(request.POST, request.FILES)
        if form.is_valid():
            action = form.save(commit=False)
            action.task = task
            action.registering_user = request.user
            action.registration_time = timezone.now()
            action.save()


            return redirect('action_success')
    else:
        form = ActionForm()

    return render(request, 'tasks/create_action.html', {'form': form, 'task': task})


def action_success(request):
    return render(request, 'tasks/action_success.html')



def user_dashboard(request):
    # Placeholder for user dashboard content
    return render(request, 'tasks/user_dashboard.html')

def general_dashboard(request):
    # Placeholder for general dashboard content
    return render(request, 'tasks/general_dashboard.html')
