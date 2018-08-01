from django.shortcuts import render, get_object_or_404
from .models import Hostel
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def homepage(request):
    context = { 'section':'hostels'}
    return render(request,'hostel/homepage.html', context) 

def hostel_list(request):
    object_list = Hostel.vacanthostel.all()
    paginator = Paginator(object_list, 8)
    page = request.GET.get('page')
    try:
        hostels = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        hostels = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        hostels = paginator.page(paginator.num_pages)
    context = { 'hostels':hostels,'section':'hostels', 'page':page,}
    return render(request,'hostel/hostels.html', context)


def hostel_detail(request, year, month, day, title, location):
    hostel = get_object_or_404(Hostel, slug=title, location=location, vacant=True, created__year = year,
                created__month=month, created__day= day)
    '''
    # List of similar houses
    house_tags_ids = house.tags.values_list('id', flat=True)
    similar_houses = House.openhouse.filter(tags__in=house_tags_ids).exclude(id=house.id)
    similar_houses = similar_houses.annotate(same_tags=Count('tags')).order_by('-same_tags','-created')[:4]
    '''
    context = {'hostel': hostel, 'section':'hostels' }
    return render(request, 'hostel/hostel_detail.html', context)

'''
@ajax_required
@login_required
@require_POST
def house_like(request):
    house_id = request.POST.get('id')
    action = request.POST.get('action')
    if house_id and action:
        try:
            house = House.objects.get(id=house_id)
            if action == 'like':
                house.users_like.add(request.user)
            else:
                house.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})
'''