

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    
   shape = input("Shape?: ")

   shape = shape.lower()
   while(shape != "pyramid" and shape != "square" and shape != "triangle" and  shape != "rhombus" and shape != "rectangle" and shape != "parallelogram"):
        shape = input("Shape?: ") 
    
   return shape
           

# TODO: Step 1 - get height (it must be int!)
def get_height():
    
    height = -1

    while(height > 80 or height < 0 ):
        height = input("Height?: ")
        if height.isdigit():
            height = int(height)
        else:
            height = -1

    return height

# TODO: Step 2
def draw_pyramid(height, outline):
    
    if outline:
        n = height -1
        for i in range(height):
         for s in range(n):
            print(end=" ")
         n = n - 1
         for j in range(2*i + 1):
            if (i == 0 or i == height - 1 or j == 0 or j == ((2*i +1)-1)):
                print("*",end="")
            else:
                print(" ",end="")

         print()
    else:        
        n = height -1
        for i in range(height):
            for s in range(n):
                print(end=" ")
            n = n - 1
            for j in range(2*i + 1):
                print("*",end="")
                     
            print()

  
    
# TODO: Step 3
def draw_square(height, outline):
    

    if outline:
        for i in range(height):
             for j in range(height):
                 if(i == 0 or i == height - 1  or j == 0 or j == height - 1):
                    print("*", end="")
                 else:
                    print(" ", end="")
             print()
            
    else:                
        for i in range(height) :
             for j in range(height) :
                 print("*", end="")
             print()
    
# TODO: Step 4
def draw_triangle(height, outline):
    
    if outline:
        for i in range(0, height):
            for j in range(0, i+1):
                if(i == 0 or  i == height - 1 or j == 0 or j == i+1 -1):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()        
    else:
        for i in range(0, height) :
         for j in range(0, i+1):
            print("*",end="")
         print()

#Step 6, Additional Shapes :

# first additional shape
def draw_rhombus(height, outline):
    if outline:
        n = (2 * height) - 1
        for i in range(0, height):
            for s in range(0, n):
                print(end=" ")
            n = n - 1
            for j in range(0, height):
                if(i == 0 or i == height - 1 or j == 0 or j == height - 1):
                   print("*", end="")
                else:
                    print(" ",end="")
            print()
    else:
        n = (2 * height) - 1
        for i in range(height):
            for s in range(0, n):
             print(end=" ")
            n = n - 1
            for j in range(height):
               print("*",end= "")
        
            print()

#Second additional shape
def draw_rectangle(height, outline):
    if outline:
        for i in range(height):
            for j in range(2*height):
                if (i == 0 or i == height - 1 or j == 0  or j == 2*height - 1): 
                     print("*",end="") 
                else:
                    print(" ",end="")
            print()
    else:
        for i in range(height):
            for j in range(2*height):
             print("*",end="") 
            print()

#Third additional shape
def draw_parallelogram(height, outline):
        
        if outline:
            n = (2 * height) - 1
            for i in range(height):
                for s in range(n):
                    print(end=" ")
                n = n - 1
                for j in range(2*height):
                    if (i == 0 or i == height or j == 0 or j == 2*height):
                        print("*",end="")
                    else:
                        print("",end="")
                print()
        else:
            n = (2 * height) - 1
            for i in range(height):
                for s in range(n):
                    print(end=" ")
                n = n - 1
                for j in range(2*height):
                     print("*", end="")
                print()
        


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):

    if shape == 'pyramid' :
        draw_pyramid(height, outline)

    if shape == 'square' :
        draw_square(height, outline)

    if shape == 'triangle' :
        draw_triangle(height, outline)

    if shape == 'rhombus' :
        draw_rhombus(height, outline)

    if shape == 'rectangle' :
        draw_rectangle(height, outline)

    if shape == 'parallelogram' :
        draw_parallelogram(height, outline)
    


   


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():

    outline_param = (input("Outline only? (y/N): "))
    if outline_param == "y":   
        return True
    else:
        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

