##us1/create registro
users =[]
def createUser():
    user =[]
    id= int(input("Ingrese su documento de identidad"))
    user.append(id)
    user_name= input("Ingrese su nombre")
    user.append(user_name)
    user_last_name = input("Ingrese su apellido")
    user.append(user_last_name)
    user_email= input("Ingrese su correo electronico")
    user.append(user_email)
    phone = input("Ingrese su número de telefono")
    user.append(phone)
    user_password=input("Ingrese su contraseña")
    user.append(user_password)
    users.append(user)

createUser()
createUser()
createUser()
createUser()
print(users)