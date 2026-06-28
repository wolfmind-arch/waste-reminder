# Waste Reminder – Project Roadmap

## Project Vision

Create a standalone Raspberry Pi device that automatically displays upcoming waste collection dates using data from the Cyclus API.

The application should boot automatically, require no user interaction, and run as a background service.

---

# Current Status

* [x] Project structure created
* [x] Git repository initialized
* [x] API endpoints identified
* [x] API documented
* [x] Software architecture designed
* [ ] Configuration system implemented
* [ ] Python API client implemented
* [ ] Waste model implemented
* [ ] Display manager implemented
* [ ] TFT display support
* [ ] Systemd service
* [ ] Automatic startup

---

# Milestone 1 – Foundation

* [x] Create config.json
* [ ] Read configuration
* [ ] Logging
* [ ] Error handling

---

# Milestone 2 – API

* [ ] Get BAG ID
* [ ] Download waste schedule
* [ ] Validate HTTP responses
* [ ] Parse JSON

---

# Milestone 3 – Models

* [ ] WasteCollection class
* [ ] Convert JSON into objects
* [ ] Sort by collection date

---

# Milestone 4 – Terminal Output

* [ ] Display schedule in terminal
* [ ] Improve formatting

---

# Milestone 5 – TFT Display

* [ ] Initialize SPI display
* [ ] Draw text
* [ ] Draw icons
* [ ] Automatic refresh

---

# Milestone 6 – Raspberry Pi Deployment

* [ ] systemd service
* [ ] Auto start
* [ ] Logging
* [ ] Recovery after reboot

---

# Future Ideas

* Weather forecast
* Clock
* Wi-Fi signal strength
* Web configuration page
* OTA updates
* Multiple API providers
* Multiple display drivers
* Dark mode
* Garbage icons
* Notifications
