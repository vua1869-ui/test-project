def viet_hoa_chu_cai_dau(s:str)->str:
    if len(s) == 0:
        return s
    return s[0].upper() + s[1:]