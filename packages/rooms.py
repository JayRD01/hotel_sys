class Room:
    def __init__(self, room_number, room_type, room_price):
        self.room_number = room_number  # Número de la habitación
        self.room_type = room_type      # Tipo de habitación (Single, Double, etc.)
        self.room_price = room_price    # Precio por noche
        self.available = True           # Estado de disponibilidad (por defecto: disponible)

    def __str__(self):
        return f"Número de habitación = {self.room_number}, Tipo de habitación = {self.room_type}, Precio = {self.room_price}"


class RoomManagement:
    def __init__(self):
        self.rooms = {}  # Diccionario para almacenar habitaciones {room_number: Room}

    def add_room(self, room):
        """Agrega una nueva habitación al sistema."""
        if room.room_number in self.rooms:
            raise ValueError(f"Error, la habitación {room.room_number} ya está creada.")
        self.rooms[room.room_number] = room
        print(f"La habitación {room.room_number} fue creada.")

    def check_availability(self, room_number):
        """Verifica si una habitación está disponible."""
        room = self.rooms.get(room_number)
        if not room:
            return f"La habitación {room_number} no se pudo encontrar."
        status = "DISPONIBLE" if room.available else "NO DISPONIBLE"
        return f"Habitación {room_number} está {status}."

    def update_status(self, room_number, available):
        """Actualiza el estado de disponibilidad de una habitación."""
        room = self.rooms.get(room_number)
        if not room:
            raise ValueError(f"La habitación {room_number} no fue encontrada.")
        room.available = available
        status = "DISPONIBLE" if room.available else "NO DISPONIBLE"
        return f"Habitación actualizada, ahora se encuentra: {status}."

    def list_rooms(self):
        """Devuelve una lista con todas las habitaciones registradas."""
        if not self.rooms:
            return "No hay habitaciones registradas."
        return [str(room) for room in self.rooms.values()]
