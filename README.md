# generate-cloud-init-ssh-host-keys

This tool generates SSH host keys and adds them to a [cloud-init](https://cloud-init.io/) config file.

You can use the companion tool [ssh-import-known-hosts-cloud-init](https://github.com/JJC1138/ssh-import-known-hosts-cloud-init) to then add the generated public keys to your `~/.ssh/known_hosts` file. This facilitates connecting to a cloud-init-configured instance securely with SSH without having to manually verify the host's keys.

## Usage

Call the program with the path to your cloud-init config file:

```
generate-cloud-init-ssh-host-keys my-cloud-init.yaml
```

SSH host keys are generated for all supported key types and they are appended to the given file.
