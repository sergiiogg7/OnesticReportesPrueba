import pandas as pd

class Reports:

    def __init__(self,productscsv,orderscsv,customerscsv):
        self.products  = pd.read_csv(productscsv)
        self.orders = pd.read_csv(orderscsv)
        self.customers = pd.read_csv(customerscsv)

    def createReport1(self):
        """
            Reporte 1
            El equipo de ventas quiere saber el total de cada pedido. Debe generar un fichero llamado “order_prices.csv” con las siguientes columnas: 
                id: ID del pedido
                total: Total del pedido en euros
        """
        productCost = self.products["cost"] 
        order_prices = pd.DataFrame(columns=["id","total"]) 

        for i, row in self.orders.iterrows():
            id = row[0] # id de la fila i
            productsOrderList = row[2] # lista de productos de la fila i
            productsOrderList = [int(x) for x in productsOrderList.split(" ")] # Convierto de string a lista de int
            totalCost = 0
            # Hago el sumatorio del precio de cpytbhada producto de la orden en totalCost y inserto en el DataFrame
            for i in productsOrderList:
                totalCost += productCost[i]
            order_prices.loc[id] = [id,totalCost] 
            
        return order_prices

    def createReport2(self):
        """
            Reporte 2
            El equipo de marketing quiere saber que clientes han comprado cada producto. 
            Debe generar un fichero llamado “product_customers.csv” con las siguientes columnas: 
                    id: ID del producto
                    customer_ids: Lista de todos los ID's que han comprado ese producto (Separados por un espacio)
        """
        productCost = self.products["cost"]
        productCustomers = {} # Diccionario con entrada: id del producto y valor lista de IDs de los customers que lo han comprado
        pCustomers = pd.DataFrame(columns=["id","customer_ids"])
        
        # Inicializacion de cada entrada a lista vacia
        for id in range(0,len(productCost)):
            productCustomers[id] = []

        for indexOrder, row in self.orders.iterrows():
            customer = row[1] # customer de la orden i
            productsOrderList = row[2] # lista de productos de la orden i
            productsOrderList = [int(x) for x in productsOrderList.split(" ")] #Convierto de string a lista de int
            # Inserto el ID del customer a la lista de IDs de customers de los productos que ha comprado
            for p in productsOrderList:
                productCustomers[p].append(customer)
            
        for productId in productCustomers:
            productCustomers[productId] = list(set(productCustomers[productId])) # Elimino clientes repetidos que han comprado un producto
            aux = " ".join(map(str, productCustomers[productId])) # Convierto de Lista de enteros a un string separado por caracteres en blanco
            pCustomers.loc[productId] = [productId,aux] # Inserto la fila [productId, customer_ids] en el DataFrame
        
        return pCustomers

    def createReport3(self): 
        """
            Reporte 1
            Para evaluar a los clientes, necesitamos un fichero que contenga todos los pedidos ordenados descendentemente por el total en euros:
            Debe generar un fichero llamado “customer_ranking.csv" con las siguientes columnas: 
                id: ID del cliente
                name: Nombre del cliente
                lastname: Apellidos del cliente
                total: Total en euros que el cliente ha comprado en productos.
            Las columnas deben ir correctamente identificadas con el nombre de cada columna en la primera fila de los ficheros.
        """
        customerRanking = pd.DataFrame(columns=["id","name","lastname", "total"]) 
        productCost = self.products["cost"]

        for indexCustumer, row in self.customers.iterrows():
            clientId = row[0] # id del Cliente
            clientName = row[1] # nombre del Cliente
            clientLastName = row[2] # apellidos del Cliente
            ordersFromCustomer = self.orders[self.orders["customer"] == indexCustumer] #Ordenes realizadas por el cliente con id igual a i
            totalCost = 0
            for indexOrder, row in ordersFromCustomer.iterrows():
                productsOrderList = row[2] # Obtengo la lista de productos de la orden i
                productsOrderList = [int(x) for x in productsOrderList.split(" ")] # Convierto de string a lista de int
                totalCost += sum(productCost[productId] for productId in productsOrderList) # Sumatorio del coste de todos los productos de la orden
            customerRanking.loc[clientId] = [clientId, clientName, clientLastName, totalCost]

        return customerRanking