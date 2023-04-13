from django.urls import path
from .views import (RitualDetailView, RitualListView, RitualCreateView, 
                    RitualUpdateView, RitualDeleteView, StepCreateView, 
                    StepUpdateView, StepDeleteView, mark_step_complete, 
                    mark_step_incomplete)

app_name = 'myapp'

urlpatterns = [
    path('rituals/', RitualListView.as_view(), name='ritual_list'),
    path('ritual/detail/', RitualDetailView.as_view(), name='ritual_detail'),
    path('ritual/create/', RitualCreateView.as_view(), name='ritual_create'),
    path('ritual/<int:pk>/update/', RitualUpdateView.as_view(), name='ritual_update'),
    path('ritual/<int:pk>/delete/', RitualDeleteView.as_view(), name='ritual_delete'),
    path('ritual/<int:pk>/step/new/', StepCreateView.as_view(), name='step_create'),
    path('ritual/<int:pk>/step/update/', StepUpdateView.as_view(), name='step_update'),
    path('ritual/<int:pk>/step/delete/', StepDeleteView.as_view(), name='step_delete'),
    path('ritual/step/<int:pk>/step/complete/', mark_step_complete, name='mark_step_complete'),
    path('ritual/step/<int:pk>/step/incomplete/', mark_step_incomplete, name='mark_step_incomplete'),
]