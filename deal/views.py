from django.shortcuts import render
from django.http import HttpResponse
from deal.models import Deal, Item

# Create your views here.
def index(request):
    deals = Deal.objects.filter()
    items=[]
    for d in deals:
        item = Item.objects.filter(deal_id=d)
        items.append(item)
    print(items)
        # print(item[0].name)
    return render(request, 'deal/index.html', {"deals":deals,"items":items})
