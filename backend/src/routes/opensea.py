from fastapi import APIRouter

from ..services.opensea_service import OpenSeaService
from ..controller.nft_controller import NFTController

opensea_service = OpenSeaService()
nft_controller = NFTController()

opensea_router = APIRouter(prefix="/opensea", tags=["OpenSea", "API"])

@opensea_router.get("/nft")
async def get_nft(contract_address: str, token_id: str):
    result = await nft_controller.get_nft(contract_address, token_id)
    return {
        "data": result
    }