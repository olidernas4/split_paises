P=input("ingrese paises:\n")
paises=[pais for pais  in P.split(',')]

print(','.join(sorted(list(set(paises)))))