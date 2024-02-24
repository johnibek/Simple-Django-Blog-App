from django.shortcuts import render
from django.views import generic
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

class PostListView(generic.ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("posts:detail", kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields['title'].widget.attrs['class'] = 'form-control'
        form.fields['title'].widget.attrs['placeholder'] = 'Title'
        form.fields['title'].label = ''

        form.fields['body'].widget.attrs['class'] = 'form-control'
        form.fields['body'].widget.attrs['placeholder'] = 'Body'
        form.fields['body'].label = ''

        return form


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    template_name = 'update.html'
    context_object_name = 'post'
    fields = ['title', 'body']

    def test_func(self):
        post_object = self.get_object()
        user = self.request.user
        if user == post_object.author:
            return True
        else:
            return False

    def get_success_url(self):
        return reverse_lazy("posts:detail", kwargs={'pk': self.object.pk})
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        form.fields['title'].widget.attrs['class'] = 'form-control'
        form.fields['title'].label = ''
        form.fields['title'].widget.attrs['placeholder'] = 'Title'

        form.fields['body'].widget.attrs['class'] = 'form-control'
        form.fields['body'].label = ''
        form.fields['body'].widget.attrs['placeholder'] = 'Body'

        return form
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = 'delete.html'
    context_object_name = 'post'

    success_url = '/'

    def test_func(self):
        post_object = self.get_object()
        user = self.request.user
        if user == post_object.author:
            return True
        else:
            return False
        