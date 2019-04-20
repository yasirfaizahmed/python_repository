my_string = input()
global le
class string_manipulation:
    def _init_(self):
        print("\nthis class contains some methods to manipulate a string")
    def length(self):
        sy = 0
        spa = 0
        le = 0
        sy_arr = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','[','}',']','|',';',':','"','<','<','.','>','/','?']
        for lett in my_string:
            le+=1
            for sym in sy_arr:
                if lett==sym:
                    sy+=1
            if lett==" ":
                spa+=1
        print("\nlength = ", le)
        print("\nspaces = ", spa)
        print("\nsymbols = ", sy)
    def Reverse(self, strin):
        str = ""
        for i in my_string:
            str = i + str
        return str
string = string_manipulation()
print(string.Reverse(my_string))
string.length()

