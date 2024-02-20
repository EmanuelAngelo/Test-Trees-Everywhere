from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import PlantedTree
from .forms import PlantedTreeForm

@login_required
def dashboard(request):
    user_planted_trees = request.user.plantedtree_set.all()

    context = {
        'user_planted_trees': user_planted_trees,
    }

    return render(request, 'dashboard.html', context)

def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('trees:dashboard')
  else:
    form = AuthenticationForm()
  return render(request, 'login.html', {'form':form})


def my_trees(request):
  trees = PlantedTree.objects.filter(user=request.user)
  return render(request, 'my_trees.html', {'trees': trees})


def add_planted_tree(request):
  if request.method == 'POST':
    form = PlantedTreeForm(request.POST)
    if form.is_valid():
      planted_tree = form.save(commit=False)
      planted_tree.user = request.user
      planted_tree.save()
      return redirect('my_trees')
  else:
    form = PlantedTreeForm()
  return render(request, 'add_planted_tree.html', {'form': form})

#testando
@login_required
def planted_tree_list(request):
  posts = PlantedTree.published.all()
  return render(request,
                'tree/post/list.html',
                {'posts':posts})


def planted_tree_detail(request, year, month, day, post):
  post = get_object_or_404(PlantedTree, slug=post,
                           status='published',
                           publish__year=year,
                           publish__month=month,
                           publish__day=day)
  return render(request, 'tree/post/detail.html', {'post':post})