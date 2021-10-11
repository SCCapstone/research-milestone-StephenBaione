from ..services.opensea_service import OpenSeaService
from ..services.blockchair_service import BlockChairService

from ..db.schema.nft import NFT

class NFTController():
    def __init__(self) -> None:
        self.blockchair_service = BlockChairService()
        self.opensea_service = OpenSeaService()

    async def get_nft(self, contract_address: str, token_id: str):

        # Fetch token metadata from OpenSea
        result_opensea = await self.opensea_service.get_asset(contract_address, token_id)

        # Fetch token stats from Blockchair
        result_blockchair = await self.blockchair_service.get_erc721_contract_stats(contract_address, limit="20")

        result = {}
        if result_opensea:
            result.update(result_opensea)
        if result_blockchair:
            result.update(result_blockchair)

        return result
        

