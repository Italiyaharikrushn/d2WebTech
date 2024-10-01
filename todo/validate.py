from .models import Todo
permission_required = 'clients.delete_csn'

# model = CSN
# form_class = CSNForm
template_name = 'generic_delete.html'
success_message = "deleted successfully."

def get_context_data(self, **kwargs):
        context = super(self).get_context_data(**kwargs)
        client_id = self.kwargs['client_id']
        context['c_id'] = client_id
        context['client_full_name'] = Todo.objects.get(id=client_id)
        return context

def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messagebox.success(self.request, self.success_message % obj.__dict__)
        return super(self).delete(request, *args, **kwargs)

def get_success_url(self):
        return reversed('clients:detail', args=[str(self.object.client.pk)])