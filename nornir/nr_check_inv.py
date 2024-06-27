#!/usr/bin/env python

from config import nr
from rich import print as rprint

inventory = nr.inventory.dict()

if __name__ == "__main__":
    rprint(inventory)

