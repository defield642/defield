import android

# Initialize Android object
droid = android.Android()

# Get all SMS messages from inbox
messages = droid.smsGetMessages(True, 'inbox').result

# Print the messages and their corresponding contact names and numbers
for message in messages:
    number = message['address']
    contact_name = droid.contactsGetContactIdsByPhoneNumber(number).result
    if contact_name:
        contact_info = droid.contactsGetContactName(contact_name[0]).result
        name = contact_info if contact_info else 'Unknown'
    else:
        name = 'Unknown'
    print(f"Message from {name} ({number}): {message['body']}")
