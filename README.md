# generate-cloud-init-ssh-host-keys

This tool generates SSH host keys and adds them to a [cloud-init](https://cloud-init.io/) config file and to your known_hosts file. This allows you to connect to a cloud-init-configured instance securely with SSH without having to manually verify the host's keys.

## Usage

Call the program with the path to your cloud-init config file:

```
generate-cloud-init-ssh-host-keys my-cloud-init.yaml
```

SSH host keys are generated for all supported key types and they are appended to the given file. The fingerprints of the keys are added to your `~/.ssh/known_hosts` file. The hostname to use for the `known_hosts` entries is taken from the [`fqdn` or `hostname`](https://cloudinit.readthedocs.io/en/latest/topics/modules.html#set-hostname) properties specified in the config file.
