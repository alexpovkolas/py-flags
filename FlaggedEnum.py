from enum import IntFlag, auto


def verify(enumeration):
    for name, member in enumeration.__members__.items():
        if name != member.name:
            ValueError('Duplicated value')

    return enumeration


@verify
class FlaggedEnum(IntFlag):

    @classmethod
    def get_by_name(cls, name):
        return cls[name]

    def __str__(self):
        return str(self.name) + ": " + str(self.value)

    def __iter__(self):
        return self.__members__.items()



