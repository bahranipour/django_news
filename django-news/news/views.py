from django.shortcuts import render,get_object_or_404,redirect
from .models import News,Category,Tag
from .forms import CommentForm,SearchForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages


def about(request):
    return render(request,'news/about.html')


def news_list(request,category_id=None):
    category = None
    news_list = News.objects.all().order_by('-created_at')
    query = request.GET.get('query')
   
    categories = Category.objects.all()

    if category_id:
        category = get_object_or_404(Category,id=category_id)
        news_list = News.objects.filter(category=category).order_by('-created_at')
    

    if query:
        news_list = news_list.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    paginator = Paginator(news_list,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    search_form = SearchForm(request.GET)

    context = {
        'page_obj':page_obj,
        'search_form':search_form,
        'category':category,
        'categories':categories,
    }

    return render(request,'news/news_list.html',context)


def news_detail(request,pk):
    news = get_object_or_404(News,pk=pk)
    comments = news.comments.filter(active=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news 
            comment.save()
            messages.success(request,'نظر شما با موفقیت ثبت شد')
            return redirect('news_detail',pk=news.pk)
    else:
        form = CommentForm()

    
    context = {
        'news':news,
        'comments':comments,
        'form':form,
    }

    return render(request,'news/news_detail.html',context)




def news_by_tag(request,tag_id):
    tag = get_object_or_404(Tag,id=tag_id)
    news_list = News.objects.filter(tags=tag).order_by('-created_at')
   


    paginator = Paginator(news_list,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    context = {
     
        'tag':tag,
        'page_obj':page_obj
    }

    return render(request,'news/news_by_tag.html',context)

    