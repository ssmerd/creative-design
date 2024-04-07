from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order
# from products.models import Product
# from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        
        pid = intent.id
        save_info = intent.metadata.save_info
        name = intent.metadata.name
        email = intent.metadata.email
        phone = intent.metadata.phone
        total = round(intent.amount / 100, 2)

        # Clean data in the shipping details
        # for field, value in shipping_details.address.items():
        #     if value == "":
        #         shipping_details.address[field] = None

        # Update profile information if save_info was checked
        # profile = None
        # username = intent.metadata.username
        # if username != 'AnonymousUser':
        #     profile = UserProfile.objects.get(user__username=username)
        #     if save_info:
        #         profile.default_phone_number = shipping_details.phone
        #         profile.default_country = shipping_details.address.country
        #         profile.default_postcode = shipping_details.address.postal_code
        #         profile.default_town_or_city = shipping_details.address.city
        #         profile.default_street_address1 = shipping_details.address.line1
        #         profile.default_street_address2 = shipping_details.address.line2
        #         profile.default_county = shipping_details.address.state
        #         profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    name__iexact=name,
                    email__iexact=email,
                    phone__iexact=phone,
                    total=total,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            # self._send_confirmation_email(order)
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                         'Verified order already in database'),
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    name=name,
                    # user_profile=profile,
                    email=email,
                    phone=phone,
                    stripe_pid=pid,
                )
               
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        # self._send_confirmation_email(order)
        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | SUCCESS: '
                     'Created order in webhook'),
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)