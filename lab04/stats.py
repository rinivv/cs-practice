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
    return {'city': city, 'temp': temp, 'date': date}

        
