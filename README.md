# Assistant Bot

A simple CLI contact book bot that stores names, phone numbers, and birthdays in memory.

## Usage

```bash
python3 address_book.py
```

## Commands

| Command | Arguments | Description |
|---|---|---|
| `hello` | — | Greet the bot |
| `add` | `<name> <phone>` | Add a phone to a new or existing contact |
| `change` | `<name> <old_phone> <new_phone>` | Replace a phone number for an existing contact |
| `remove-phone` | `<name> <phone>` | Remove a specific phone from a contact |
| `delete` | `<name>` | Remove a contact entirely |
| `phone` | `<name>` | Show a contact's phones |
| `all` | — | List all contacts |
| `add-birthday` | `<name> <DD.MM.YYYY>` | Add a birthday to a contact |
| `show-birthday` | `<name>` | Show a contact's birthday |
| `birthdays` | — | List contacts with birthdays in the next 7 days |
| `close` / `exit` | — | Exit the bot |

