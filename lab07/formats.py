def csv_to_records(text: str) -> list[dict]:
    if not text.strip():
        return []
    lines = text.strip().split('\n')
    heads = [h.strip() for h in lines[0].split(',')]
    records = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(',')]
        record = dict(zip(heads, values))
        records.append(record)
    return records

def conv_for_f2(val:str):
    val_low = val_str.lower()
    if val_low in ('true','yes'):
        return True
    if val_low in ('false','no'):
        return False
    try:
        return int(val_str)
    except ValueError:
        pass
    try:
        return float(val_str)
    except ValueError:
        pass
    return val
    
def parse_settings(lines: list[str]) -> dict:
    result = {}
    cur_key = None
    for line in lines:
        line = line.split('#')[0].strip()
        if not line:
            continue
        if line[0] == '-':
            if cur_key is not None:
                val_str = line[1:].strip()
                result[cur_key].append(conv_for_f2(val_str))
            continue
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()
            if val:
                result[key] = conv_for_f2(val)
                cur_key = None
            else:
                result[key] = []
                cur_key = key
    return result

def merge_by_key(rows: list[dict], extra: dict, key: str = 'id') -> list[dict]:
    merged_records = []
    for row in rows:
        record_id = row.get(key)
        if record_id is not None and record_id in extra:
            new_record = {**extra[record_id], **row}
            merged_records.append(new_record)
        else:
            merged_records.append(row)
    return merged_records
