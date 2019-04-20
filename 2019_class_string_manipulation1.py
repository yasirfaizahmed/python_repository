print("enter a sentence:")
my_string = input()
global le
class string_manipulation:
    def _init_(self):
        print("\nthis class contains some methods to manipulate a string")

    def length(self, strin):
        le = 0
        for lett in my_string:
            le+=1
        return le

    def Reverse(self, strin):
        str = ""
        for i in my_string:
            str = i + str
        return str

    def spaces(self, strin):
        spa = 0
        for lett in my_string:
            if lett==" ":
                spa+=1
        return spa

    def symbols(self, strin):
        sy = 0
        sy_arr = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '[', '}', ']', '|', ';',
                  ':', '"', '<', '<', '.', '>', '/', '?']
        for lett in my_string:
            for sym in sy_arr:
                if lett==sym:
                    sy+=1
        return sy


