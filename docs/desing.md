# Waste Reminder – Design Notes

## main.py

Coordinates the application.

Responsibilities:
- load configuration
- call the API module
- create waste collection objects
- send data to the display module
- handle basic errors

## api/cyclus.py

Talks to the Cyclus API.

Functions:
- `get_bag_id(postcode, house_number)`
  - Gets BAG ID for the address.

- `get_waste_schedule(bag_id)`
  - Gets raw waste collection data from Cyclus.

## models/waste.py

Represents waste collection data.

Possible model:
- `WasteCollection`
  - name
  - collection_date

## display/terminal.py

Shows results in the terminal.

Functions:
- `show_schedule(collections)`
  - Prints upcoming waste collection dates.


