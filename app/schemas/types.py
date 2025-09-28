from typing import Annotated, List, Optional

from pydantic import Field, StringConstraints


phone_type = Annotated[str, StringConstraints(pattern=r"^\+\d{8,15}$")]
name_type = Annotated[str, Field(..., max_length=100)]
title_type = Annotated[str, Field(..., max_length=200)]
description_type = Annotated[Optional[str], Field(None, max_length=1000)]
price_type = Annotated[float, Field(ge=0)]
skill_type = Annotated[
    List[str],
    Field(min_length=1, description="At least one skill required"),
    Field(max_length=30, description="No more than 30 skills"),
]
