# Python Cardano-Wallet API

cwAPI is a python wrapper for the Cardano Wallet API.

## Securty Warning
This Python Library can help you connect to your Deadalus or Cardano-wallet prossess and interact freely, the very act of writing your passpharase in a script violates all best practises in regards to storing Crypto! 
##### When used on the mainnet, wallets using such integrations should only be operational and never intented for storage! 

## Installation
cwAPI is avaiable via Pypi 

Install using pip:

```sh
pip install cwAPI
```

## Usage

Import using:
```sh
pip install cwAPI
```

Intialize API and configure port:

```sh
api = cwAPI()
api.port="https://localhost:8080"
```

To connct to an HTTPS port add TLS credencials: 
```sh
api.cert=(r'{PATH_TO_CERT}\client.crt',r"{PATH_TO_CERT}\client.key")
api.ca=r'{PATH_TO_CERT}\ca.crt'
```

Hint: You can get your path and port from the Deadalus diagnostic pannel(Ctrl+D)

Get Wallets:
```sh
api.Wallets.list(api)
```

Send Transaction:
```sh
api.Transactions.create(api,walletId=walletId,passphrase=passphrase,payments=payments,metadata=metadata)
```
Example Payments:
```sh
payments=[{
"address": "addr_test1qz0mmzuwnya2yasfy78klcqazd73a320a9agpunuv4zqlyjwrycda8m2jmtws4hktfq6xp59q2t2a8w6elnky6a9txtsht8h6d",
"amount": {
"quantity": 42000000,
"unit": "lovelace"
},
"assets": []
}]
```

Example Metadata:
```sh
metadata={"1":{"string":"Hello World"}}
```

All APIS are available with the same arguments as the referencing API.
https://input-output-hk.github.io/cardano-wallet/api/edge/

Always use 'self' as the first positional argument!


