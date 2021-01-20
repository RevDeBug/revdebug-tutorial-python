from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@csrf_exempt
def index(order):
    data = json.loads(order.body)
    total = 0
    invoice = ""
    orderDetailsArray = data['OrderDetails']
    for no in range(len(orderDetailsArray)):
        print(orderDetailsArray[no])
        orderDetails=orderDetailsArray[no]
        print(orderDetails['Discount'])
        discount = orderDetails['Discount']
        if discount > 100:
            continue

        if no == 0:
            invoice = "Invoice number " + data['OrderId'] + " for " + data['Customer']['CompanyName'] + "\n"

        print(invoice)




    print ('Raw Data: "%s"' % orderDetailsArray)
    return HttpResponse("Hello, world. You're at the polls index.")
