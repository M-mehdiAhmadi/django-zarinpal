import json
import requests
from django.conf import settings
from django.http import HttpRequest


class Zarinpal:
    def __init__(self, request: HttpRequest, amount, description, mobile=None, email=None) -> None:
        self.merchant_id = settings.ZARINPAL_MERCHANT_ID
        self.amount = amount
        self.description = description
        self.callback_url = request.build_absolute_uri(settings.ZARINPAL_CALLBACK_URL)
        self.mobile = mobile
        self.email = email

    def send_request(self) -> dict:
        """
        Send payment request to Zarinpal.
        Returns JSON response dict.
        """
        payload = {
            "merchant_id": self.merchant_id,
            "amount": self.amount,
            "description": self.description,
            "callback_url": self.callback_url,
            "metadata": {}
        }

        if self.mobile:
            payload["metadata"]["mobile"] = self.mobile
        if self.email:
            payload["metadata"]["email"] = self.email

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        try:
            response = requests.post(
                settings.ZARINPAL_API_REQUEST_URL,
                data=json.dumps(payload),
                headers=headers,
                timeout=10  # add a timeout for safety
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}
