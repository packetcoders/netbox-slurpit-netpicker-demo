import os

from dotenv import load_dotenv

from nornir import InitNornir

load_dotenv()

print(os.getenv("NETBOX_FQDN"))

nr = InitNornir(
    runner={"plugin": "threaded", "options": {"num_workers": 20}},
    inventory={
        "plugin": "NetBoxInventory2",
        "options": {
            "nb_url": os.getenv("NETBOX_FQDN"),
            "nb_token": os.getenv("NETBOX_TOKEN"),
            #"ssl_verify": False,
            "filter_parameters": {"role": "spine", "tenant": "uber-coffees"},
            "use_platform_slug": True,
        },
    }
)

