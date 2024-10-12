from .models import Catagory

def link_menu(request):
    links = Catagory.objects.all()
    return dict(links = links)