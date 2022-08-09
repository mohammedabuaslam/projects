from django.shortcuts import render, get_object_or_404
from .models import blog
from django.views.generic import (
    ListView
)

from django.http import Http404

def bloghome(request):
	return render(request, 'blog/bloghome.html',{'title':'Blogs'})

class blogcategory(ListView):
    model = blog
    template_name = 'blog/blogcategory.html'
    context_object_name = 'posts'
    paginate_by = 12

    def get_queryset(self):
        return blog.objects.filter(niche=self.kwargs.get('categories')).order_by('-date_posted')

class blogdetail(ListView):
    model = blog
    template_name = 'blog/blog-detailed.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        res = get_object_or_404(blog, url=self.kwargs.get('url'))
        return blog.objects.filter(url=self.kwargs.get('url'))

    def get_context_data(self, **kwargs):
        context = super(blogdetail, self).get_context_data(**kwargs)
        train = blog.objects.filter(url=self.kwargs.get('url'))
        context['title'] = 'Blog - ' + str(train[0])
        return context