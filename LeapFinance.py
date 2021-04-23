import time
from time import sleep
from threading import *

record={}                    #Maintain the json data in the form of python dictionary object
memoryLimit=1024*1024*1024   #memory limit given 1GB
valuesize=16*1024            #value size limit give 1KB


#create function to do the create operation
def create(key,value,timeout=0):
    if key in record:
        print("Error: Key already exists. Can't do create operation on this key")
        return
    #input key contraint check i.e. capped at 32 chars
    if len(key)>32:
        print("Error: Key maximum length 32 chars")
        return
    if type(key)==str:
        
        #constraint check on record file size and must be less than 1GB
        if len(record)>memoryLimit:           
            print("Error: Memory limit exceeded")
            return
        
        #constraint check on value size and must be less than 16KB
        if len(value)>valuesize:
            print("Error: value size limit exceeded")
            return
        
        #If all constraints are passed (Optional)
        if timeout==0:
            data=[value,timeout]
        else:
            data=[value,time.time()+timeout]
        
        #data has stored correspond to the given key
        record[key]=data
    else:
        print("Error: Key must contain only alphabets")
        
        
# reading operation       
def read(key):
    if key not in record:
        print("Error: Key doesn't exists")
        return
    #If timeout for a particular key is 0
    if record[key][1]==0:
        print(str(key)+" : "+str(record[key][0]))
    #If current time exceeds the timeout corresponding to the key
    if time.time() > record[key][1]:
        print("Time to live has expired for the key ",key)
        return
    print(str(key)+" : "+str(record[key][0]))


#Delete operation
def delete(key):
    if key not in record:
        print("Error: Key doesn't exists")
        return
    #if timeout is 0 or the timeout is greater than the current time
    if record[key][1]==0 or record[key][1]>time.time():
        del record[key]
        print("Delete operation successful on key ",key)
        return
    
    print("Time to live has expired for the key ",key)
    
    
    
create("Sahil","10000",2)
create("Rajat","10393",10)
create("Sahil","10000")
delete("Rajat")
read("Sahil")
read("Rajat")
delete("Sahil")

        
#Making threads as per need of operations

'''thread1=Thread(target=(create,delete,read),args=(keys[i],values[i],timeout))
thread1.start()
sleep()
thread2=Thread(target=(create,delete,read),args=("b",20,0))
thread2.start()'''


    
    
    
    

            
        
            