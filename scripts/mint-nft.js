// require('dotenv').config();
// const API_URL = process.env.API_URL;
// const PUBLIC_KEY = process.env.PUBLIC_KEY;
// const PRIVATE_KEY = process.env.PRIVATE_KEY;

// const { createAlchemyWeb3 } = require("@alch/alchemy-web3");
// const web3 = createAlchemyWeb3(API_URL);

// const contract = require("../artifacts/contracts/psych_punks.sol/psychpunks.json");
// const contractAddress = "0x38d1eD2fB642fB4146a6C688c3417Be0340FEb3e";
// const nftContract = new web3.eth.Contract(contract.abi, contractAddress);

// async function mintNFT(tokenURI) {
//     const nonce = await web3.eth.getTransactionCount(PUBLIC_KEY, 'latest'); //get latest nonce
  
//     //the transaction
//     const tx = {
//       'from': PUBLIC_KEY,
//       'to': contractAddress,
//       'nonce': nonce,
//       'gas': 500000,
//       'maxPriorityFeePerGas': 1999999987,
//       'data': nftContract.methods.mintNFT(PUBLIC_KEY, tokenURI).encodeABI()
//     };
  
  
//     const signPromise = web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);
//     signPromise.then((signedTx) => {
  
//       web3.eth.sendSignedTransaction(signedTx.rawTransaction, function(err, hash) {
//         if (!err) {
//           console.log("The hash of your transaction is: ", hash, "\nCheck Alchemy's Mempool to view the status of your transaction!"); 
//         } else {
//           console.log("Something went wrong when submitting your transaction:", err)
//         }
//       });
//     }).catch((err) => {
//       console.log("Promise failed:", err);
//     });
//   }
//   mintNFT("https://gateway.pinata.cloud/ipfs/QmZ9UyRGrcpgmtFiv8WwDhjxdChR8JmVSZaqkw3UJ8c1Nz")
require('dotenv').config();
const API_URL = process.env.API_URL;
const PUBLIC_KEY = process.env.PUBLIC_KEY;
const PRIVATE_KEY = process.env.PRIVATE_KEY;

const { createAlchemyWeb3 } = require("@alch/alchemy-web3");
const web3 = createAlchemyWeb3(API_URL);

const contract = require("../artifacts/contracts/psych_punks.sol/psychpunks.json");
const contractAddress = "0xd9145CCE52D386f254917e481eB44e9943F39138";
const nftContract = new web3.eth.Contract(contract.abi, contractAddress);

async function mintNFT(tokenURI) {
  const nonce = await web3.eth.getTransactionCount(PUBLIC_KEY, 'latest'); //get latest nonce

  //the transaction
  const tx = {
    'from': PUBLIC_KEY,
    'to': contractAddress,
    'nonce': nonce,
    'gas': 500000,
    'maxPriorityFeePerGas': 1999999987,
    'data': nftContract.methods.mintNFT(PUBLIC_KEY, tokenURI).encodeABI()
  };

  const signPromise = web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);
  signPromise.then((signedTx) => {

    web3.eth.sendSignedTransaction(signedTx.rawTransaction, function(err, hash) {
      if (!err) {
        console.log("The hash of your transaction is: ", hash, "\nCheck Alchemy's Mempool to view the status of your transaction!"); 
      } else {
        console.log("Something went wrong when submitting your transaction:", err)
      }
    });
  }).catch((err) => {
    console.log("Promise failed:", err);
  });
}

mintNFT("https://gateway.pinata.cloud/ipfs/QmYueiuRNmL4MiA2GwtVMm6ZagknXnSpQnB3z2gWbz36hP");