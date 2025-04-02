# session.py

_cf_token = None
_selected_zones = {}  # ключ = домен, значение = ID


def set_token(token: str):
    global _cf_token
    _cf_token = token.strip()


def get_token() -> str:
    if not _cf_token:
        raise ValueError("Token is not set. Use set_token()")
    return _cf_token


def set_selected_zones(zone_dict: dict[str, str]):
    global _selected_zones
    _selected_zones = zone_dict


def get_selected_zones() -> dict:
    return _selected_zones


def clear_selected_zones():
    global _selected_zones
    _selected_zones = {}
