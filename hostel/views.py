from django.shortcuts import render, get_object_or_404
from .models import Hostel
from .forms import ContactForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#view for the homepage
def homepage(request):
    context = { 'section':'homepage'}
    return render(request,'hostel/homepage.html', context) 

#view for the "about page"
def about_hostelite(request):
    sent = False
    if request.method == 'POST':
        # Form was submitted
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # Form fields passed validation
            cd = contact_form.cleaned_data
            subject = 'A message from {} with contact({}) on Hostelite'.format(cd['name'], cd['email'])
            message = 'Reads: "{}" '.format(cd['message'])
            send_mail(subject, message, [cd['email']], ['admin@myblog.com'])
            sent = True
    else:
        contact_form = ContactForm()
        sent = False
    context = { 'section':'about', 'contact_form':contact_form, 'sent':sent}
    return render(request,'hostel/about.html', context) 

#the view that list all vacant hostels
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
    context = {'section':'hostels', 'hostels':hostels, 'page':page,}
    return render(request,'hostel/hostels.html', context)


#the view for a particular hostel details
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