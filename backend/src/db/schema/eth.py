from typing import Optional
from pydantic import BaseModel, Field

class EthStats(BaseModel):
    blocks: int = Field(...)
    transactions: int = Field(...)
    blocks_24h: int = Field(...)
    circulation_approximate: str = Field(...)
    blockchain_size: int = Field(...)
    difficulty: int = Field(...)
    volume_24h_approximate: str = Field(...)
    average_transaction_fee_24h: str = Field(...)
    median_transaction_fee_24h: str = Field(...)
    average_transaction_fee_usd_24h: float = Field(...)
    median_transaction_fee_usd_24h: float = Field(...)
    market_price_usd: float = Field(...)
    market_price_usd_change_24h_percentage: float = Field(...)
    market_cap_usd: int = Field(...)
    market_dominance_percentage: float = Field(...)
    layer_2: dict = Field(...)


