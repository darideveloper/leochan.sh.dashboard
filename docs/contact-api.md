# Contact API Endpoint

This document provides instructions on how to use the contact form API endpoint.

## Endpoint

-   **URL**: `/api/contact/`
-   **Method**: `POST`
-   **Permissions**: `AllowAny` (publicly accessible)

## Request Body

The request body must be a JSON object with the following fields:

| Field     | Type   | Description              | Required |
| --------- | ------ | ------------------------ | -------- |
| `name`    | String | The name of the sender.  | Yes      |
| `email`   | String | The email of the sender. | Yes      |
| `message` | String | The message content.     | Yes      |

### Example Request Body

```json
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "message": "Hello, I would like to get in touch with you."
}
```

## Response

### Successful Response

-   **Status Code**: `201 Created`
-   **Body**: A JSON object representing the created message.

#### Example Successful Response Body

```json
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "message": "Hello, I would like to get in touch with you.",
    "created_at": "2026-04-01T23:10:22.995852-06:00"
}
```

### Error Response

-   **Status Code**: `400 Bad Request`
-   **Body**: A JSON object with error details.

#### Example Error Response Body

```json
{
    "email": [
        "Enter a valid email address."
    ],
    "message": [
        "This field may not be blank."
    ]
}
```

## `curl` Example

```bash
curl -X POST 
  http://127.0.0.1:8000/api/contact/ 
  -H 'Content-Type: application/json' 
  -d '{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "message": "Hello, I would like to get in touch with you."
}'
```
