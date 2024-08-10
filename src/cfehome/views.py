import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent
def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = 'My page'
    html_template = 'home.html'
    my_context = {
        'page_title': my_title,
        'page_visit_count': page_qs.count(),
        'total_visit_count': qs.count()
    }
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)



def old_home_page_view(request, *args, **kwargs):
    my_title = 'My page'
    my_content = {
        'page_title': my_title
    }
    html = ''
    html_file_path = this_dir / 'home.html'
    html = html_file_path.read_text()
    html = html.format(**my_content)
    return HttpResponse(html)
