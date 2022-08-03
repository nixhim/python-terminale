
# -- Suite explicite
# u(n) = 2n+5
def u(n: int) -> int:
  return 2*n+5

assert u(0) == 5
assert [u(0), u(1), u(2)] == [5,7,9]

# -- Calculer les x premiers termes de la suite...

def calcul_x_premiers_termes_u(combien: int):
  tableau_termes = []
  for i in range(combien):
    tableau_termes.append(u(i))
  return tableau_termes;

assert calcul_x_premiers_termes_u(0) == []
assert calcul_x_premiers_termes_u(1) == [5]
assert calcul_x_premiers_termes_u(3) == [5,7,9]