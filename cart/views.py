from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from catalogue.decorators import order_required, adress_required
from .utils import get_or_set_order, refresh_quantity
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView, RedirectView
from cart.forms import AdressForm
from cart.models import Order, Adress
import stripe



class Cart(TemplateView):
    template_name = 'pages/cart.html'


@method_decorator(order_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class Shipping(FormView):
    form_class = AdressForm
    template_name = 'pages/shipping.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save(commit=True)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('cart:shipping')

@method_decorator(adress_required, name='dispatch')
@method_decorator(login_required(login_url='/account/login'), name='dispatch')
class Payment(TemplateView):
    template_name = 'pages/payment.html'
    def post(self, request, *args, **kwargs):
        try :
            stripe.api_key = 'sk_test_51KyVnpBtHPWEuLFwI33xUlMRcm2CY0WiFvtQt7D4tY8emMBAD0kK5s9aC0z1bN3c9bqAmBGVhPwWZN8KRbdeemRC00mxdVboJC'
            YOUR_DOMAIN = 'http://localhost:8000'
            order = get_or_set_order(request)
            items = [{
                        'price_data': {
                            'currency': 'eur',
                            'unit_amount': x.product.price,
                            'product_data': {
                                'name': x.product.name,
                                'images': [x.product.img],
                            },
                        },
                        'quantity': x.quantity
                    } for x in order.orderItems.all()]
            checkout_session = stripe.checkout.Session.create(
                line_items=items,
                metadata={'order_id': order.id},
                mode='payment',
                payment_intent_data={
                    'capture_method': 'manual',
                },
                success_url=YOUR_DOMAIN + reverse('cart:success'),
                cancel_url=YOUR_DOMAIN + reverse('cart:cancel'),
            )
            order.payment_id = checkout_session.stripe_id
            order.save()
            return redirect(checkout_session.url)
        except Exception as e:
            print(str(e))
        return render(request,'pages/payment.html')


@method_decorator(csrf_exempt, name='dispatch')
class WebHook(View):
    def post(self,request):
        stripe.api_key = 'sk_test_51KyVnpBtHPWEuLFwI33xUlMRcm2CY0WiFvtQt7D4tY8emMBAD0kK5s9aC0z1bN3c9bqAmBGVhPwWZN8KRbdeemRC00mxdVboJC'
        print("enter")
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        event = None
        endpoint_secret = 'whsec_0e2e2ebe8a26f6477ae77c01f467cabb1cccb6db0f344846cab5650b33f0e561'
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(status=400)

        print(event['type'])
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            order = Order.objects.get(id=session['metadata']['order_id'])
            if order.is_valid():
                paymentIntent_id = session['payment_intent']
                intent = stripe.PaymentIntent.capture(
                    paymentIntent_id
                )
                refresh_quantity(order)
            else :
                print("stock pas disponible")
                paymentIntent_id = session['payment_intent']
                intent = stripe.PaymentIntent.capture(
                    paymentIntent_id,0
                )
                return HttpResponse(status=400)
        return HttpResponse(status=200)



@method_decorator(login_required, name='dispatch')
class SelectAdress(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        order = get_or_set_order(self.request)
        order.adress = Adress.objects.get(id=kwargs['adressId'])
        order.save()
        return reverse('cart:shipping')