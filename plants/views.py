from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Plant, UserPlant, Comment
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    """首页视图"""
    recent_plants = Plant.objects.all().order_by('-created_at')[:6]
    return render(request, 'plants/home.html', {
        'recent_plants': recent_plants
    })

class PlantListView(ListView):
    """植物列表视图"""
    model = Plant
    template_name = 'plants/plant_list.html'
    context_object_name = 'plants'
    paginate_by = 12

    def get_queryset(self):
        queryset = Plant.objects.all().order_by('-created_at')
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query) | \
                      queryset.filter(scientific_name__icontains=search_query)
        return queryset

class PlantDetailView(DetailView):
    """植物详情视图"""
    model = Plant
    template_name = 'plants/plant_detail.html'
    context_object_name = 'plant'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comment_set.all().order_by('-created_at')
        if self.request.user.is_authenticated:
            context['user_plant'] = UserPlant.objects.filter(
                user=self.request.user,
                plant=self.object
            ).first()
        return context

@login_required
def add_user_plant(request, plant_id):
    """添加用户植物"""
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        UserPlant.objects.create(
            user=request.user,
            plant=plant,
            nickname=request.POST.get('nickname', ''),
            acquired_date=request.POST.get('acquired_date')
        )
        messages.success(request, '成功添加植物到您的收藏！')
        return redirect('plant_detail', pk=plant_id)
    return render(request, 'plants/add_user_plant.html', {'plant': plant})

@login_required
def add_comment(request, plant_id):
    """添加评论"""
    plant = get_object_or_404(Plant, id=plant_id)
    if request.method == 'POST':
        Comment.objects.create(
            user=request.user,
            plant=plant,
            content=request.POST.get('content')
        )
        messages.success(request, '评论发布成功！')
    return redirect('plant_detail', pk=plant_id) 