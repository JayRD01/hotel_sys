from packages import (
    Customer,
    CustomerManagement,
    Room,
    RoomManagement,
    Reservation,
    ReservationsSys,
    Payments,
)
import asyncio


async def main():
    # Inicializar sistemas
    customer_mgmt = CustomerManagement()
    room_mgmt = RoomManagement()
    reservation_system = ReservationsSys()
    payment_processor = Payments()

    # Crear clientes
    customer1 = Customer(id_customer=1, name="Alice", email="alice@example.com")
    customer2 = Customer(id_customer=2, name="Bob", email="bob@example.com")

    # Agregar clientes al sistema
    print(customer_mgmt.add_customer(customer1))
    print(customer_mgmt.add_customer(customer2))

    # Crear habitaciones
    room_mgmt.add_room(Room(101, "Single", 100))
    room_mgmt.add_room(Room(102, "Double", 150))

    # Verificar disponibilidad y hacer una reserva
    if room_mgmt.check_availability(101):
        reservation = Reservation(
            id_reservation=1,  # Corregido de reservation_id a id_reservation
            customer_name="Alice",
            room_number=101,
            check_in="2025-01-01",
            check_out="2025-01-05",
        )
        print(reservation_system.add_in(reservation))

        # Procesar el pago
        await payment_processor.process_payment("Alice", 100)

    if room_mgmt.check_availability(102):
        reservation = Reservation(
            id_reservation=2,  # Corregido de reservation_id a id_reservation
            customer_name="Bob",
            room_number=102,
            check_in="2025-01-02",
            check_out="2025-01-06",
        )
        print(reservation_system.add_in(reservation))

        # Procesar el pago
        await payment_processor.process_payment("Bob", 150)

    # Listar clientes registrados
    print("\nClientes registrados:")
    for info in customer_mgmt.customers.values():
        print(info)

    # Listar habitaciones registradas
    print("\nHabitaciones registradas:")
    print(room_mgmt.list_rooms())  # Uso del método correcto

    # Listar pagos procesados
    print("\nPagos procesados:")
    print(payment_processor.list_payments())

    # Cancelar una reserva
    print(reservation_system.cancel(reservation))

    # Listar reservas actuales
    print("\nReservas actuales:")
    for room, reservations in reservation_system.reservated.items():
        for res in reservations:
            print(f"ID Reservación: {res.id_reservation}, Cliente: {res.customer_name}, Habitación: {res.room_number}")


if __name__ == "__main__":
    asyncio.run(main())
