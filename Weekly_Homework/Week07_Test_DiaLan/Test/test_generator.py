import os
import random
root = os.getcwd()
input_dest = 'input'
output_dest = 'output'
for i in range(15):
    file_name = str(i+1)+'.txt'
    if i+1 == 1:
        result = 'YES'
        n,k = 3,2
        test = [5,4,3]
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)
    if i+1 == 2:
        result = 'YES'
        n,k = 1,1
        test = [0]
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)
    if i+1 == 3:
        result = 'NO'
        n,k = 1,1
        test = [1]
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)
    if i+1 == 4:
        result = 'YES'
        n,k = 200000, 200000
        test = [random.randint(0,4096) for _ in range(199999)]
        test.append(0)
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)
    if i+1 == 5:
        result = 'NO'
        n,k = 200000,200000
        test = [random.randint(2048,4096) for _ in range(200000)]
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)
    if i+1 == 6:
        result = 'YES'
        n,k = 200000,13
        test = [random.randint(0,4095) for _ in range(199999)]
        test.append(0)
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)
    if i+1 == 7:
        result = 'NO'
        n,k = 200000,13
        test = [random.randint(2048,4095) for _ in range(200000)]
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)
    if i+1 == 8:
        result = 'YES'
        n,k = 200000,2
        test = [random.randint(0,4096) for _ in range(199999)]
        test.append(0)
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)
    if i+1 == 9:
        result = 'NO'
        n,k = 200000,2
        test = [random.randint(2048,4096) for _ in range(200000)]
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)
    if i+1 == 10:
        result = 'YES'
        n,k = 200000,12
        test = [random.randint(0,4096) for _ in range(199999)]
        test.append(0)
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)
    if i+1 == 11:
        result = 'NO'
        n,k = 200000, 12
        test = [random.randint(2048,4096) for _ in range(200000)]
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)
    if i+1 == 12:
        result = 'YES'
        n,k = 200000,2
        test = [random.randint(1,4095) for _ in range(199998)]
        test.append(3)
        test.append(4092)
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)
    if i+1 == 13:
        result = 'NO'
        n,k = 200000, 2
        test = [random.choice([4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) for _ in range(199999)]
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)
    if i+1 == 14:
        result = 'YES'
        n,k = 200000,12
        test = [random.randint(2,4095) for _ in range(199998)]
        test.append(4903)
        test.append(2)
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)
    if i+1 == 15:
        result = 'NO'
        n,k = 200000, 12
        test = [random.choice([4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]) for _ in range(199999)]
        with open(os.path.join(root,input_dest,file_name),'w+') as f:
            f.writelines(' '.join(map(str,[n,k])))
            f.writelines('\n')
            f.writelines(' '.join(map(str,test)))
        with open(os.path.join(root,output_dest,file_name),'w+') as f:
            f.writelines(result)