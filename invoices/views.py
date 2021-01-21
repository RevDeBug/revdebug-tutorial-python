from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import os
import requests

@csrf_exempt
def index(order):
    data = json.loads(order.body)
    total = 0
    invoice = ""
    orderDetailsArray = data['OrderDetails']
    for no in range(len(orderDetailsArray)):
        orderDetails=orderDetailsArray[no]
        discount = orderDetails['Discount']

        if discount > 100:
            continue

        if no == 0:
            invoice = "Invoice number " + data['OrderId'] + " for " + data['Customer']['CompanyName'] + "\n"

    resourceUrl = os.environ['InvoicesSenderAddress'] + "/Sender/Send?invoice=" + invoice
    requests.get(resourceUrl)

    return HttpResponse("OK")
