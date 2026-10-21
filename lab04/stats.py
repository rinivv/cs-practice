def parse_record(line: str) -> dict:
    parts = line.strip().split(';')
    if len(parts) != 3:
        raise ValueError('Неверное кол-во полей')
    city, temp1, date = parts
    if city == '' or date == '':
        raise ValueError('Пустое значение города или даты')
    try:
        temp = float(temp1)
    except ValueError:
        raise ValueError('Температура не является числом')
    return {'city': city, 'temperature': temp, 'date': date}

def read_valid(lines: list[str]) -> list[dict]:
    res = []
    for line in lines:
        if not line.strip():
            continue
        try:
            rec = parse_record(line)
            res.append(rec)
        except ValueError:
            continue
    return res

def average_by_city(records: list[dict]) -> dict:
    total = {}
    cnt = {}
    for i in records:
        city = i['city']
        temp= i['temperature']
        total[city] = total.get(city,0) + temp
        cnt[city] = cnt.get(city,0) + 1
    ave = {}
    for city in total:
        ave[city] = round(total[city]/cnt[city], 1)
    return ave

def warmest_city(records: list[dict]) -> str:
    city_temps = average_by_city(records)
    if not city_temps:
        return ''
    return max(city_temps.keys(), key=lambda c: city_temps[c])
