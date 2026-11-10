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
