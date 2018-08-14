formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "两个黄鹂鸣翠柳",
    "一行白鹭上青天",
    "窗含西岭千秋雪",
    "门泊东吴万里船"
))