def count_by_extension(paths: list[str]) -> dict[str, int]:
    cnt = {}
    for p in paths:
        file = p.split('/')[-1]
        if '.' in file:
            ext = file.split('.')[-1].lower()
        else:
            ext = ""
        cnt[ext] = cnt.get(ext, 0) + 1
    return cnt
