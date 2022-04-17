from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

def index(request):
	"""Домашняя страница приложения Blogs"""
	title = BlogPost.objects.all()
	text = BlogPost.objects.order_by('-date_added')
	context = {'title': title, 'text': text}
	return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
	"""Определяет новую запись"""
	if request.method != 'POST':
		# Данные не отправились создается пустая форма
		form = BlogPostForm()
	else:
		# Отправленны данные POST; обработать данные
		form = BlogPostForm(data=request.POST)
		if form.is_valid():
			new_text = form.save(commit=False)
			new_text.owner = request.user
			new_text.save()
			return redirect('blogs:index')

	# Вывести пустую или недействительную форму
	context = {'form': form}
	return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, texts_id):
	texts = BlogPost.objects.get(id=texts_id)
	if request.method != 'POST':
		form = BlogPostForm(instance=texts)
	else:
		form = BlogPostForm(instance=texts, data=request.POST)
		if form.is_valid():
			if texts.owner != request.user:
				raise Http404
			form.save()
			return redirect('blogs:index')

	context = {'texts': texts, 'form': form}
	return render(request, 'blogs/edit_post.html', context)