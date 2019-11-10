from django.shortcuts import render
from core.models import Posts, Comments
from django.shortcuts import get_object_or_404

# Create your views here.


def index_view(request):
    ctx = {}
    ctx['comment_list'] = Comments.objects.all()
    return render(request, 'core/index.html', ctx)

def comment_list_view(request):
    sort = request.GET.get('sort', 'id')
    comment_qs = Comments.objects.all()
    ctx = {}
    ctx['comment_list'] = comment_qs.order_by(sort)
    return render(request, 'core/comment_list.html', ctx)

def comment_detail_view(request, pk, slug):
    ctx = {}
    comment = Comments.objects.filter(pk=pk).first()
    if comment:
        ctx['comment'] = comment
    return render(request, 'core/comment.html', ctx)

def post_list_view(request):
    ctx = {}
    post_list = list()
    for post in Posts.objects.all():
        post_list.append({
            'url': post.get_absolute_url(),
            'title': post.title.title(),
            'count': post.comment_set.count()
        })
    ctx['post_list'] = post_list
    return render(request, 'core/post_list.html', ctx)

def post_detail_view(request, slug):
    ctx = {}
    post = Posts.objects.filter(slug=slug).first()
    if post:
        ctx['post'] = post.title.title()
        ctx['comment_list'] = post.comment_set.all()
    return render(request, 'core/post.html', ctx)
