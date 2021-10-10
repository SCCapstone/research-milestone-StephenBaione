from typing import Optional
from pydantic import BaseModel,Field


class NFT(BaseModel):
    token_id: Optional[int] = None
    num_sales: Optional[int] = None
    background_color: Optional[str] = None
    image_url: Optional[str] = None
    image_preview_url: Optional[str] = None
    image_thumbnail_url: Optional[str] = None
    image_original_url: Optional[str] = None
    animation_url: Optional[str] = None
    animation_original_url: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    external_link: Optional[str] = None
