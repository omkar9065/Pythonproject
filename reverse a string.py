class MyClass:
    def get_String(self):
        self.myStr=input("Enter any String: ")
    def Reverse_String(self):
        s=self.myStr
        cnt=len(s)
        i=cnt-1
        revStr=""
while(i>=0):
        revStr=revStr + s[i]
        i=i-1
        print("String in Reverse:" , revStr)