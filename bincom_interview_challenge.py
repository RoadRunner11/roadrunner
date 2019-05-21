
'''I had to write the function on a different file first and make sure that it works, then  i copied it here'''


# define a function that loops
def bincom():
    global html_page 
    html_page ="<html><head> </head> <body>" #begin the html tag
    
    for i, j in enumerate(range(1, 1000000)): # loop between 1 and 1000000
        
        if (i+1)%3 ==0: #check for every third number
            every_third = "<i>" + str(j) + "</i>"+' '
            html_page += every_third#add the html tags
            
        elif (i+1)%10==0: #check for every tenth number
            every_tenth = "<b>" +str(j)+ "</b>" +' ' 
            html_page += every_tenth#add to the html tag
            
        is_prime = True # initiate the condition for prime
        
        for k in range(2, int(j**0.5) + 1): #set the condition for prime
            if (j % k) == 0:
                is_prime = False
                break

        if is_prime:  # check if the number in the series is prime  
            prime = "<u>" +str(j) + "</u>"+' '
            html_page += prime + "<br>" #add to the html tag

    html_page = html_page+"</body> </htlm>" #completion 
    
    with open('bincom.html', 'w') as bc: #create an html file
        bc.write(html_page) # write the html tags to the file
        
if __name__ == "__main__": #check if the file is running on its own
    bincom() # call function