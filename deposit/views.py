from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import View, ListView, FormView, DetailView
from django.urls import reverse_lazy
from deposit.models import Deposit
from deposit.forms import DepositForm


class DepositListView(ListView):

    model = Deposit
    template_name = 'deposit_list.html'


class DepositDetailView(DetailView):

    model = Deposit
    template_name = 'deposit_detail.html'


class AddDepositView(FormView):

    form_class = DepositForm
    template_name = 'add_form.html'
    success_url = reverse_lazy('deposit-list')

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)
        return response


class FilterByInterestView(View):

    def get(self, request):

        return render(
            template_name='filter_by_interest.html',
            request=request,
        )

    def post(self, request):

        interest = request.POST['interest']
        deposits = Deposit.objects.filter(interest=interest)

        context = {
            'deposit_list': deposits
        }

        return render(
            template_name='deposit_list.html',
            request=request,
            context=context,
        )


class FilterByRate(View):

    def get(self, request):

        return render(
            template_name='filter_by_rate.html',
            request=request,
        )

    def post(self, request):

        rate = request.POST['rate']
        deposits = Deposit.objects.filter(rate=rate)

        context = {
            'object_list': deposits
        }

        return render(
            template_name='filter_by_rate.html',
            request=request,
            context=context,
        )


class FilterByTerm(View):

    def get(self, request):

        return render(
            template_name='filter_by_term.html',
            request=request,
        )

    def post(self, request):

        rate = request.POST['term']
        deposits = Deposit.objects.filter(term=term)

        context = {
            'object_list': deposits
        }

        return render(
            template_name='filter_by_term.html',
            request=request,
            context=context,
        )


# Create your views here.
