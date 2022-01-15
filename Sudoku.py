class Sudoku():
    global i,j,lista,listaAux,dim1,dim2,rangoAux
    i=0
    j=0 
    rangoAux=1
    # lista=[[7,0,0,0,2,0,4,8,0],[2,0,6,0,0,8,0,0,5],[5,0,0,9,0,0,0,0,0],[0,0,0,1,5,0,0,0,0],[0,2,0,0,0,0,0,6,0],[0,0,0,0,6,7,0,0,0],[0,0,0,0,0,6,0,0,3],[6,0,0,5,0,0,1,0,4],[0,9,3,0,4,0,0,0,7]] 
    # listaAux=[[7,0,0,0,2,0,4,8,0],[2,0,6,0,0,8,0,0,5],[5,0,0,9,0,0,0,0,0],[0,0,0,1,5,0,0,0,0],[0,2,0,0,0,0,0,6,0],[0,0,0,0,6,7,0,0,0],[0,0,0,0,0,6,0,0,3],[6,0,0,5,0,0,1,0,4],[0,9,3,0,4,0,0,0,7]] 
    lista=[[0,0,0,0,0,0,6,0,4],
    [2,0,3,5,4,6,0,0,0],
    [0,0,0,0,0,0,8,5,0],
    [0,9,0,4,0,5,0,0,0],
    [0,2,0,1,6,7,0,8,0],
    [0,0,0,8,0,2,0,7,0],
    [0,7,1,0,0,0,0,0,0],
    [0,0,0,6,7,3,9,0,5],
    [6,0,9,0,0,0,0,0,0]]
    listaAux=[[0,0,0,0,0,0,6,0,4],
    [2,0,3,5,4,6,0,0,0],
    [0,0,0,0,0,0,8,5,0],
    [0,9,0,4,0,5,0,0,0],
    [0,2,0,1,6,7,0,8,0],
    [0,0,0,8,0,2,0,7,0],
    [0,7,1,0,0,0,0,0,0],
    [0,0,0,6,7,3,9,0,5],
    [6,0,9,0,0,0,0,0,0]]
    # lista=[[6,0,0,0,0,0,0,0,1],
    # [0,2,7,0,8,0,0,0,0],
    # [0,0,0,3,9,6,0,0,0],
    # [7,0,6,0,0,0,0,0,0],
    # [0,0,1,9,3,5,9,0,0],
    # [0,0,0,0,0,0,2,0,4],
    # [0,0,0,9,6,3,0,0,0],
    # [0,0,0,0,4,0,6,5,0],
    # [3,0,0,0,0,0,0,0,2]]
    # listaAux=[[6,0,0,0,0,0,0,0,1],
    # [0,2,7,0,8,0,0,0,0],
    # [0,0,0,3,9,6,0,0,0],
    # [7,0,6,0,0,0,0,0,0],
    # [0,0,1,9,3,5,9,0,0],
    # [0,0,0,0,0,0,2,0,4],
    # [0,0,0,9,6,3,0,0,0],
    # [0,0,0,0,4,0,6,5,0],
    # [3,0,0,0,0,0,0,0,2]]
    # dim1,dim2=(9,9)
    # lista=[[ 0 for i in range (dim1)] for j in range (dim2)]

    # def rellenaMatriz():
    #     global lista,listaAux        
    #     for i in range(0,9):
    #         for j in range(0,9):
    #             print("Posicion: ",i,"-",j)
    #             num=input("Introduce numero: ") 
    #             lista[i][j]=num                
    #     listaAux=lista 

    def avanzaPosicion():
        global i,j
        if (j==8 and i==8):
            return False
        elif (j<8):
            j+=1
            return True
        elif (j==8 and i<8):
            j=0
            i+=1
            return True

    def muestraSudoku():
       for fila in range(0,9):
            for col in range(0,9):
                print(listaAux[fila][col])
            print()

           

    def compruebaLinea(n):   
        global i,j,listaAux     
        for n1 in range(0,9):            
            if (listaAux[i][n1]==n):
                return True  
            elif (n1==8):
                return False

    def compruebaColumna(n):
        global i,j,listaAux
        for n1 in range(0,9):
            if (listaAux[n1][j]==n):
                return True
            elif (n1==8):
                return False

    def compruebaCuadro(n):
        global i,j,listaAux
        if (i>=0 and i<=2 and j>=0 and j<=2):
            for n1 in range(0,3):
                for n2 in range(0,3):
                    if (listaAux[n1][n2]==n):
                        return True
                    elif (n1==2 and n2==2):
                        return False
        elif (i>=0 and i<=2 and j>=3 and j<=5):  
            for n1 in range(0,3):
                for n2 in range(3,6):
                    if (listaAux[n1][n2]==n):
                        return True
                    elif (n1==2 and n2==5):
                        return False
        elif (i>=0 and i<=2 and j>=6 and j<=8):  
            for n1 in range(0,3):
                for n2 in range(6,9):
                    if (listaAux[n1][n2]==n):
                        return True
                    elif (n1==2 and n2==8):
                        return False
        elif (i>=3 and i<=5 and j>=0 and j<=2):  
            for n1 in range(3,6):
                for n2 in range(0,3):
                    if (listaAux[n1][n2]==n):
                        return True
                    elif (n1==5 and n2==2):
                        return False
        elif (i>=3 and i<=5 and j>=3 and j<=5):  
            for n1 in range(3,6):
                for n2 in range(3,6):
                    if (listaAux[n1][n2]==n):
                        return True
                    elif (n1==5 and n2==5):
                        return False
        elif (i>=3 and i<=5 and j>=6 and j<=8):  
            for n1 in range(3,6):
                for n2 in range(6,9):
                    if (listaAux[n1][n2]==n):
                        return True
                    elif (n1==5 and n2==8):
                        return False
        elif (i>=6 and i<=8 and j>=0 and j<=2):
            for n1 in range(6,9):
                for n2 in range(0,3):
                    if (listaAux[n1][n2]==n):
                        return True
                    elif (n1==8 and n2==2):
                        return False
        elif (i>=6 and i<=8 and j>=3 and j<=5):
            for n1 in range(6,9):
                for n2 in range(3,6):
                    if (listaAux[n1][n2]==n):
                        return True
                    elif (n1==8 and n2==5):
                        return False
        elif (i>=6 and i<=8 and j>=6 and j<=8):
            for n1 in range(6,9):
                for n2 in range(6,9):
                    if (listaAux[n1][n2]==n):
                        return True
                    elif (n1==8 and n2==8):
                        return False                                                                                                                          
        else:
            return True 

    def retrocedePosicion():
        global i,j,listaAux,rangoAux,lista
        if (j==0 and i>0):
            j=8
            i-=1
            if (lista[i][j]>0):
                Sudoku.retrocedePosicion()
            else:
                if (listaAux[i][j]==9):
                    listaAux[i][j]=0                   
                    Sudoku.retrocedePosicion()
                else:
                    rangoAux=listaAux[i][j]+1
                return True            
        elif (i==0 and j==0):
            return False  
        else:
            j-=1
            if (lista[i][j]>0):
                Sudoku.retrocedePosicion()
            else:
                if (listaAux[i][j]==9): 
                    listaAux[i][j]=0                     
                    Sudoku.retrocedePosicion()
                else:
                    rangoAux=listaAux[i][j]+1

    def sirveCandidato():           
        global i,j,lista,listaAux,rangoAux 
        continuar=True
        while (continuar==True):                     
            if (lista[i][j]>0):
                if (Sudoku.avanzaPosicion()==False):
                    continuar=False
                    Sudoku.muestraSudoku()                                      
            else:
                for n in range(rangoAux,10):                                                      
                    if (Sudoku.compruebaLinea(n)==False):
                        if (Sudoku.compruebaColumna(n)==False):
                            if (Sudoku.compruebaCuadro(n)==False):
                                listaAux[i][j]=n                                
                                rangoAux=1
                                n=1
                                print("Calculando posicion ",i,"-",j)
                                if (Sudoku.avanzaPosicion()==False):
                                    continuar=False
                                    Sudoku.muestraSudoku()
                                break
                    if (n==9):
                        listaAux[i][j]=0
                        if(Sudoku.retrocedePosicion()==False):
                            print("No se puede resolver el Sudoku. Error en la posicion " +i+";"+j) 
# Sudoku.rellenaMatriz()                        
Sudoku.sirveCandidato()

   
           
               



   


    
    

                   

                     


    

   


