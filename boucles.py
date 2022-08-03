
print("boucle for avec range")
# boucler de 0 à 4
for x in range(5):
  print(str(x))


print("boucle for avec tableau")
# boucler de 0 à 4 avec un tableau
tableau = [0,1,2,3,4]

for x in tableau:
  print(str(x))


print("boucle avec une condition")
# boucler tant que quelque chose est vrai
compteur = 0

while compteur < 5:
  print(str(compteur))
  # on n'oublie pas de modifier le compteur
  # sinon BOUCLE INFINIE !
  # on appelle ce genre de variable 
  # un 'variant de boucle'
  compteur = compteur +1

print("boucle avec une condition - décrémentation")
# boucler tant que quelque chose est vrai
compteur = 5

while compteur > 0:
  print(str(compteur))
  # on n'oublie pas de modifier le compteur
  # sinon BOUCLE INFINIE !
  # on appelle ce genre de variable 
  # un 'variant de boucle'
  compteur = compteur -1
