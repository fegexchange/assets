# FEGex Asset Repo

## How to submit token asset information

- Fork this repo to your own GitHub account
- Create a new folder and name it the contract address of your token, under the matching blockchain. Example: if you're submitting an Ethereum based token you need to create a new folder under `blockchains/ethereum/assets/<YOUR TOKENS CONTRACT ADDRESS>`


- In this folder create a new file named `info.json`

- In this folder include your token logo, and the file must be named `logo.png`
- Submit a PR to have your submission reviewed

### info.json

- `id` : contract address of the token
- `name` : full token name
- `symbol` : token's symbol
- `type` : token type; `BEP20` or `ERC20`
- `decimals` : number of decimals your token supports
- `website` : official website of your token
- `explorer` : url of your token's info page on the block explorers
- `social`: key/value pair of your token's social media links

### logo.png

Include the official logo of your token you want displayed on FEGex

- the logo should be square, recommended 256x256px 
- avoid transparent backgrounds so your logo is displayed properly in light and dark themes

### Example

For an example, look at the details of the FEG Token submission on the Binance Smart Chain side: [FEG Token](https://github.com/fegexchange/assets/tree/main/blockchains/smartchain/assets/0xacFC95585D80Ab62f67A14C566C1b7a49Fe91167)
