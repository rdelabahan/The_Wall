from django.shortcuts import render, redirect
from .models import Wall_Message, Comment
from login_app.models import User

def index(request):
    if "user_id" not in request.session:
        return redirect('/')
    context = {
        'wall_messages': Wall_Message.objects.all(),
    }
    return render(request,'wall.html',context)

def post_message(request):
    Wall_Message.objects.create(message = request.POST['message'], poster = User.objects.get(id = request.session['user_id']))
    return redirect('/wall')

def delete_comment(request, id):
    poster = Comment.objects.get(id=id)
    if request.session['user_id'] == poster.poster.id:
        poster.delete()
        print('id did match!!!')
        return redirect('/wall')
    else:
        print('id does not match')
        return redirect('/wall')

def post_comment(request, id):
    poster = User.objects.get(id = request.session['user_id'])
    message = Wall_Message.objects.get(id = id)
    Comment.objects.create(
        comment = request.POST['comment'],
        poster = poster,
        wall_message = message,
    )
    return redirect('/wall')

def profile(request, id):
    context = {
        "user": User.objects.get(id = id)
    }
    return render(request,'profile.html',context)

def add_like(request, id):
    liked_message = Wall_Message.objects.get(id = id)
    user_liking = User.objects.get(id = request.session['user_id'])
    liked_message.user_likes.add(user_liking)
    return redirect('/wall')