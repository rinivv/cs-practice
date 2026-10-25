def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")
    parts = line.split(" ", 2)
    if len(parts) != 3:
        raise ValueError("Неверный формат строки")
    time, level, message = parts
    levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in levels:
        raise ValueError("Неверно задан уровень")
    return {"time": time,
            "level": level,
            "message": message}

def count_levels(lines: list[str]) -> dict:
    cnt = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event["level"]
            cnt[level] = cnt.get(level, 0) + 1
        except ValueError:
            cnt["BROKEN"] = cnt.get("BROKEN", 0) + 1
    return cnt

def top_errors(lines: list[str], n: int) -> list[list]:
    error_cnt = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                message2 = event["message"]
                error_cnt[message2] = error_cnt.get(message2, 0) + 1
        except ValueError:
            pass
    res = [[message2, cnt] for message2, cnt in error_cnt.items()]
    res.sort(key=lambda x: (-x[1], x[0]))
    return res[:n]

def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts.keys()):
        lines.append(f"{level}: {counts[level]}")
    lines.append("")
    lines.append("Частые ошибки:")
    if not errors:
        pass
    else:
        for message, count in errors:
            lines.append(f"- {message} — {count}")
    return "\n".join(lines) + "\n"
