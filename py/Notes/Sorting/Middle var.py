def get_median_font_size(font_sizes: list[int]) -> int | None:
    font_sizes_list = []

    if len(font_sizes) == 0:
        return None

    font_sizes_list = sorted(font_sizes)

    m_pos = (len(font_sizes_list) - 1) // 2

    middle_number = font_sizes_list[m_pos]
    return middle_number