from typing import Optional
from pydantic import BaseModel, Field

class BitCoin(BaseModel):
    blocks: int = Field(...)
    transactions: int = Field(...)
    circulation: int = Field(...)
    blocks_24h: int = Field(...)
    transactions_24h: int = Field(...)
    volume_24h: int = Field(...)
    blockchain_size: int = Field(...)
    average_transaction_fee: int = Field(...)
    inflation_24h: int = Field(...)
    median_transaction_fee_24h: int = Field(...)
    inflation_usd_24h: int = Field(...)
    average_transaction_fee_usd_24h: int = Field(...)
    median_transaction_fee_usd_24h: int = Field(...)
    market_price_usd: int = Field(...)
    market_cap_usd: int = Field(...)
    market_dominance_percentage: int = Field(...)
    
