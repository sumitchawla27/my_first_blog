from django.shortcuts import render
from .models import Post
from django.utils import timezone
#filter(published_date__lte=timezone.now())
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts':posts})
