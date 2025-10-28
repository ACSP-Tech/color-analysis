from pydantic import BaseModel
from typing import List

class ColorFreq(BaseModel):
    frequency: int
    color: str

class ColorRes(BaseModel):
    Which_color_of_shirt_is_the_mean_color: List[str]
    Which_color_is_mostly_worn_throughout_the_week: str
    Which_color_is_the_median: str
    Get_the_variance_of_the_colors: float
    what_is_the_probability_that_the_color_is_red: float
    Saved_colours_and_their_frequencies: List[ColorFreq]