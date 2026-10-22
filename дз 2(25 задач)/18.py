
from re import *
import logging
import json

logging.basicConfig(
    filename="processing.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    encoding="utf-8"
)

tips = {}
error = 0
urls = {}
sch = r"([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\s+([a-zA-Z]+)\s+/(\S+)\s+([0-9]+)"
try:
    logging.info("Начинаем обработку access.log")
    with open("access.log", "r", encoding="utf-8") as file:
        for s in file:
            lst = findall(sch, s)
            if not lst:
                logging.warning("Строка не соответствует формату: %s", s.strip())
                continue
            tip = lst[0][1]
            id_i = lst[0][0]
            url = lst[0][2]
            kod = int(lst[0][3])
            if tip not in tips:
                tips[tip] = 1
            else:
                tips[tip] += 1
            if 400 <= kod <= 499:
                error += 1
            if url not in urls:
                urls[url] = 1
            else:
                urls[url] += 1

    logging.info("Обработка access.log завершена")
    if urls:
        most_common_url = max(urls, key=lambda x: urls[x])
    else:
        most_common_url = None

    stats = {
        "requests_by_method": tips,
        "errors_4xx": error,
        "requests_by_url": urls,
        "most_common_url": most_common_url
    }
    with open("stats.json", "w", encoding="utf-8") as file:
        json.dump(stats, file, ensure_ascii=False, indent=4)

    logging.info("Статистика сохранена в stats.json")
    print("Обработка завершена. Статистика сохранена в stats.json")

except OSError as e:
    logging.exception("Ошибка при работе с файлом: %s", e)
    print("Не удалось обработать файл:", e)


