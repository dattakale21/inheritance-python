# 5. write a class vector representing the vector of n dimension.
#  overload the + and * operator which calculates the sum and the dot product of them.



class Vector:        # creating the class
    def __init__(self, vec):         # constructor for taking the input(vector) from the user.
       self.vec = vec
    
    def __str__(self):       #creating the string function 
        str1 = ""  
        index = 0
        for i in self.vec:        
            str1 += f" {i}a{index} +"
            index +=1
    #   return str1      # output will be 2a1 + 5a2 + 6a3 +   ---> at last one '+' will print.      
        return str1[:-1]      # to avoid the '+' at last use the string slicing, means print from -__ to -1.  

    def __add__(self,vec2):     # for adding the function.
        newList = []    # creating the empty list,afterwords i will add the vector in this list, so for now it is empty list.
        for i in range(len(self.vec)):        # for loop for adding the vector ---> this for adds the vector till the length of the vectors. means if the vectors as i,j and k then the length is 3,so add till 3.
            newList.append(self.vec[i] + vec2.vec[i])     # after adding append that added vector into the empty list, so used the append function here.
        #   return Vector(newList)    # i can also write like this line for returning the function. <---   
            # a=(newList)    # if write like this <--- then it will only add the numbers and prints, but not prints in the vector form.
            a=Vector(newList)
        return a   
    
    def __mul__(self, vec2):     # for * the vectors.
        sum = 0
        for i in range(len(self.vec)):    # it is for kutparanta jaycha ahi mala multiply karat. i.e. till the length of the vector.
            # sum = self.vec[i] * vec2.vec[i]    # if i do this then it will not add the vectors , means it will only multiply the number and prints.means here at this line the output will be 54, because 6X9=54
            sum += self.vec[i] * vec2.vec[i]     # this line is for multiplying and adding the numbers
            # return sum
        return sum    # i can't write this in the for loop because i want the final ans. like the above line.

# v1 = Vector(1, 4, 6)  # i can't write this because in __init__(self,vec) only one argument is there that is vec but i am giving 3 arguments(1,4,6) here <--- to avoid this give make one list as a argument.
v1 = Vector([1, 4, 6])     # one argument as list
v2 = Vector([1, 6, 9])
print(v1+v2)    # for adding the vectors.
print("by multiplying the vectors the ans is: ",v1*v2)    # for multiplying the vectors.
