emp=["Sagar",102,"USA"]
Dep1=["CS",10]
Dep2=["IT",20]
HOD_CS=[10,"Mr.Kapadnis"]
HOD_IT=[20,"Mr.Bhadane"]
print("printing employee data...")
print("Name:%s,Id:%d,Country:%s"%(emp[0],emp[1],emp[2]))
print("printing department...")
print("Department 1:\nName:%s,Id:%d\nName:%s,,Id:%d"%(Dep1[0],Dep1[1],Dep2[0],Dep2[1]))
print("HOD details...")
print("CS HOD Name:%s,Id:%d"%(HOD_CS[1],HOD_CS[0]))
print("IT HOD Name:%s,Id:%d"%(HOD_IT[1],HOD_IT[0]))
print(type(emp),type(Dep1),type(Dep2),type(HOD_CS),type(HOD_IT))