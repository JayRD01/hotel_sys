class Customer: #Aqui se gestiona la parte de los datos
    def __init__(self, id_customer, name, email):
        self.id_customer = id_customer
        self.name = name
        self.email = email

    def __str__(self):
        return f'ID: {self.id_customer}, Nombre: {self.name}, Email: {self.email}'

class CustomerManagement: #Aqui se establece la logica del sistema de gestion
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        try:
            # Verificar si el ID ya existe en el diccionario
            if customer.id_customer in self.customers:
                raise ValueError(f"El ID {customer.id_customer} ya se encuentra registrado, intenta nuevamente.")
            
            # Agregar el cliente al diccionario
            self.customers[customer.id_customer] = customer
            return f"El cliente {customer.id_customer} fue agregado exitosamente."

        except ValueError as e:
            # Manejo del error y retorno del mensaje
            return f"Error: {e}"

    def info(self, custo_id):
        finder = self.customers.get(custo_id)
        if finder:
            return custo_id
        else:
            return custo_id
        
    def updater(self, customer_id, name=None, email=None):
        try:
            # Validación: name y email no pueden ser ambos None
            if name is None and email is None:
                raise ValueError("Debes modificar Name y/o Email, para poder actualizar correctamente.")
            
            # Buscar al cliente
            customer = self.customers.get(customer_id)
            if not customer:
                raise ValueError(f"Cliente con ID {customer_id} no encontrado.")
            
            # Actualizar los campos proporcionados
            if name:
                customer.name = name
            if email:
                customer.email = email

            # Confirmación de la actualización
            return f"Cliente {customer_id} actualizado con éxito."

        except ValueError as e:
            # Manejo del error directamente dentro del método
            return f"Error: {e}"

            

        