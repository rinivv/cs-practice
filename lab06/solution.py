def count_by_extension(paths: list[str]) -> dict[str, int]:
    cnt = {}
    for p in paths:
        file = p.split('/')[-1]
        if '.' in file and file[0]!=0:
            ext = file.split('.')[-1].lower()
        else:
            ext = ""
        cnt[ext] = cnt.get(ext, 0) + 1
    return cnt

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return sorted(paths, key=lambda p: (-p.count('/'), p))[0]

def human_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    ras = ["КБ", "МБ", "ГБ", "ТБ"]
    size = n_bytes
    for r in ras:
        size /= 1024
        if size < 1024:
            return f"{size:.1f} {r}"
    return f"{size:.1f} {ras[-1]}"
