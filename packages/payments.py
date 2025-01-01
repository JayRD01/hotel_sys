import asyncio
import random

class Payments:
    def __init__(self):
        self.pays = []

    async def process_payment(self, customer_name, amount):
        if amount <= 0:
            raise ValueError("Estas loco? cómo vas a pagar con esa cantidad, intenta de nuevo.")

        print(f'Procesando el pago del cliente {customer_name}')
        await asyncio.sleep(random.randint(1, 6))
        print('Pago ha sido procesado')
        self.pays.append({'customer_name': customer_name, 'amount': amount})

    async def process_multiple_payments(self, payments_list):
        if not payments_list:
            raise ValueError('No puede enviar lista de pagos vacía')

        tasks = [
            self.process_payment(customer_name, amount)
            for customer_name, amount in payments_list
        ]
        await asyncio.gather(*tasks)

    def list_payments(self):
        if not self.pays:
            return 'No existen pagos procesados'

        return [
            f"Cliente: {payment['customer_name']}, Monto: ${payment['amount']}"
            for payment in self.pays
        ]

async def main():
    processor = Payments()

    # Procesar un solo pago
    await processor.process_payment("Alice", 100)

    # Procesar múltiples pagos
    payment_list = [("Bob", 200), ("Charlie", 300)]
    await processor.process_multiple_payments(payment_list)

    # Listar pagos procesados
    print("\nPagos procesados:")
    print(processor.list_payments())

# Ejecutar el programa
asyncio.run(main())
