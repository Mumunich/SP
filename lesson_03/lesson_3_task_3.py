from Address import Address
from Mailing import Mailing

to_address = Address(
    index="101000",
    city="Москва",
    street="Тверская",
    house="15",
    apartment="42"
)

from_address = Address(
    index="197101",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="120",
    apartment="8"
)

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="TR123456789RU"
)

print(f"Отправление {mailing.track} из {mailing.from_address} "
      f"в {mailing.to_address}. Стоимость {mailing.cost} рублей.")
