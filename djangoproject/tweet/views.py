# from django.shortcuts import render
# from .models import Tweet
# from .forms import TweetForm
# from django.shortcuts import get_object_or_404, redirect
# # Create your views here.

# def index(request):
#     return render(request, 'index.html')

# def tweet_list(request):
#     tweets = Tweet.objects.all().order_by('-created_at')
#     return render(request, 'tweet_list.html',{'tweets':tweets})

# def tweet_create(request):
#     if request.method == "POST":
#         form = TweetForm(request.POST,request.FILES)
#         if form.is_valid():
#             tweet = form.save(commit=False)
#             tweet.user = request.user   
#             tweet.save()
#             return redirect('tweet_list')
#     else:
#         form = TweetForm()
#     return render(request, 'tweet_form.html',{'form':form})

# def tweet_edit(request, tweet_id):
#     tweet = get_object_or_404(Tweet, pk = tweet_id, user=request.user)
#     if request.method == 'POST':
#         form = TweetForm(request.POST, request.FILES, instance=tweet)
#         if form.is_valid():
#             tweet = form.save(commit=False)
#             tweet.user = request.user
#             tweet.save()
#             return redirect('tweet_list')
#     else:
#         form = TweetForm(instance=tweet)
#     return render(request, 'tweet_form.html',{'form':form})


# def tweet_delete(request, tweet_id):
#     tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user )
#     if request.method == 'POST':
#         tweet.delete()
#         return redirect('tweet_list')
#     return render(request, 'tweet_confirm_delete.html',{'tweet':tweet})




































# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Tweet
# from .forms import TweetForm, UserRegistrationForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login
# from django.contrib.auth.models import User

# # Create your views here.

# def index(request):
#     return render(request, 'index.html')

# def tweet_list(request):
#     tweets = Tweet.objects.all().order_by('-created_at')
#     return render(request, 'tweet_list.html', {'tweets': tweets})

# def tweet_create(request):
#     if not request.user.is_authenticated:
#         # Handle the case where the user is not authenticated
#         # For now, redirect to tweet list or show a message
#         return redirect('tweet_list')  # Or render a page with a message
    
#     if request.method == "POST":
#         form = TweetForm(request.POST, request.FILES)
#         if form.is_valid():
#             tweet = form.save(commit=False)
#             tweet.user = request.user   
#             tweet.save()
#             return redirect('tweet_list')
#     else:
#         form = TweetForm()
#     return render(request, 'tweet_form.html', {'form': form})

# def tweet_edit(request, tweet_id):
#     if not request.user.is_authenticated:
#         return redirect('tweet_list')

#     tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
#     if request.method == 'POST':
#         form = TweetForm(request.POST, request.FILES, instance=tweet)
#         if form.is_valid():
#             tweet = form.save(commit=False)
#             tweet.user = request.user
#             tweet.save()
#             return redirect('tweet_list')
#     else:
#         form = TweetForm(instance=tweet)
#     return render(request, 'tweet_form.html', {'form': form})

# def tweet_delete(request, tweet_id):
#     if not request.user.is_authenticated:
#         return redirect('tweet_list')

#     tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
#     if request.method == 'POST':
#         tweet.delete()
#         return redirect('tweet_list')
#     return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})


# def Register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password1'])
#             user.save()
#             login(request,user)
#             return redirect('tweet_list')
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'registration/register.html', {'form': form})



























from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user   
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
# def tweet_delete(request, tweet_id):
#     tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
#     if request.method == 'POST':
#         tweet.delete()
#         return redirect('tweet_list')
#     return render

# def tweet_delete(request, tweet_id):
#     if not request.user.is_authenticated:
#         return redirect('tweet_list')

#     tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
#     if request.method == 'POST':
#         tweet.delete()
#         return redirect('tweet_list')
#     return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

# def tweet_delete(request, tweet_id):
#     tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user )
#     if request.method == 'POST':
#         tweet.delete()
#         return redirect('tweet_list')
#     return render(request, 'tweet_confirm_delete.html',{'tweet':tweet})












def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

