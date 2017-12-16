from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer


# Create your views here.


def test(request, *args, **kwargs):
    return HttpResponse("Ok")


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


# New questions


def index(request):
    t = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(t, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    # page, paginator = paginate(request, t)
    return render(request, 'index.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })

# def post_list_all(request):
#     posts = Post.objects.filter(is_published=True)
#     limit = request.GET.get('limit', 10)
#     page = request.GET.get('page', 1)
#     paginator = Paginator(posts, limit)
#     paginator.baseurl = '/blog/all_posts/?page='
#     page = paginator.page(page) # Page
#     return render(request, 'blog/post_by_tag.html', {
#         'posts':  page.object_list,
#         'paginator': paginator, 'page': page,
# })


def popular(request):
    t = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(t, limit)
    page = paginator.page(page)
    # page, paginator = paginate(request, t)
    return render(request, 'popular.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
    })


def question(request, pk):
    t = get_object_or_404(Question, id=pk)
    #id = request.GET.get(pk)
    # t = Question.objects.get(id=pk)
    try:
        a = Answer.objects.filter(question_id=pk)
    except Answer.DoesNotExist:
        raise Http404
    return render(request, 'question.html', {
        'title': t.title,
        'text': t.text,
        'answer': a,
    })
