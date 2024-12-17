from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from .forms import CategoryForm, PreacherForm, PlaylistForm, SermonForm
from .models import Category, Preacher, Playlist, Sermon
from django.db.models import Count, Q

from base_apmo.forms import SignUpForm

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import SermonSerializer

# Create your views here.

def signup(request):
    form = SignUpForm()
    context = {
        'username': '',
        'password1': '',
        'password2': '',
        'email': '',
        'form': form,
    }

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        context['username'] = request.POST.get('username')
        context['password1'] = request.POST.get('password1')
        context['password2'] = request.POST.get('password2')
        context['email'] = request.POST.get('email')
        context['form'] = form

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            form.save()
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("home")
        else:
            messages.error(request, form.errors)
    
    return render(request, "auth/signup.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def loginPage(request):
    context = {
        'username': '',
        'password': ''
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        context['username'] = username
        context['password'] = password

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid Credentials')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong credentials')

    return render(request, 'auth/login.html', context)

        

@login_required
def home(request):
    sermons = Sermon.objects.all()
    total_sermons = Sermon.objects.count()
    total_audio_sermons = Sermon.objects.filter(~Q(audio_file="")).count()

    context = {
        'sermons': sermons,
        'total_sermons': total_sermons,
        'total_audio_sermons': total_audio_sermons
    }
    return render(request, "dashboard.html", context)


@login_required
def categories(request):
    categories = Category.objects.all()
    preachers = Preacher.objects.all()
    playlists = Playlist.objects.all()
    context = {
        'categories' : categories,
        'preachers' : preachers,
        'playlists' : playlists,
    }
    return render(request, 'sermons/category.html', context)


@login_required
def createCategory(request):
    form = CategoryForm
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            messages.success(request, "Category has been created")
            form.save()
            return redirect('categories')
    return render(request, 'sermons/add_category_form.html')

@login_required
def createPreacher(request):
    form = PreacherForm()
    if request.method == 'POST':
        form = PreacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Preacher has been added")
            return redirect('categories')
        else:
            messages.error(request, "Please correct the errors below.")
    
    return render(request, 'sermons/add_preacher_form.html', {'form': form})


@login_required
def createPlaylist(request):
    form = PlaylistForm
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            messages.success(request, "Playlist has been created")
            form.save()
            return redirect('categories')
    return render(request, 'sermons/add_playlist_form.html')


@login_required
def createSermon(request):
    form = SermonForm
    preachers = Preacher.objects.all()
    categories = Category.objects.all()
    playlists = Playlist.objects.all()

    context = {
        'preachers': preachers,
        'categories': categories,
        'playlists': playlists,
        'form' : form
    }

    if request.method == 'POST':
        form = SermonForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, "Sermon has been created")
            form.save()
            return redirect('home')
        else:
            print("Form errors:")
            for field, errors in form.errors.items():
                print(f"{field}: {errors}")
    
    return render(request, 'sermons/add_sermons_form.html', context)


@login_required(login_url='/login')
def editCategory(request, pk):
    category = Category.objects.get(id=pk)
    context = {
        'category': category
    }

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            messages.success(request, "Category has been edited")
            form.save()
            return redirect('categories')
    return render(request, 'sermons/edit_category.html', context)


@login_required(login_url='/login')
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    context = {
        'category': category
    }
    if request.method == 'POST':
        category.delete()
        messages.success(request, "Category has been deleted")
        return redirect('categories')
    return render(request, 'sermons/delete_category.html', context)

@login_required
def editPreacher(request, pk):
    preacher = Preacher.objects.get(id=pk)
    context = {
        'preacher' : preacher,
    }

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=preacher)
        if form.is_valid():
            messages.success(request, "Preacher has been edited successfully")
            form.save()
            return redirect("categories")
        
    return render(request, "sermons/edit_preacher.html", context)


@login_required(login_url='/login')
def deletePreacher(request, pk):
    preacher = Preacher.objects.get(id=pk)
    context = {
        'preacher': preacher
    }
    if request.method == 'POST':
        preacher.delete()
        messages.success(request, "Preacher has been deleted")
        return redirect('categories')
    return render(request, 'sermons/delete_preacher.html', context)


@login_required
def editPlaylist(request, pk):
    playlist = Playlist.objects.get(id=pk)
    context = {
        'playlist' : playlist,
    }

    if request.method == "POST":
        form = PlaylistForm(request.POST, instance=playlist)
        if form.is_valid():
            messages.success(request, "Playlist has been edited successfully")
            form.save()
            return redirect("categories")
        
    return render(request, "sermons/edit_playlist.html", context)


@login_required(login_url='/login')
def deletePlaylist(request, pk):
    playlist = Playlist.objects.get(id=pk)
    context = {
        'playlist': playlist
    }
    if request.method == 'POST':
        playlist.delete()
        messages.success(request, "Playlist has been deleted")
        return redirect('categories')
    return render(request, 'sermons/delete_playlist.html', context)


@login_required
def editSermon(request, pk):
    sermon = Sermon.objects.get(id=pk)
    context = {
        'sermon' : sermon,
    }

    if request.method == "POST":
        form = SermonForm(request.POST, instance=sermon)
        if form.is_valid():
            messages.success(request, "Sermon has been edited successfully")
            form.save()
            return redirect("home")
        
    return render(request, "sermons/edit_sermons.html", context)


@login_required(login_url='/login')
def deleteSermon(request, pk):
    sermon = Sermon.objects.get(id=pk)
    context = {
        'sermon': sermon
    }
    if request.method == 'POST':
        sermon.delete()
        messages.success(request, "Sermon has been deleted")
        return redirect('home')
    return render(request, 'sermons/delete_sermons.html', context)




# Api Views
class SermonListView(APIView):
    def get(self, request):
        sermons = Sermon.objects.all()
        serializer = SermonSerializer(sermons, many=True, context={'request': request})
        return Response(serializer.data)
