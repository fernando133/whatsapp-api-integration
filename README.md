# Intruction

## Prerequisites

Have Docker and Docker Compose installed on the machine or server.

First of all you shoud copy *.env.sample files in /env directory to *.env and configure with the necessary informations.

The infos to integrate with GraphApi are in whatsapp.env. 
In BEARER_TOKEN you don't need to explicit Bearer, only the token like:
BEARER_TOKEN=Ea912kdjsdkaçlsaldjfa...

The infos are:
<br>
WHATSAPP-BUSINESS-ACCOUNT-ID=XXXXXXXXXXX
<br>
NUMBER_ID=XXXXXXXXXXXXXXXXXXXXXXXXXX
<br>
BEARER_TOKEN=EAAImXXXXXXXXXXXXXXXXXXXXXXXXXXXX
<br>


## Then run 
In root folder of project run: ```docker-compose up --build -d```

## Migrates

If necessary you can run this commands, but migrates are in version control and in all first run the migrate command is run by default. This configurantion is in the docker-compose.yml file.

```docker-compose exec app ./manage.py makemigrations```\
```docker-compose exec app ./manage.py migrate```

### Superuser
For access in admin control panel.
```docker-compose exec app ./manage.py createsuperuser```

### Acess
```http://localhost:8000```\
```http://localhost:8000/admin```

### Create Consumer Systems in Admin
You have to create consumer system in admin to start send messages.

# Webhook configuration
With the docker containers running into port 8000, you can use the ngrok to expose the webook into the internet.
<br>
More information about ngrok: https://ngrok.com/
<br>
And in your developer.facebook.com account configure the webhook to:
https://<ngrok_address>/webhook/

Obs.: Don't forget the end slash.

Here is the oficial documentation about configure webhook in GraphApi:
<br>
https://developers.facebook.com/docs/whatsapp/cloud-api/get-started#configure-webhooks


# API Endpoints Documentation

## Sending a message in real time.
#### POST /messages/

```json
{
    "to": "5562982769980",
    "message_body": "Ok, sending...",
    "send_now": true,
    "date_to_send": null,
    "consumer_system": "fcfa7b2a-c429-4fa5-81f9-37e988968e20"
}
```
#### Response
#### HTTP 200 OK
```json
{
    "id": "7641cd6a-21e6-4d84-9fcc-a7106193a470",
    "to": "5562982769980",
    "message_body": "Ok, sending...",
    "send_now": true,
    "date_to_send": null,
    "created_at": "2022-10-02T21:19:33.038118",
    "consumer_system": "fcfa7b2a-c429-4fa5-81f9-37e988968e20"
}
```
## Scheduling a message to specific date.
```json
{
    "to": "5562982769980",
    "message_body": "Ok, sending...",
    "send_now": false,
    "date_to_send": 2022-10-02,
    "consumer_system": "fcfa7b2a-c429-4fa5-81f9-37e988968e20"
}
```

#### Response
#### HTTP 200 OK
```json
{
    "id": "7641cd6a-21e6-4d84-9fcc-a7106193a470",
    "to": "5562982769980",
    "message_body": "Ok, sending...",
    "send_now": false,
    "date_to_send": 2022-10-02,
    "created_at": "2022-10-02T21:19:33.038118",
    "consumer_system": "fcfa7b2a-c429-4fa5-81f9-37e988968e20"
}
```

## Getting all messages
#### GET /messages/
<br>
return a list of all messages of all consumer systems. 

```json
[
{
        "id": "28139f58-8c5d-4617-9384-2ed6f66a7b82",
        "to": "5562982759963",
        "message_body": "Tese webhook",
        "send_now": true,
        "date_to_send": null,
        "was_sent": true,
        "is_canceled": false,
        "api_return": "{'messaging_product': 'whatsapp', 'contacts': [{'input': '5562982759963', 'wa_id': '556282759963'}], 'messages': [{'id': 'wamid.HBgMNTU2MjgyNzU5OTYzFQIAERgSRkUwMjdGQTg1MTVEMzc2QjUzAA=='}]}",
        "created_at": "2022-10-01T21:26:13.421146",
        "consumer_system": "fcfa7b2a-c429-4fa5-81f9-37e988968e20"
    }
]
```

## Getting all messages of an specific consumer system
#### GET /messages/?consumer_system=fcfa7b2a-c429-4fa5-81f9-37e988968e20

#### Response
#### HTTP 200 OK
```json
[
    {
        "id": "fd1cee2a-8a0f-4838-8831-8c200bfba3b2",
        "to": "5562982759963",
        "message_body": "Testing scheduled message...",
        "send_now": false,
        "date_to_send": "2022-10-02",
        "was_sent": true,
        "is_canceled": false,
        "api_return": "{'messaging_product': 'whatsapp', 'contacts': [{'input': '5562982759963', 'wa_id': '556282759963'}], 'messages': [{'id': 'wamid.HBgMNTU2MjgyNzU5OTYzFQIAERgSQkNGMEJCQUZDQTI2REJDOEJCAA=='}]}",
        "created_at": "2022-10-02T21:22:27.632012",
        "consumer_system": "fcfa7b2a-c429-4fa5-81f9-37e988968e20"
    },
    {
        "id": "7641cd6a-21e6-4d84-9fcc-a7106193a470",
        "to": "5562982759963",
        "message_body": "Teste",
        "send_now": true,
        "date_to_send": null,
        "was_sent": true,
        "is_canceled": false,
        "api_return": "{'messaging_product': 'whatsapp', 'contacts': [{'input': '5562982759963', 'wa_id': '556282759963'}], 'messages': [{'id': 'wamid.HBgMNTU2MjgyNzU5OTYzFQIAERgSQjAzMkRBRDE4RDdGRDNBODdFAA=='}]}",
        "created_at": "2022-10-02T21:19:33.038118",
        "consumer_system": "fcfa7b2a-c429-4fa5-81f9-37e988968e20"
    }
]
```
## Canceling a scheduled message
#### PUT /messages/{message-uuid}/cancel


#### Response
#### HTTP 200 OK

```json
{
    "id": "fc01e22b-cec3-420a-b08f-c5fc41fc5670",
    "to": "5562982759963",
    "message_body": "Canceling messages...",
    "send_now": false,
    "date_to_send": "2022-10-05",
    "was_sent": false,
    "is_canceled": true,
    "api_return": null,
    "created_at": "2022-10-02T21:40:58.017029",
    "consumer_system": "fcfa7b2a-c429-4fa5-81f9-37e988968e20"
}
```


# Code verification (Optional)

### Install
```apt-get install pre-commit```

In project directory:
```pre-commit install```

### Run hooks of pre-commit in all files
```pre-commit run --all-files```

# Useful Information

### Useful commands for docke
https://www.codenotary.com/blog/extremely-useful-docker-commands/

### Gitflow process
https://medium.com/trainingcenter/utilizando-o-fluxo-git-flow-e63d5e0d5e04
