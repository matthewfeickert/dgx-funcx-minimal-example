# Minimal (failing) example of funcX on HAL DGX

## Machine

These (CPU scaling) examples are all run on the [NCSA HAL DGX cluster](https://wiki.ncsa.illinois.edu/display/ISL20/NVIDIA+DGX+A100) which has [128 cores](https://images.nvidia.com/aem-dam/Solutions/Data-Center/nvidia-dgx-a100-datasheet.pdf) and so is desirable to test scaling performance across.
The DGX does not have a batch system on it and so the users are responsible for load balancing and not overwhelming the system.
How best to do this with `funcX` is not yet fully understood by Matthew.

(GPU scaling examples will follow on another project after CPU scaling is understood.)

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
$ funcx-endpoint start pyhf && funcx-endpoint list
YYYY-MM-DD HH:MM:SS endpoint.endpoint_manager:173 [INFO]  Starting endpoint with uuid: 12345678-abcd-abcd-abcd-123456789101
YYYY-MM-DD HH:MM:SS endpoint.endpoint_manager:238 [INFO]  Launching endpoint daemon process
+---------------+---------+--------------------------------------+
| Endpoint Name | Status  |             Endpoint ID              |
+===============+=========+======================================+
| pyhf          | Running | 12345678-abcd-abcd-abcd-123456789101 |
+---------------+---------+--------------------------------------+
```

6. Copy the Endpoint ID file to wherever you're going to submit from
```console
$ funcx-endpoint list | grep pyhf | awk '{print $(NF-1)}' > endpoint_id.txt
# From the machine to be used at submit time
# $ scp DGX:~/PATH-TO-WHERE-THIS-REPO-CLONED/endpoint_id.txt .
# $ echo "endpoint_id.txt" >> .gitignore
```

7. From the submission machine, make sure that you have the same Python virtual environment setup. So enter into a Python virtual environment and then

```console
$ python -m pip install -r core-requirements.txt
```

8. Then once you're sure that on DGX the `funcx-endpoint` is running and from the submission machine `endpoint_id.txt` is correct run the test job of 5 signal patches

```console
$ time python fit_analysis.py -c config/1Lbb.json -b numpy
```

9. On DGX you'll probably want to try to monitor how things are going with `htop -u $USER`.


## Observed behavior

Things now run but after execution the `funcx-endpoint` ends up in a `Disconnected` state

```console
(pyhf-funcx) [feickert@hal-dgx dgx-funcx-minimal-example]$ funcx-endpoint list
+---------------+--------------+--------------------------------------+
| Endpoint Name |    Status    |             Endpoint ID              |
+===============+==============+======================================+
| pyhf          | Disconnected | 12345678-abcd-abcd-abcd-123456789101 |
+---------------+--------------+--------------------------------------+
```

which according to the [`funcx` `v0.3.0`](https://funcx.readthedocs.io/en/latest/endpoints.html) docs is bad:

> **Disconnected:** The endpoint disconnected unexpectedly. It is not running and therefore, cannot service any functions. Starting this endpoint will first invoke necessary endpoint cleanup, since it was not stopped correctly previously.
