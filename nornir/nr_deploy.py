#!/usr/bin/env python
import os
from pathlib import Path

from dotenv import load_dotenv
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_utils.plugins.functions import print_result
from config import nr
from nornir.core.task import Result, Task

load_dotenv()

OUTPUT_PATH = f"{Path(__file__).parent}/output"

nr.inventory.defaults.username = os.getenv("DEVICE_USERNAME")
nr.inventory.defaults.password = os.getenv("DEVICE_PASSWORD")

def deploy_config(task: Task) -> Result:
    napalm_result = task.run(
        task=napalm_configure,
        filename=f"{OUTPUT_PATH}/{task.host}.txt",
        replace=False,
        #dry_run=True
    )

    return Result(
        host=task.host,
        result=f"{napalm_result.result}",
    )


if __name__ == "__main__":
    deploy_result = nr.run(task=deploy_config)

    print_result(deploy_result)
