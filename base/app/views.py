from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from app.models import Ritual, Step
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from app.models import Ritual, Step
from app.forms import RitualStepForm
from django.http import Http404

# View list of rituals
class RitualListView(ListView):
    model = Ritual
    template_name = 'ritual_list.html'

# detail view of ritual
class RitualDetailView(DetailView):
    model = Ritual
    template_name = 'ritual_detail.html'

# View to create a ritual
class RitualCreateView(CreateView):
    model = Ritual
    fields = ['name', 'user']
    success_url = reverse_lazy('ritual_list')
    template_name = 'ritual_form.html'

# View to update a ritual
class RitualUpdateView(UpdateView):
    model = Ritual
    fields = ['name', 'user']
    success_url = reverse_lazy('ritual_list')
    template_name = 'ritual_form.html'

# View to delete a Ritual
class RitualDeleteView(DeleteView):
    model = Ritual
    success_url = reverse_lazy('ritual_list')
    template_name = 'ritual_confirm_delete.html'

# View to list the steps of a ritual in JSON format
def step_list(request, pk):
    ritual = get_object_or_404(Ritual, pk=pk)
    steps = ritual.steps.all().order_by('order')
    data = list(steps.values('id', 'description', 'order'))
    return JsonResponse(data, safe=False)

# View to update the order of steps in a ritual
def step_order(request):
    if request.method == 'POST':
        new_order = request.POST.getlist('order[]')
        for i, pk in enumerate(new_order):
            step = get_object_or_404(Step, pk=pk)
            step.order = i
            step.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid method'})



class StepListView(ListView):
    model = Step
    template_name = 'step_list.html'

    def get_queryset(self):
        ritual_pk = self.kwargs['pk']
        ritual = get_object_or_404(Ritual, pk=ritual_pk, user=self.request.user)
        queryset = Step.objects.filter(ritual=ritual)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ritual_pk = self.kwargs['pk']
        ritual = get_object_or_404(Ritual, pk=ritual_pk, user=self.request.user)
        context['ritual'] = ritual
        context['csrf_token'] = self.request.COOKIES['csrftoken']
        context['steps'] = Step.objects.filter(ritual=ritual)
        return context

class StepCreateView(LoginRequiredMixin, CreateView):
    model = Step
    template_name = 'step_form.html'
    form_class = RitualStepForm

    def get_form_kwargs(self):
        kwargs = super(StepCreateView, self).get_form_kwargs()
        kwargs['ritual_pk'] = self.kwargs['pk']
        return kwargs

    def form_valid(self, form):
        ritual_pk = self.kwargs['pk']
        ritual = get_object_or_404(Ritual, pk=ritual_pk, user=self.request.user)
        ritual_step = form.save(commit=False)
        ritual_step.routine = ritual
        ritual_step.save()
        return super().form_valid(form)

class StepUpdateView(LoginRequiredMixin, UpdateView):
    model = Step
    template_name = 'ritual_step_form.html'
    form_class = RitualStepForm

    def get_object(self, queryset=None):
        obj = super(StepUpdateView, self).get_object()
        if not obj.routine.user == self.request.user:
            raise Http404
        return obj

    def get_success_url(self):
        return reverse_lazy('routine_step_list', kwargs={'pk': self.object.routine.pk})

class StepDeleteView(LoginRequiredMixin, DeleteView):
    model = Step
    template_name = 'ritual_step_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super(StepDeleteView, self).get_object()
        if not obj.routine.user == self.request.user:
            raise  
        return obj

    def get_success_url(self):
        return reverse_lazy('ritual_step_list', kwargs={'pk': self.object.routine.pk})

class mark_step_complete():
    model = Step
    template_name = 'mark_step_complete.html'



class mark_step_incomplete():
    model = Step
    template_name = 'mark_step_incomplete.html'