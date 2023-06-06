from django.shortcuts import render,get_object_or_404,redirect

from .models import Post
from .forms import CommentForm
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request,'index.html')

def post_list(request):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    # Pagination
    paginator = Paginator(queryset, 1)  # Show 1 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'post_list': queryset,'page_obj': page_obj}
    return render(request, template_name, context)
    
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comment_form = CommentForm()
    template_name = 'post-detail.html'
    context = {'post': post,'comment_form': comment_form}
    return render(request, template_name, context) 


def create_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
    return redirect('post_detail', slug=slug)