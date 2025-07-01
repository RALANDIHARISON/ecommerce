from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from store.models import Order, Customer, Product, OrderItem, ShippingAddress


class ManagerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

   def test_func(self):

        return self.request.user.groups.filter(name='Store Managers').exists()



class OrderListView(ManagerRequiredMixin, ListView):

    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    ordering = ['-date_ordered']



class OrderDetailView(ManagerRequiredMixin, DetailView):

    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['order_items'] = self.object.orderitem_set.all()

        context['shipping_addresses'] = self.object.shippingaddress_set.all()
        return context