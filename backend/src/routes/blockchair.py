from fastapi import APIRouter

from ..services.blockchair_service import BlockChairService

blockchair_router = APIRouter(prefix="/blockchair", tags=["Blockchair", "API"])
blockchair_service = BlockChairService()

@blockchair_router.get("/stats")
async def get_blockchair_stats():
    results = await blockchair_service.get_eth_stats()
    return {
        "data": results
    }

@blockchair_router.get("/erc20/stats")
async def get_erc20_stats(entity_type: str, token_address):
    if entity_type == "collection":
        results = await blockchair_service.get_erc20_contract_stats(token_address)
        return {
            "data": results
        }
    return {}

@blockchair_router.get("/erc721/stats")
async def get_erc20_stats(entity_type: str, token_address: str):
    results = await blockchair_service.get_erc721_contract_stats(token_address)
    return {
        "data": results
    }
