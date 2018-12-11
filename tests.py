import unittest
from FlaggedEnum import FlaggedEnum, auto

# uncomment the line below and change the path specified
# sys.path.insert(0, r'path_to_solution_folder')


class  MyEnum(FlaggedEnum):
    read_only = (1 << 0)
    lowercased = (1 << 2)
    immediate = (1 << 3)
    auto_field_1 = auto()
    auto_field_2 = auto()


class EnumClassTest(unittest.TestCase):

    def test_myenum(self):
        assert MyEnum.read_only.name == 'read_only'
        assert MyEnum.read_only.value == (1 << 0)
        print(MyEnum.read_only)
        assert MyEnum.get_by_name('read_only') == MyEnum.read_only
        assert MyEnum.read_only in MyEnum
        assert isinstance(MyEnum.read_only, int)
        assert isinstance(MyEnum.read_only, MyEnum)
        value = MyEnum.read_only | MyEnum.immediate
        assert value & MyEnum.read_only and value & MyEnum.immediate
        assert isinstance(value, int)
        assert isinstance(value, MyEnum)


if __name__ == '__main__':
    unittest.main()
