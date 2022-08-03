# Suite définie par récurrence
# v(0)   = 3
# v(n+1) = v(n) + 2
def v(n: int) -> int:
  # valeur initiale
  v0 = 3
  # valeur finale du rang n qu'on veut calculer
  total_rang_n = v0
  # on boucle de 1 à n (0 est déja caculé !)
  for i in range(1,n+1):
    # on ajoute à la valeur précédente
    # la raison de la suite (ici, +2)
    total_rang_n = total_rang_n +2
  # Apres la boucle, on peut renvoyer le résultat final
  return total_rang_n

assert v(0) == 3
assert v(1) == 5, "V1 doit valoir 5, recu " + str(v(1))