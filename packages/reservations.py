from collections import defaultdict
from datetime import datetime

class Reservation:
    def __init__(self, id_reservation, room_number, customer_name, check_in, check_out):
        self.id_reservation = id_reservation
        self.room_number = room_number
        self.customer_name = customer_name
        self.check_in = check_in
        self.check_out = check_out
        self.available = True


class ReservationsSys:
    def __init__(self):
        self.reservated = defaultdict(list)

    def add_in(self, reservating):
        for room in self.reservated[reservating.room_number]:
            if room.id_reservation == reservating.id_reservation:
                return f'Esta reservacion ya fue creada, intenta nuevamente'
        
        self.reservated[reservating.room_number].append(reservating)
        return f'La reservacion numero {reservating.id_reservation} fue creada'
    
    def cancel(self, reservation):
        for keys, rooms in self.reservated.items():
            for r in rooms:
                if r.id_reservation == reservation.id_reservation:
                    rooms.remove(r)
                    return f"Su reservación fue removida de la habitación número {keys}."
        # Agregar información más legible en el mensaje de error
        return f"La reservación con ID {reservation.id_reservation} no pudo ser encontrada."


info = Reservation(100,3,"Darlyn",datetime.today(),datetime.today())
start = ReservationsSys()

print(start.add_in(info))


print(start.cancel(info))
  