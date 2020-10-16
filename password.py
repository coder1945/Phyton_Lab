def clave(password):

        validar=False 
        long=len(password) 
        espacio=False  
        mayuscula=False 
        minuscula=False 
        numeros=False 
        y=password.isalnum()
        correcto=True 
        
        for carac in password: 

            if carac.isspace()==True: 
                espacio=True 

            if carac.isupper()== True: 
                mayuscula=True 
                
            if carac.islower()== True: 
                minuscula=True 
                
            if carac.isdigit()== True: 
                numeros=True 
                            
        if espacio==True: 
                print("La contraseña tiene espacios")
        else:
            validar=True 
                       
        if long <8 and validar==True:
            print("Mínimo 8 caracteres")
            validar=False 

        if mayuscula == True and minuscula ==True and numeros == True and y== False and validar ==True:
           validar = True 
        else:
           correcto=False 
           
        if validar == True and correcto==False:
           print("La clave debe tener minúsculas, mayúsculas, números y por lo menos 1 carácter especial...")

        if validar == True and correcto ==True:
           return True
