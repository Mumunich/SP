from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "17 Pro", "+79139998765"),
    Smartphone("Xiaomi", "11 Pro", "+79138887654"),
    Smartphone("Pixel", "10 Pro", "+79137776543"),
    Smartphone("Samsung", "S25 Ultra", "+79136665432"),
    Smartphone("Vivo", "X100 Pro", "+79135554321")
]

for smartphone in catalog:
    print(f"<{smartphone.mark}> - <{smartphone.model}>. {smartphone.number}")
