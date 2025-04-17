import enum


class Optiuni(enum.Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


# print(Optiuni.Rock)
# print(Optiuni.Rock.value)

ales = Optiuni(3)
print(ales)