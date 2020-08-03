print("\t--: Aritmetic Series :--")

def series():

    choice = str(input("Is the series Finite or Infinite? >> "))
    
    a = int(input("Enter the first term, a = "))
    d = int(input("Enter the common difference, d = "))
    n = int(input("Enter the number of terms, n = "))
    
    if choice == "Finite":
        n_terms = int(input("How many terms are to be shown? >> "))
        
        for i in range(0, n_terms):
            print(i,"+",end="...+",n_terms)

series()
