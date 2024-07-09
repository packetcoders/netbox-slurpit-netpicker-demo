
# Slurp'it, Netpicker, and NetBox Demo

This repository contains scripts and examples from the Packet Coders Tech Showcase featuring Slurp'it, Netpicker, and NetBox.

## Tools Overview

Learn more about each tool showcased in this repository:

- [NetBox](https://www.netboxlabs.com)
- [Netpicker](https://www.netpicker.io)
- [Slurp'it](https://www.slurpit.io)

## Nornir, NAPALM, and GraphQL Setup

> **Note:** The examples in this repository, including Jinja templates, are built for Cisco IOS devices.

### 1. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Update Environment Variables

```bash
cp .env.example .env
```

Update the `.env` file with your NetBox settings and device credentials.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Nornir Scripts

You can now run any of the following Nornir scripts:

1. Check NetBox is correctly sending inventory data.
    ```bash
    python3 nornir/nr_check_inv.py
    ```
2. Render the Jinja templates using data from NetBox's GraphQL.
    ```bash
    python3 nornir/nr_build.py
    ```
3. Deploy the config out to your devices within your inventory.
    ```bash
    python3 nornir/nr_deploy.py
    ```
