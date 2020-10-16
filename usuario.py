def nickname(alias):

        long=len(alias) 
        y=alias.isalnum()
        
        if y== False: 
            print("El nombre de usuario debe tener solo letras y números")
            
        if long < 6: 
            print("El nombre de usuario debe tener por lo menos de 6 carácteres")
            
        if long > 12: 
            print("El nombre de usuario no puede contener más de 12 caracteres")
            
        if long >5 and long <13 and y ==True:
            return True 
