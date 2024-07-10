class Test:
    count_obj=1
    def __init__(self,name=None):
        Test.count_obj+=1
        self.name = name
    
t1=Test("Abhi")
t2=Test("ANkit")
t3=Test("Preeti")

print(Test.count_obj)
