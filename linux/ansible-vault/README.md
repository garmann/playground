# ansible-vault

basic guide for vault commands:

- http://docs.ansible.com/ansible/playbooks_vault.html

i came across this link:

- http://docs.ansible.com/ansible/playbooks_best_practices.html#variables-and-vaults

it says:

```
Variables and Vaults
For general maintenance, it is often easier to use grep, or similar tools, to find variables in your Ansible setup. Since vaults obscure these variables, it is best to work with a layer of indirection. When running a playbook, Ansible finds the variables in the unencrypted file and all sensitive variables come from the encrypted file.

A best practice approach for this is to start with a group_vars/ subdirectory named after the group. Inside of this subdirectory, create two files named vars and vault. Inside of the vars file, define all of the variables needed, including any sensitive ones. Next, copy all of the sensitive variables over to the vault file and prefix these variables with vault_. You should adjust the variables in the vars file to point to the matching vault_ variables and ensure that the vault file is vault encrypted.

This best practice has no limit on the amount of variable and vault files or their names.
```

with the idea you are able to use environments with different variables including encryption. perfect!

lets run this:

```
ansible-playbook -i inv/prod/hosts_prod playbook.yml
ERROR! Decryption failed
```

ups... ;-)

```
ansible-playbook --ask-vault-pass -i inv/prod/hosts_prod playbook.yml
Vault password:

PLAY [all] *********************************************************************

TASK [setup] *******************************************************************
ok: [x.x.x.x]

TASK [debug : test debug] ******************************************************
ok: [x.x.x.x] => {
    "text": "test with ansible-vault"
}

PLAY RECAP *********************************************************************
x.x.x.x              : ok=2    changed=0    unreachable=0    failed=0
```

try:

- view the vault.yml
- vault password is: x
