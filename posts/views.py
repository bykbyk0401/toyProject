from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import  *
from django.db import models
import json
# Create your views here.

@require_http_methods(["DELETE"])
def delete_post(request,id):
    delete_post=get_object_or_404(Post,pk=id)
    delete_post.delete()

    return JsonResponse({
        'status':200,
        'message':'방명록 삭제 성공',
    })


@require_http_methods(["GET"])
def get_post_all(request):

    post_all = Post.objects.all()
    
    post_json_all = []
    for post in post_all:
        post_json = {
            "id": post.post_id,
            "writer": post.writer,
            "content": post.content,
            "date": post.date
        }
        post_json_all.append(post_json)
    
    return JsonResponse({
        'status': 200,
        'message': '모든 방명록 조회 성공',
        'data': post_json_all
    })

@require_http_methods(["GET"])
def get_post(request,id):
        post = get_object_or_404(Post, pk=id)
        
        post_json = {
            "id": post.post_id,
            "name": post.writer,
            "content": post.content,
            "date": post.date
        }

        return JsonResponse({
            'status': 200,
            'message': '방명록 조회 성공',
            'data': post_json
        })


@require_http_methods(["POST"])
def create_post(request):
    body = json.loads(request.body.decode('utf-8'))

    new_post=Post.objects.create(
        writer=body['writer'],
        content=body['content'],
        date=body['date']
    )

    new_post_json={
        "id":new_post.post_id,
        "name":new_post.writer,
        "content":new_post.content,
        "date":new_post.date
    }

    return JsonResponse({
        'status':200,
        'message':'방명록 작성 성공',
        'data':new_post_json
    })