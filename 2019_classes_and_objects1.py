class my_class:
    def __init__(self):
        print("\nThis from my_class/_init")
    def first_method(self):
        print("\nfrom my_class/first_method")
    def second_method(self):
        print("\nfrom my_class/second_method")
class others_class:
    def __init__(my_class):
        print("\nfrom others_class/_init")
    def others_first_method(self):
        print("\nfrom others_class/others_first_method")
    def others_second_method(self):
        print("\nfrom others_class/others_second_method")
m = my_class()
m.first_method()
m.second_method()

o = others_class()
o.others_first_method()
o.others_second_method()