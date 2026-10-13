from enum import Enum


class Unit(Enum):
    CELSIUS = "C"
    FAHRENHEIT = "F"


print("허용 값:", [u.value for u in Unit])
print("값으로 찾기:", Unit("C"), Unit("C").name)
try:
    Unit("K")
except ValueError as e:
    print("허용되지 않는 값:", e)
