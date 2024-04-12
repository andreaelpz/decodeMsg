#approach:
#1. read the file
#2. create a dictionary with the number as key and word as value
#3. organize keys into pyramid structure
#4. use values from last number in each row (each number corresponds to a key)
#5. return decoded message

def decode(message_file):
    message_dict = createDict(message_file)
    if not message_dict:
        print("File is empty")
        return None
    pyramid = createPyramid(message_dict)
    if not pyramid:
        print("Invalid pyramid")
        return None
    decodedMsg = decodeMsg(pyramid)
    print(decodedMsg)
    return decodedMsg
         
                   
def decodeMsg(pyramid):
    message = ""
    for row in pyramid:
        message += row[-1] + " "
    return message
          
          
def createPyramid(dict):
    pyramid = [] 
    counter = 1
    nextKey = 1
    while dict:
        row = []
        for i in range(counter):
            if nextKey in dict:
                row.append(dict.pop(nextKey))
                nextKey+=1
            else:
                return None
        pyramid.append(row)
        counter+=1
    return pyramid
           
            
def createDict(file):
    message_dict = {}
    
    try:
        with open(file, 'r') as file:
            
            file.seek(0)
            
            for line in file:
                number, word = line.strip().split(' ', 1)
                number = int(number)
                message_dict[number] = word
    except FileNotFoundError:
        print("File not found")
        return None
    
    return message_dict
    
decode('msg.txt')
        