from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from . models import Post
from django.views.generic import ListView ,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
# Create your views here.

# post = [
#     {
#         'author':"a",
#         "title":"asdl;sa"
#     },
#     {
#         'author':"OJLKLKL",
#         "title":"aojdalssad",
#     }
# ]


# def home(request):
#     context = {
#         'posted':Post.objects.all()
#     }
#     return render(request,"blog/home.html",context)

class PostList(ListView):
    model = Post 
    template_name = 'blog/home.html'
    context_object_name = 'posted'
    ordering = ['-post_date']
    paginate_by = 5

class UserList(ListView):
    model = Post 
    template_name = 'blog/user_posts.html'
    context_object_name = 'posted'
    ordering = ['-post_date']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username')) #get user from url
        return Post.objects.filter(author=user,post_date__isnull=False).order_by('-post_date')


class PostDetail(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin,CreateView):
    
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

class PostUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'blog/confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False

class DraftListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/post_drafts_list.html'
    success_url = reverse_lazy('post-detail')
    context_object_name = 'posted'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(post_date__isnull=True).order_by('create_date')

def about(request):
    return render(request,"blog/about.html")

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post-detail',username=post.author,pk=pk)
