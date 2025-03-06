from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Category,Tag
from .forms import CommentForm,SearchForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages


def about(request):
    return render(request,'blog/about.html')

def post_list(request):
    post_list = Post.objects.all().order_by('-created_at')
    query = request.GET.get('query')

    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    search_form = SearchForm(request.GET)

    context = {
        'page_obj':page_obj,
        'search_form':search_form,
    }
    return render(request,'blog/post_list.html',context)


def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post 
            comment.save()
            messages.success(request,'نظر شما با موفقیت ثبت شد')
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()

    context = {
        'post':post,
        'comments':comments,
        'form':form,
    }

    return render(request,'blog/post_detail.html',context)


def posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    post_list = Post.objects.filter(category=category).order_by('-created_at')
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category':category,
        'page_obj':page_obj,
    }
    return render(request, 'blog/posts_by_category.html', context)

def posts_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    post_list = Post.objects.filter(tags=tag).order_by('-created_at')
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'tag':tag,
        'page_obj':page_obj
    }
    return render(request, 'blog/posts_by_tag.html',context)

