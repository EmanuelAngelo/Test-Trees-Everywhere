from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import generics, permissions
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import PlantedTree, Account, Tree
from django.urls import reverse
from .serializers import PlantedTreeSerializer
from .forms import PlantedTreeForm, LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('trees:planted_tree_list'))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def planted_tree_list(request):
  user = request.user
  object_list = PlantedTree.objects.filter(user=user)
  paginator = Paginator(object_list, 4)
  page = request.GET.get('page')
  try:
     posts = paginator.page(page)
  except PageNotAnInteger:
     posts = paginator.page(1)
  except EmptyPage:
     posts = paginator.page(paginator.num_pages)
  return render(request,
                'tree/post/list.html',
                {'page':page, 'posts':posts})

@login_required
def planted_tree_detail(request, id, year, month, day, post):
    try:
        post = PlantedTree.objects.filter(
            slug=post,
            id=id,
            status='published',
            publish__year=year,
            publish__month=month,
            publish__day=day
        ).first()
    except PlantedTree.DoesNotExist:
        post = None

    if post is None:
        return HttpResponseNotFound("A árvore solicitada não foi encontrada.")

    return render(request, 'tree/post/detail.html', {'post': post})



class PlantedTreeListAPIView(generics.ListAPIView):
  serializer_class = PlantedTreeSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return PlantedTree.objects.filter(user=self.request.user)


@login_required
def add_planted_tree(request):
    if request.method == 'POST':
        form = PlantedTreeForm(request.POST)
        if form.is_valid():
            planted_tree = form.save(commit=False)
            planted_tree.user = request.user
            planted_tree.save()
            return redirect('planted_tree_detail', id=planted_tree.id)
    else:
        form = PlantedTreeForm()

    accounts = Account.objects.all()
    trees = Tree.objects.all()

    print(accounts.name)
    print(trees)

    return render(request, 'add_planted_tree.html', {'form': form, 'accounts': accounts, 'trees': trees})
