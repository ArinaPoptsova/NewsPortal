from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from news.models import Author
from profiles.models import Profile
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


class CreateProfileView(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'profiles/edit_profile.html'
    success_url = '../../../news/'
    fields = ['avatar', 'about']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='author').exists()
        return context


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profiles/edit_profile.html'
    success_url = '../../../news/'
    fields = ['avatar', 'about']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.request.user.username
        context['is_not_author'] = not self.request.user.groups.filter(name='author').exists()
        return context

    def get_object(self):
        return Profile.objects.get(user__pk=self.request.user.pk)


@login_required
def upgrade_me(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)
        Author.objects.create(user=user, user_rating=0)
    return redirect('/news/')
