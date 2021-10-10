import httpx

from src.db.schema.eth import EthStats

class BlockChairService():
    """
    Blockchair will be the primary API for blockchain and ERC statistics
    Many of these calls will be made at the same time from different accounts and internally
    Best to make these service calls asynchronous for optimal performance (Don't bog the server down)
    """
    def __init__(self) -> None:
        # TODO:// Secure this in production
        self.api_key = "G___fugCRxWaoY5t04thDGYKndytAnjJ"
        self.base_url = "https://api.blockchair.com"
        self.classifications = {
            "bitcoin": ["bitcoin", "dogecoin"],
            "ethereum": ["ethereum"],
            "crosschain": ["tether", "usd-coin", "binance-usd"]
        }

    async def get_all_stats(self) -> dict:
        endpoint = "/stats"
        data = (await self.make_request("get", endpoint))["data"]
        return data

    async def get_eth_stats(self) -> dict:
        endpoint = "/ethereum/stats"
        data = (await self.make_request("get", endpoint))["data"]
        return self.parse_eth_stats(data)

    def parse_eth_stats(self, data):
        eth_stats = EthStats(**data)
        return eth_stats

    async def get_erc20_contract_stats(self, token_address: str):
        endpoint = f"/ethereum/erc-20/{token_address}/stats"
        params = {
            "limit": 50
        }
        data = (await self.make_request("get", endpoint, params))["data"]
        return data

    async def get_erc721_contract_stats(self, token_address: str, limit = 50):
        endpoint = f"/ethereum/erc-721/{token_address}"
        params = {
            "limit": 50
        }
        data = (await self.make_request("get", "https://api.blockchair.com/ethereum/dashboards/address/0x139b522955d54482e7662927653abb0bfb6f19ba?erc_20=precise&erc_721=true&assets_in_usd=true&contract_details=true&transactions_instead_of_calls=true"))["data"]
        return data
    
    async def make_request(self, method: str, endpoint: str, params: dict = None, body: dict = None, json: dict = None):
        if method.lower() == "get":
            async with httpx.AsyncClient(base_url=self.base_url) as client:
                req_options = {"method": "get", "url": endpoint}
                if params:
                    req_options.update({"params": params})
                request = client.build_request(**req_options)
                resp = await client.send(request)
                if resp.status_code != 200:
                    raise Exception(f"Error fetching {endpoint} from BlockChair\nStatus Code: {resp.status_code}")
                return resp.json()
        raise Exception("Not Implemented")
