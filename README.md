# **MoonheimSMS**

![](./img.webp)

An asynchronous Python module for interacting with the Moonheim SMS API. The MoonheimSMS package allows for easy
integration of SMS functionalities into your Python applications, including sending SMS messages, checking message
status, and querying account balance.

## **Features**

- Asynchronous API calls
- Send SMS messages
- Check the status of sent messages
- Retrieve account balance

## **Installation**

```bash
pip install moonheimsms
```

## **Quick Start**

First, ensure you have \`**aiohttp**` installed:

```bash
pip install aiohttp
```

Then, you can start using \`**MoonheimSMS**` by importing it in your project:

```python
from moonheimsms import MoonheimSMS
```

## Usage

### Initialize the Client

```python
moonheim = MoonheimSMS(token="YOUR_API_TOKEN", proxy="YOUR_PROXY")
```

### Sending an SMS

```python
await moonheim.sendSms(
    phone="RECIPIENT_PHONE_NUMBER",
    sender_name="YOUR_SENDER_NAME",
    text="Hello, World!",
    type_=0,
    gateway=0,
    short_link=1
)
```

### Checking SMS Status

```python
status = await moonheim.checkSmsStatus(message_id="YOUR_MESSAGE_ID")
print(status)
```

### Retrieving Account Balance

```python
balance = await moonheim.getBalance()
print(balance)
```

## Handling Exceptions

\`**MoonheimSMS**\` raises \`**InvalidPhoneNumber**\` if an invalid phone number is provided. Ensure to handle this
exception in your code to manage such errors gracefully.

## Contributing

We welcome contributions! Please open an issue or submit a pull request for any improvements.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](./LICENSE) file for details.


> [!IMPORTANT]
> This package is not officially affiliated with Meow SMS. All trademarks belong to their respective owners.