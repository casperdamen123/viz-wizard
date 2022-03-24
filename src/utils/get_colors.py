from typing import List
import numpy as np


def random_color_selection(n: int) -> List[str]:
    """Generate random Hex color
    Args:
        n (int): Number of colors to generate
    Returns:
        hex_codes (List[str]): Hex color codes
    """
    hex_codes = []
    for _ in range(n):
        hex_number = str(hex(np.random.randint(1118481, 16777215)))
        hex_code = '#' + hex_number[2:]
        hex_codes.append(hex_code)
    return hex_codes
