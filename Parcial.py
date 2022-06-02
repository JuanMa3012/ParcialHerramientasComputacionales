#Andres Camilo Guzman
#Juan Manuel Hurtado

def cafeteria():

    m = [[101,3000], [102,9000], [103,4500], [104,1200], [105,4000], [106,2500], [107,1000], [108,2000], [109,3000]]
    personas = int(input("¿Cuantas personas hay en la fila?: "))
    print()
    p = 0
    while p < personas:
        print("###################################")
        print("#Bienvenido a la Cafeteria Central#")
        print("###################################")
        print()
        print("########################################")
        print("#          Nuestro menú es             #")
        print("# 1. Gaseosa(101) -----> 3000          #")
        print("# 2. Almuerzo(102) -----> 9000         #")
        print("# 3. Salchipapa(103) ----> 4500        #")
        print("# 4. Dedo(104) -----> 1200             #")
        print("# 5. Jugo natural(105) -----> 4000     #")
        print("# 6. Pastel de pollo(106) ---> 2500    #")
        print("# 7. Cheetos(107) ----> 1000           #")
        print("# 8. Consome(108) ----> 2000           #")
        print("# 9. Helado(109) -----> 3000           #")
        print("########################################")
        print()
        codigo = int(input("Ingrese el codigo del producto que desea llevar: "))
        print()
        valorP = 0
        cantidad = int(input("Cuantos productos desea llevar: "))
        lP = [(codigo,cantidad)]
        lC = [codigo]
        print()
        print("¿Desea llevar mas productos?")
        mas = input()
        print()
        while mas != "No":
            c2 = int(input("Ingrese el otro codigo del producto que desea llevar: "))
            lC.append(c2)
            print()
            cant2 = int(input("Cuantos productos desea llevar: "))
            lP.append((c2,cant2))
            print()
            print("¿Desea llevar mas productos?")
            mas = input()
            print()
        for j in range(len(lP)):
            i = 0
            ans = False
            while not ans and i < len(m):
                if lP[j][0] in m[i]:
                    valorP += (m[i][1] * lP[j][1])
                    ans = True
                i += 1   
        print()
        print("##################################################")
        print("#  ¿Cual es su rol en la Universidad Javeriana?  #")
        print("#  -Profesor                                     #")
        print("#  -Estudiante                                   #")
        print("##################################################")
        print()
        rol = input()
        cedula = input("Ingrese su cedula: ")
        print()
        if rol == "Estudiante":
            print("¿Es del programa de becas?")
            res = input()
            if res == "Si":
                desc = (50 * valorP) / 100
                valorF = valorP - desc
                valorF = int(valorF)
            else:
                desc = (30 * valorP) / 100
                valorF = valorP - desc
                valorF = int(valorF)
        else:
            desc = (20 * valorP) / 100
            valorF = valorP - desc
            valorF = int(valorF)
        if len(lC) == 1:
            print("El",rol,"con cedula",cedula,"debe pagar",valorF,"por el producto",lC[0])
        else:
            print("El",rol,"con cedula",cedula,"debe pagar",valorF, "por los productos:",lC[0],end = ",")
            for i in range(1,len(lC)):
                if i == len(lC) - 1:
                    print(lC[i])
                else:
                    print(lC[i], end = ",")
        print()
        p += 1

cafeteria()
