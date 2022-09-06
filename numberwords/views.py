from numberwords.forms import NumberForm

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View


from num2words import num2words  # <-- this is why you have to love python


class NumberFormView(View):
    template_name = 'index.html'
    form_class = NumberForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return render(request, self.template_name, {'form': form, 'result': num2words(form.cleaned_data['number'])})

        return render(request, self.template_name, {'form': form})  # might be good to display error results here
