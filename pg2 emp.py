 #employee bonus
 #swetha
def bonus(s,sr):
    amt=0
    if s>3:
        if sr<60000:
            amt= sr*0.05
        else:
            amt= sr*0.10

    if amt>0:
        return amt
    else:
        return "employee not eligible"
sal=int(input('enter salary'))
ser=int(input('enter period of service'))
res=bonus(ser,sal)
print(res)
