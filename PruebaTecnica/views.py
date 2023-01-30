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

    #Creo el objeto reports
    reports = Reports(productscsv, orderscsv, customerscsv) 

    #Creo los reportes
    orderPricesReport = reports.createReport1().to_csv(index=False)
    productsCustomersReport = reports.createReport2().to_csv(index=False)
    customerRankingReport = reports.createReport3().to_csv(index=False)

    #Respuesta HTTP descargable 
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="reports.zip"'

    # Crea el archivo zip
    with zipfile.ZipFile(response, mode='w') as zf:
        zf.writestr("order_prices.csv", orderPricesReport)
        zf.writestr("products_customers.csv", productsCustomersReport)
        zf.writestr("customer_ranking.csv", customerRankingReport)
 
    return response

