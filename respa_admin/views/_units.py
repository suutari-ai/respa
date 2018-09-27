from django.views.generic import ListView

from resources.models import Unit


class UnitListView(ListView):
    model = Unit
    template_name = 'respa_admin/unit_list.html'
    context_object_name = 'units'
    paginate_by = 10
