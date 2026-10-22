from csv import *
from csv import DictReader

ans = []
zag = []
with open("product.csv", 'r', encoding="UTF-8", newline='') as file:
    products = DictReader(file)
    with open("expensive.csv", "w", encoding="utf-8", newline="") as file_out:
        ans = DictWriter(file_out, fieldnames=products.fieldnames)
        ans.writeheader()

        for s in products:
            if int(s["price"]) > 100:
                ans.writerow(s)
