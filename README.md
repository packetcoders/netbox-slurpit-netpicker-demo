# Slurp`it, Netpicker and NetBox Demo

This repo contains the scripts and examples from the Packet Coders Tech Showcase around Slurp`it, Netpicker and NetBox.

## Links

To learn more about each of the tools within this example please see the links below:

- [NetBox](https://www.netboxlabs.com)
- [Netpicker](https://www.netpicker.io)
- [Slurp'it](https://www.slurpit.io)



## Nornir, NAPALM and GraphQL Setup

> [!NOTE]
> The examples within this repo, the Jinja templates, etc have all been built for Cisco IOS devices.

1. Create virtual environment

```
python3 -m venv .venv
source .venv/bin/activiate
```

2. Update `.env`

```
cp .env.example .env
```

Next, update the `.env` with your settings for NetBox and your device credentials.

3. Install depos

```
pip install -r requirements.txt
```

4. Run Nornir

You can now run either of the Nornir scripts:

```
1. Check NetBox is correctly sending inventory data.
python3 nornir/nr_check_inv.py

2. Render the Jinja templates using data from NetBoxs GraphQL.
python3 nornir/nr_build.py

3. Deploy the config out to your devices within your inventory.
python3 nornir/nr_deploy.py
```





