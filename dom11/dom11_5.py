class SuperStr(str):

    def is_repeatance(self, s):
        if self == "":
            return False

        len_self = len(self)
        len_s = len(s)

        if len_self % len(s) != 0:
            return False
        repeat = len_self // len(s)
        repeat_s_string = s * repeat
        if self == repeat_s_string:
            return True

    def is_palindrom(self):
        if self == "":
            return True
        return self.lower() == self.lower()[::-1]


my_str = SuperStr("ahahahahaha")
print(my_str.is_repeatance("ah"))
print(my_str.is_palindrom())
