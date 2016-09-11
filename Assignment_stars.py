# Part 1
x = [4,6,1,3,5,7,25]
def draw_starsI(arr):
    for element in arr:
        output = ''
        for i in range(element):
            output += '*'
        print output 

draw_starsI(x)

# Part 2
y = [4,'Tom',1,'Michael',5,7,'Jimmy Smith']
def draw_stars2(arr):
    for element in arr:
        output = ''
        if type(element) is int:
            for i in range(element):
                output += '*'
        elif type(element) is str:
            first_letter = element[0].lower()
            for i in range(len(element)):
                output += first_letter
        print output

draw_stars2(y)