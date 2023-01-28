from django.shortcuts import render
from django.http import HttpResponse
from PruebaTecnica.Classes.reports import Reports
import zipfile

def uploadfiles(request):

    return render(request, "uploadcsv.html")

def downloadfiles(request):

    productscsv = request.FILES['file1']
    orderscsv = request.FILES['file2']
    customerscsv = request.FILES['file3']

    reports = Reports(productscsv, orderscsv, customerscsv)

    report1 = reports.createReport1().to_csv()
    report2 = reports.createReport2().to_csv()
    report3 = reports.createReport3().to_csv()

    #Respuesta HTTP descargable 
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="reports.zip"'

    # Crea el archivo zip
    with zipfile.ZipFile(response, mode='w') as zf:
        zf.writestr("order_prices.csv", report1)
        zf.writestr("products_customers.csv", report2)
        zf.writestr("customer_ranking.csv", report3)
 
    return response

