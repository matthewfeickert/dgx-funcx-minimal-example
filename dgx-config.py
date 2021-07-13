from parsl.addresses import address_by_hostname
from funcx_endpoint.endpoint.utils.config import Config
from funcx_endpoint.executors import HighThroughputExecutor
from parsl.providers import LocalProvider
from parsl.launchers import SimpleLauncher

user_opts = {
    "dgx": {
        "worker_init": ". ${HOME}/dgx-funcx-minimal-example/worker_env_setup.sh",
    }
}

config = Config(
    executors=[
        HighThroughputExecutor(
            label="DGX",
            max_workers_per_node=25,
            address=address_by_hostname(),
            provider=LocalProvider(
                init_blocks=1,
                min_blocks=1,
                max_blocks=1,
                nodes_per_block=1,  # default value
                parallelism=1,  # default value
                worker_init=user_opts["dgx"]["worker_init"],
                # launcher=SimpleLauncher(),
            ),
        )
    ],
    funcx_service_address="https://api.dev.funcx.org/v2"
)

# For now, visible_to must be a list of URNs for globus auth users or groups, e.g.:
# urn:globus:auth:identity:{user_uuid}
# urn:globus:groups:id:{group_uuid}
meta = {
    "name": "pyhf",
    "description": "",
    "organization": "",
    "department": "",
    "public": False,
    "visible_to": [],
}
