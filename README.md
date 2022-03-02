![Pressale on FEGex](https://fegexchange.github.io/assets/presale.jpg)

# FEGex Asset Repo

## How to submit token asset information

- Fork this repo to your own GitHub account
- Create a new folder and name it the contract address of your token (case sensitive), under the matching blockchain. Example: if you're submitting an Ethereum based token you need to create a new folder under `blockchains/ethereum/assets/<YOUR TOKENS CONTRACT ADDRESS>`. 
- **When using your contract address, be sure to supply it in the checksum version (case sensitive)**


- In this folder create a new file named `info.json`

- In this folder include your token logo, and the file must be named `logo.png`
- Submit a PR to have your submission reviewed

### info.json

- `id` : contract address (case sensitive) of the token **Be sure to use the [checksum version](https://support.mycrypto.com/general-knowledge/ethereum-blockchain/ethereum-address-has-uppercase-and-lowercase-letters)**
- `name` : full token name
- `symbol` : token's symbol
- `type` : token type; `BEP20` or `ERC20`
- `decimals` : number of decimals your token supports
- `website` : official website of your token
- `explorer` : url of your token's info page on the block explorers
- `refelections` : does your token receive reflections, only need if your token has reflections
- `social`: key/value pairs of your token's social media links

Example of Valid JSON

```
{
    "id": "Contract Address",
    "name": "Token Name",
    "symbol": "Token Symbol",
    "type": "ERC20",
    "decimals": 9,
    "website": "https://fegtoken.com",
    "explorer": "https://etherscan.io/token/ConTRactAddRESs", 
    "reflections": true,
    "social" : {
        "twitter" : "https://twitter.com/fegtoken"
    }
}
 ```

### logo.png

Include the official logo of your token you want displayed on FEGex

- the logo should be square of size *`256x256px`* 

### Example

For an example, look at the details of the FEG Token submission on the Binance Smart Chain side: [FEG Token](https://github.com/fegexchange/assets/tree/main/blockchains/smartchain/assets/0xacFC95585D80Ab62f67A14C566C1b7a49Fe91167)

![SmartDeFi](https://fegexchange.github.io/assets/smartdefi.jpeg)
