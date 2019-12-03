from django.shortcuts import render
from core.models import Post, Comment
from django.shortcuts import get_object_or_404
from django.utils.formats import date_format
from django.urls import reverse, reverse_lazy
from core.forms import ContactUsForm
from django.views.generic import View, TemplateView, ListView, DetailView, FormView


def post_list_view(request):
    ctx = {}
    post_list = list()
    for post in Post.objects.filter(public = True):
        post_list.append({
            'url': post.get_absolute_url(),
            'imageUrl': post.image.url,
            'title': post.title.title(),
            'date': date_format(post.public_date),
            'count': post.comment_set.count()
        })
    ctx['post_list'] = post_list
    return render(request, 'core/post_list.html', ctx)

def comment_list_view(request):
    ctx = {}
    sort = request.GET.get('sort', 'id')
    comment_qs = Comment.objects.all()
    ctx['comment_list'] = comment_qs.order_by(sort)
    return render(request, 'core/comment_list.html', ctx)

def post_detail_view(request, slug):
    ctx = {}
    post = Post.objects.filter(slug=slug).first()
    if post:
        ctx['post'] = post.title.title()
        ctx['comment_list'] = post.comment_set.all()
    return render(request, 'core/comment_list.html', ctx)

def index_view(request):
    ctx = {}
    ctx['comment_list'] = Comment.objects.all()
    return render(request, 'core/index.html', ctx)

def comment_detail_view(request, pk, slug):
    ctx = {}
    comment = Comment.objects.filter(pk=pk).first()
    if comment:
        ctx['comment'] = comment
    return render(request, 'core/comment.html', ctx)

class ContactUsFormView(FormView):
    template_name = 'contact_us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
