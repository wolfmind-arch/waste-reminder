# Cyclus API Documentation

This project communicates with the Cyclus REST API to retrieve upcoming waste collection dates.

The API consists of two HTTP GET endpoints.

---

# Endpoint 1 – Get BAG ID

## Description

Retrieves address information and the BAG (Basisregistratie Adressen en Gebouwen) identifier.

The BAG ID is required for the second API request.

---

## HTTP Method

```text
GET
```

---

## URL

```text
https://cyclusnv.nl/adressen/{postcode}:{house_number}
```

Example:

```text
https://cyclusnv.nl/adressen/2861XC:10
```

---

## Request Parameters

| Parameter    | Type    | Description    |
| ------------ | ------- | -------------- |
| postcode     | string  | Dutch postcode |
| house_number | integer | House number   |

---

## Response

Returns a JSON array containing one address object.

Example:

```json
[
    {
        "bagid": "0491200001322380",
        "postcode": "2861XC",
        "huisnummer": 10,
        "huisletter": "",
        "toevoeging": "",
        "description": "Schoolstraat 10, 2861XC Bergambacht",
        "straat": "Schoolstraat",
        "woonplaats": "Bergambacht",
        "woonplaatsId": 2365,
        "gemeenteId": 1931,
        "latitude": 51.934694,
        "longitude": 4.786302
    }
]
```

---

## Required Response Fields

| Field       | Description            |
| ----------- | ---------------------- |
| bagid       | BAG identifier         |
| postcode    | Postal code            |
| huisnummer  | House number           |
| description | Human-readable address |

---

## Output

The application only needs:

```text
bagid
```

The remaining fields are currently ignored.

---

# Endpoint 2 – Get Waste Collection Schedule

## Description

Retrieves all waste collection information for a specific BAG ID.

---

## HTTP Method

```text
GET
```

---

## URL

```text
https://cyclusnv.nl/rest/adressen/{bagid}/afvalstromen
```

Example:

```text
https://cyclusnv.nl/rest/adressen/0491200001322380/afvalstromen
```

---

## Request Parameters

| Parameter | Type   | Description    |
| --------- | ------ | -------------- |
| bagid     | string | BAG identifier |

---

## Response

Returns a JSON array.

Each element represents one waste stream.

Example:

```json
{
    "id": 14,
    "parent_id": 0,
    "title": "Plastic, metaal en drankenkartons",
    "slug": "",
    "tags": null,
    "page_title": "Plastic, metaal en drankenkartons",
    "content": "...",
    "ophaaldatum": "2026-06-29"
}
```

---

## Available Fields

| Field       | Description        |
| ----------- | ------------------ |
| id          | Waste stream ID    |
| parent_id   | Parent category ID |
| title       | Waste type         |
| slug        | URL slug           |
| tags        | Optional tags      |
| page_title  | Display title      |
| content     | HTML description   |
| ophaaldatum | Collection date    |

---

## Required Response Fields

The application only requires:

| Field       | Purpose         |
| ----------- | --------------- |
| title       | Waste type      |
| ophaaldatum | Collection date |

All other fields are ignored.

---

# Filtering Rules

Only keep records where:

```text
ophaaldatum != null
```

Reason:

Records with a `null` collection date contain general information rather than an upcoming waste collection event.

Example:

```json
{
    "title": "GFT Krimpenerwaard",
    "ophaaldatum": null
}
```

This record should be ignored.

---

# Processing Pipeline

```text
Address
    │
    ▼
GET /adressen/{postcode}:{house_number}
    │
    ▼
Extract BAG ID
    │
    ▼
GET /rest/adressen/{bagid}/afvalstromen
    │
    ▼
Filter:
ophaaldatum != null
    │
    ▼
Extract:
- title
- ophaaldatum
    │
    ▼
Create WasteCollection objects
    │
    ▼
Sort by collection date
    │
    ▼
Display schedule
```

---

# Notes

Current implementation assumptions:

* Both endpoints use the HTTP GET method.
* The first endpoint always returns one address.
* The second endpoint may return multiple waste streams.
* Not every waste stream has a collection date.
* The application ignores all records where `ophaaldatum` is `null`.
* The application displays only the waste type (`title`) and collection date (`ophaaldatum`).
