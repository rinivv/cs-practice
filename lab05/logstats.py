def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")
    parts = line.split(" ", 2)
    if len(parts) != 3:
        raise ValueError("Неверный формат строки")
    time, level, message = parts
    
    # Проверяем, что уровень входит в список допустимых
    levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in levels:
        raise ValueError("Неверно задан уровень")
    return {"time": time,
            "level": level,
            "message": message}
