from django.shortcuts import render, redirect #redirect, метод для переадресации
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

#Order_by это сортировка по какому-то признаку, если не нужна, то .all, для обратного порядка ставим перед -title. Date, сортировка по дате.
def news_home(request):
    news = Articles.objects.order_by('title')#[:2]Срез 
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_views.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid(): #метод позволяет проверить, корректно ли заполнены введенные данные.
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена не верно'
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)
