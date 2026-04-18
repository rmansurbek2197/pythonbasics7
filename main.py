def eng_uzun_kalit(lugat):
    if not lugat:
        return None
    return max(lugat, key=len)

lugat = {"apples": 5, "banana": 10, "cherry": 15}
print(eng_uzun_kalit(lugat))