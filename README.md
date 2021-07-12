# dgx-funcx-minimal-example

## Minimal Example

1. On DGX get Python 3.8.11 with pyenv following instructions at https://github.com/Neubauer-Group/dgx-setup
   - Step 1 is optional, but ensures that you're off of the `/home/` directory which means you won't get yelled at for downloading large binaries
2. Clone this repo to your `$HOME` directory (for PATH consistency in example)
2. Create the pyenv virtual environment

```console
$ . create_env.sh
```
3. On DGX create the `funcx-endpoint`

```console
$ funcx-endpoint configure pyhf
```

4. Then copy the example `funcx` config into place for `funcx`

```console
$ cp dgx-config.py ~/.funcx/pyhf/config.py
```

5. Then startup the endpoint

```console
$ funcx-endpoint start pyhf
YYYY-MM-DD HH:MM:SS endpoint.endpoint_manager:173 [INFO]  Starting endpoint with uuid: 12345678-abcd-abcd-abcd-123456789101
YYYY-MM-DD HH:MM:SS endpoint.endpoint_manager:238 [INFO]  Launching endpoint daemon process
$ funcx-endpoint list
+---------------+--------+--------------------------------------+
| Endpoint Name | Status |             Endpoint ID              |
+===============+========+======================================+
| pyhf          | Active | 12345678-abcd-abcd-abcd-123456789101 |
+---------------+--------+--------------------------------------+
```

6. Copy the Endpoint ID file to wherever you're going to submit from
```console
$ funcx-endpoint list | grep pyhf | awk '{print $(NF-1)}' > endpoint_id.txt
# From the machine to be used at submit time
# $ scp DGX:~/PATH-TO-WHERE-THIS-REPO-CLONED/endpoint_id.txt .
# $ echo "endpoint_id.txt" >> .gitignore
```
