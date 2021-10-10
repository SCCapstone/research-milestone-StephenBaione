import httpx

class OpenSeaService():
    def __init__(self) -> None:
        self.base_url = "https://api.opensea.io/api/v1"

    async def get_asset(self, contract_address: str, token_id: str):
        endpoint = f"/asset/{contract_address}/{token_id}"
        result = await self.make_request("get", endpoint)
        return result
            

    async def make_request(self, method: str, endpoint: str, params: dict = None, body: dict = None, json: dict = None):
        if method.lower() == "get":
            async with httpx.AsyncClient(base_url=self.base_url) as client:
                req_options = {"method": "get", "url": endpoint}
                if params:
                    req_options.update({"params": params})
                request = client.build_request(**req_options)
                resp = await client.send(request)
                if resp.status_code != 200:
                    return None
                return resp.json()
        raise Exception("Not Implemented")
