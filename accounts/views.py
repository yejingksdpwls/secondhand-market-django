from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            auth_login(request, form.save())
            return redirect("main")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


@require_http_methods(["GET","POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get("next") or "main"
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


@login_required
@require_http_methods(["POST"])
def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect("main")


@login_required
@require_http_methods(["POST"])
def delete(request):
    if request.method == "POST":
        request.user.delete()
        auth_logout(request)
    return redirect("main")



@login_required
@require_http_methods(["POST", "GET"])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            next_url = request.GET.get("next") or "main"
            return redirect(next_url)
    else:
        form = CustomUserChangeForm(request.POST)
    context = {"form":form}
    return render(request, "accounts/update.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            next_url = request.GET.get("next") or "main"
            return redirect(next_url)
    else:
        form = PasswordChangeForm(request.user)
    context = {"form":form}
    return render(request, "accounts/password.html", context)


@require_http_methods(["POST"])
def follow(request, pk):
    if request.user.is_authenticated:
        user = get_object_or_404(get_user_model(), pk=pk)
        if request.user != user:
            if request.user in user.followers.all():
                user.followers.remove(request.user)
            else:
                user.followers.add(request.user)
        next_url = request.GET.get("next") or "main"
        return redirect(next_url)
    return redirect("accounts:login")


def profile(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    context = {"user":user}
    return render(request, "accounts/profile.html", context)