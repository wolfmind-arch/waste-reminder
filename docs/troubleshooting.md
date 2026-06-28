# Waste Reminder – Troubleshooting Log

This document contains problems encountered during development and their solutions.

---

## 2026-06-28

### Raspberry Pi not visible on network

**Problem**

SSH connection failed.

**Cause**

Wi-Fi configuration was missing.

**Solution**

Configured Wi-Fi manually and enabled SSH.

Status:

✅ Solved

---

### Raspberry Pi Imager

**Problem**

Custom settings (Wi-Fi and user) were not written to the SD card.

**Solution**

Verified boot partition and created configuration manually.

Status:

✅ Solved

---

### Cyclus API

**Problem**

The API was undocumented.

**Solution**

Reverse engineered the endpoints using:

* Browser Developer Tools
* Network tab
* Fetch/XHR
* Postman

Status:

✅ Solved

---

### Software Architecture

**Problem**

Initially considered storing runtime data inside config.json.

**Solution**

Separated configuration from runtime data.

Configuration:

* postcode
* house number
* display settings

Runtime data:

* BAG ID
* waste schedule
* collection dates

Status:

✅ Improved design
