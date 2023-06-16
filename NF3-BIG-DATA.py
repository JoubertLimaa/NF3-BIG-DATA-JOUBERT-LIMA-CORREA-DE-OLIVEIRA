#EXERCÍCO FINAL DE BIG DATA.
#ALUNO - JOUBERT LIMA CORRÊA DE OLIVERIA - 202102283388
#PROFESSOR(A) - SIMONE GAMA

             #QUESTÃO 1-

#LETRA A - 
import pandas as pd
df = pd.read_csv('world_alcohol.csv', sep=',')
bebidas = df.groupby('Beverage Types')

for b, g in bebidas:

    print(f"Beverage Types: {g}")

    print(b,"\n")
    
#--------------.----------------

#LETRA B-
import pandas as pd
df = pd.read_csv('world_alcohol.csv',sep = ',')
reg= df.groupby('WHO region')
ano=df.groupby('Year')

for r, g in reg:
    print(f"{g}")
    print(r,'\n')
    
for a, g in reg:
    print(f"{g}")
    print(a,'\n')

#-------------.--------------   

#LETRA C - 
import pandas as pd
df = pd.read_csv('world_alcohol.csv', sep = ',')
rg = df['WHO region'].value_counts() 


ps = df['Country'].value_counts()
print(rg)
print()
print(ps)

soma_c = df['Display Value'].sum()
print(f'Soma:{soma_c:.2f}')

#-------------.-----------------

#LETRA D -
import pandas as pd
import matplotlib.pyplot as plt

df = pd. read_csv("world_alcohol.csv",sep = ',')

media = df['Display Value'].mean()
print(f'Media:{media:.2f}')
moda = df['Display Value'].mode()[0]
print("Moda:",moda)
mediana = df['Display Value'].median()
print(f'Mediana:{mediana:.2f}')

es_des = df['Display Value'].describe()
print("Estatíscas Descritivas:")
print(es_des)

#---------------.---------------------

#LETRA E - 
import pandas as pd
df = pd.read_csv("world_alcohol.csv",sep = ',')

ano1985 = df.loc[df['Year'] == 1985]['Beverage Types']
maiorq4 = df.loc[df['Display Value'] > 4]['WHO region']
print("Bebidadas 1985")
print(ano1985)


print("Regiões com bebidas maior que 4")
print(maiorq4)

#----------------.------------------




                        #QUESTÃO 2 --
                        
#LETRA A --
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/JoubertLimaa/datasets/main/cursos-prouni.csv", sep = ",")
df = df.fillna(0.0)
print(df)
#---------------.--------------------

#LETRA B --
import pandas as pd
df= pd.read_csv("https://raw.githubusercontent.com/JoubertLimaa/datasets/main/cursos-prouni.csv",sep = ",")
bach  = df.loc[df['grau']== "Bacharelado"]
licen = df.loc[df['grau']== "Licenciatura"]
tec =df.loc[df['grau']== "Tecnológico"]

print (bach)
print(licen)
print(tec)

#-----------------.-------------

#LETRA C --
import pandas as pd
df= pd.read_csv("https://raw.githubusercontent.com/JoubertLimaa/datasets/main/cursos-prouni.csv",sep = ",")
med = df.loc[df['curso_busca'] == "Medicina"]
enfe= df.loc[df['curso_busca'] == "Enfermagem"]
peda= df.loc[df['curso_busca'] == "Pedagogia"]

print(med,"\n")
print(enfe,"\n")
print(peda)

#-----------------.---------------------

#LETRA D --
import pandas as pd
df= pd.read_csv("https://raw.githubusercontent.com/JoubertLimaa/datasets/main/cursos-prouni.csv",sep = ",")
md= df.groupby("uf_busca")["nota_integral_ampla"].mean()
print("Estados e médias de notas de corte:",md)

#----------------------.----------------

#LETRA E --
import pandas as pd
df= pd.read_csv("https://raw.githubusercontent.com/JoubertLimaa/datasets/main/cursos-prouni.csv",sep = ",")
agpcursos = df.loc[df['grau']=='Tecnológico']
print(agpcursos)

#-----------.------------------------

#LETRA F --
import pandas as pd
df= pd.read_csv("https://raw.githubusercontent.com/JoubertLimaa/datasets/main/cursos-prouni.csv",sep = ",")
remover = df.drop("cidade_filtro",axis = 'columns')
print(remover)

#------------------.------------------

#LETRA G --
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/JoubertLimaa/datasets/main/cursos-prouni.csv",sep = ",")
mediamensal= df.loc[df['curso_busca'] == 'Medicina']['mensalidade'].mean()
print(f"Média de Mensalidades de Medicina:{mediamensal:.3f}")

#----------------.------------------------

#LETRA H
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/JoubertLimaa/datasets/main/cursos-prouni.csv",sep = ",")
med_notacorte_curs_de_tint = df.loc[df['turno'] == 'Integral']['nota_integral_ampla'].mean()
print(f'Média de nota de corte dos curos de tempo integral:{med_notacorte_curs_de_tint:.3f}')

#--------------.------------------------

#LETRA I --
import pandas as pd
df =pd.read_csv("https://raw.githubusercontent.com/JoubertLimaa/datasets/main/cursos-prouni.csv",sep = ",")
estatisicas_desc= df.loc[df['grau'] == 'Bacharelado']['nota_integral_ampla'].describe()
print('Estatiscas Descritivas:'+'\n', estatisicas_desc)

#-------------.------------------------

#LETRA J --
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("https://raw.githubusercontent.com/JoubertLimaa/datasets/main/cursos-prouni.csv", sep=",")
    

grau_c = df.groupby('grau')['nota_integral_ampla'].mean()
print(grau_c)
plt.figure(figsize=(15,10))

plt.barh(grau_c.index, grau_c)
plt.xlabel('NOTAS')
plt.ylabel('CURSOS')
plt.title('COMPARAÇÃO')

plt.show()


#------------------------------.---------------------------------------------------------