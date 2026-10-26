import logstats

path = input().strip()
all_lines = 0
error_lines = 0
broken_lines = 0
try:
    with open(path, encoding="utf-8") as log:
        for line in log:
            if not line.strip():
                continue
            all_lines += 1
            try:
                event = logstats.parse_event(line)
                if event["level"] == "ERROR":
                    error_lines += 1
            except ValueError:
                broken_lines += 1
except FileNotFoundError:
    print(f"Файл {path} не найден.")
    exit()
    
print(all_lines)
print(error_lines)
print(broken_lines)

with open(path, encoding="utf-8") as log:
    cnt = logstats.count_levels(log)

with open(path, encoding="utf-8") as log:
    n = 3 
    top_error = logstats.top_errors(log, n)

text = logstats.format_report(cnt, top_error)

with open("report.txt", "w", encoding="utf-8") as log:
    log.write(text)
