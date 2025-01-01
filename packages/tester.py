from customers import Customer, CustomerManagement

if __name__ == "__main__":
    test1 = Customer(1, 'Duarte', 'example@example.com')
    test2 = CustomerManagement()

    # Agregar cliente
    print(test2.add_customer(test1))

    print(test2.info(test1))

    print(test2.updater(1,'Darlyn','exampl@ex.com'))
    print(test2.info(test1))