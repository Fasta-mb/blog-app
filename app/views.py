from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from app.forms import CommentForm, PostForm
from app.models import Comment, Post
from authentications.forms import ProfileForm
from django.db.models import Q

from authentications.models import Profile
from django.contrib.auth.decorators import login_required

def home(request):
    post_datas = Post.objects.all()

    topPosts = Post.objects.all().order_by('-num_view')[0:3]
    newPosts = Post.objects.all().order_by('-created_at')[0:3]
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    searches = Post.objects.filter(
        Q(title__icontains=q) |
        Q(author__username__icontains=q)
    )
   
    context = {
        'post_datas': post_datas, 
        'searches': searches,
        'q': q,
        'topPosts': topPosts,
        'newPosts': newPosts,
        }
    return render(request, 'app/index.html', context)



# get the user data
@login_required(login_url='login')
def profileUser(request):
    actual_user = request.user.id
    comment_count = Comment.objects.filter(user=actual_user).count()
    if request.user.is_authenticated:
        profs = Profile.objects.filter(author=actual_user)
        posts = Post.objects.filter(author=request.user.id)
        post_count = posts.count()
        if request.POST:
            form = ProfileForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                form_save = form.save(commit=False)
                form_save.author = request.user
                form_save.save()
                return redirect(reverse('profile-user'))
        else:
            form = ProfileForm()
    else: 
        return redirect(reverse('login'))
    context = { 
                'profs': profs,
                'form':form,
                'posts': posts,
                'post_count': post_count,
                'comment_count': comment_count,
               }
    return render(request, 'app/profile_user.html', context)

@login_required(login_url="login")
def editProfileUser(request):
    if request.user.is_authenticated:
        if request.POST:
            
            prof = ProfileForm(instance=request.user.profile,data=request.POST, files=request.FILES)
        
            if prof.is_valid():
                prof.save()
                return redirect(reverse('profile-user'))
        else:
            prof = ProfileForm(instance=request.user.profile)
    else:
        return redirect(reverse('login'))
    context = { 'prof': prof}
    return render(request, 'app/profile_user_edit.html', context)

@login_required(login_url="login")
def postCreate(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            postsave = form.save(commit=False)
            postsave.author = request.user
            postsave.save()
            return redirect(reverse('home'))
    else:
        form = PostForm()
    
    context = {'form': form}
    return render(request, 'app/create_post.html', context)

#edit and delete post
@login_required(login_url="login")
def postedit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form_edit = PostForm(instance=post, data=request.POST, files=request.FILES)
        if form_edit.is_valid():
            form_edit.save()
            return redirect(reverse('home'))
    else:
        form_edit =PostForm(instance=post)
    
    context = {'form_edit': form_edit}
    
    return render(request, 'app/post_edit.html', context)

@login_required(login_url="login")
def postDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect(reverse('home'))

def notification(request):
    notifs = Post.objects.all().order_by('-created_at')[0:4]
    return render(request, 'app/notification.html', {'notifs': notifs})

def postDisplay(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    
    recent_blog = Post.objects.all().order_by('-created_at')[0:3]
    spec_comment = post.comment_set.all()
    

    if post.num_view is None:
        post.num_view = 1
    else:
        post.num_view = post.num_view + 1
    
        
    post.save()
    
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            save_comment = comment.save(commit=False)
            save_comment.user = request.user
            save_comment.post = post
            save_comment.save()
            return HttpResponseRedirect(reverse('post-display', kwargs={'pk': pk}))
    else:
        comment = CommentForm()
    context = {'post': post,
               'comment': comment,
               'spec_comment': spec_comment,
               'recent_blog': recent_blog
               }
    return render(request, 'app/post_display.html', context)




    
    
    
        
        
