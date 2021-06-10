import connect;
#connect.deleteall()
#array = [['test1','2021-05-15','happy'],['test2','2021-05-16','excited'],['test3','2021-04-15','stoked']]
#connect.insert(array);
array2 = connect.read();
for x in array2:
    print(x)