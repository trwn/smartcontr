// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;



import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PsychPunks is ERC721Enumerable, Ownable {

  uint public constant MAX_SUPPLY = 100;
  uint public price;
	string _baseTokenURI;
	bool public paused;

  // team wallets
  address public t1 = 0x8871E95723c191DCa371A5031aA12d05a40bFf95; // 20%
  address public t2 = 0x8871E95723c191DCa371A5031aA12d05a40bFf95; // 20%
  address public t3 = 0x8871E95723c191DCa371A5031aA12d05a40bFf95; // 20% 

  // community wallets
  address public designWallet = 0x8871E95723c191DCa371A5031aA12d05a40bFf95; // 20%
  address public marketingWallet = 0x8871E95723c191DCa371A5031aA12d05a40bFf95; // 10%
  address public charityWallet = 0x8871E95723c191DCa371A5031aA12d05a40bFf95; // 10%

  constructor(string memory baseURI) ERC721("PsychPunk", "PSYCHPUNK")  {
      setBaseURI(baseURI);
      paused = true;
      price = 30000000000000000; // 0.03 ETH
  }

  modifier saleIsOpen{
      require(totalSupply() < MAX_SUPPLY, "Sale end");
      _;
  }

  function mintPsychPunk(address _to, uint _count) public payable saleIsOpen {
      if(msg.sender != owner()){
          require(!paused, "Pause");
      }
      require(totalSupply() + _count <= MAX_SUPPLY, "Max limit");
      require(totalSupply() < MAX_SUPPLY, "Sale end");
      require(_count <= 10, "Exceeds 10");
      require(msg.value >= price * _count, "Value below price");

      for(uint i = 0; i < _count; i++){
          _safeMint(_to, totalSupply());
      }
  }

  function getPrice(uint _count) public view returns (uint) {
      return price * _count;
  }

  function setPrice(uint _price) external onlyOwner {
      price = _price;
  }

  function _baseURI() internal view virtual override returns (string memory) {
      return _baseTokenURI;
  }
  function setBaseURI(string memory baseURI) public onlyOwner {
      _baseTokenURI = baseURI;
  }

  function walletOfOwner(address _owner) external view returns(uint[] memory) {
      uint tokenCount = balanceOf(_owner);

      uint[] memory tokensId = new uint[](tokenCount);
      for(uint i = 0; i < tokenCount; i++){
          tokensId[i] = tokenOfOwnerByIndex(_owner, i);
      }

      return tokensId;
  }

  function pause(bool val) public onlyOwner {
      paused = val;
  }

  modifier onlyTeam{
    require(
      msg.sender == t1 ||
      msg.sender == t2 ||
      msg.sender == t3 ||
      msg.sender == owner(),
      "Only team can do this"
    );
    _;
  }

  function withdrawAll() public onlyTeam {
      uint share = address(this).balance / 5;

      payable(t1).transfer(share);
      payable(t2).transfer(share);
      payable(t3).transfer(share);

      payable(designWallet).transfer(share);
      payable(marketingWallet).transfer(share/2);
      payable(charityWallet).transfer(share/2);
  }
}