from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    is_valid = any(item.lower() in ingredients.lower() for item in allowed)

    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
