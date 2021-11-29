from django.shortcuts import render
from .models import Post

# Create your views here.


def detail(req, question_id):
    try:
        obj = Post.objects.get(pk=question_id)
        context = {
            "title": obj.title,
            "content": obj.content,
            "image_url": obj.feature_image.url
        }
    except Post.DoesNotExist:
        context = {"title": "No post id: %s" % question_id}

    return render(req, 'post/index.html', {"post": context})
