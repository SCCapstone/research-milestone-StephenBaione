from ..services.opensea_service import OpenSeaService
from ..services.blockchair_service import BlockChairService

from ..db.schema.nft import NFT

class NFTController():
    async def get_nft(self, contract_address: str, token_id: str):

        # Fetch token metadata from OpenSea
        opensea_service = OpenSeaService()
        result = await opensea_service.get_asset(contract_address, token_id)
        return result if result else None
        

