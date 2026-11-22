
from pathlib import Path

project_name = "bus_ticket_reservation"

folders = [
    "app",
    "app/database",
    "app/models",
    "app/schemas",
    "app/routers",
    "app/services"
]

files = [
    "app/__init__.py",
    "app/main.py",

    "app/database/__init__.py",
    "app/database/connection.py",

    "app/models/__init__.py",
    "app/models/bus.py",
    "app/models/booking.py",

    "app/schemas/__init__.py",
    "app/schemas/bus.py",
    "app/schemas/booking.py",

    "app/routers/__init__.py",
    "app/routers/bus.py",
    "app/routers/booking.py",

    "app/services/__init__.py",
    "app/services/bus.py",
    "app/services/booking.py",

    ".gitignore",
    "req.txt"
]

base_path = Path(project_name)

# Create folders
for folder in folders:
    (base_path / folder).mkdir(parents=True, exist_ok=True)

# Create empty files
for file in files:
    file_path = base_path / file
    file_path.touch(exist_ok=True)

print("Bus Ticket Reservation folder structure created successfully!")
