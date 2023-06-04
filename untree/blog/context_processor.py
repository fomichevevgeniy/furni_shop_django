from .forms import SubscriptionForm

def add_my_forms(request):
    return {
        'sub_form': SubscriptionForm()
    }