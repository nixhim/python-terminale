
# Programme pour générer la suite de Fibonacci en utilisant la récursivité
def fibonacci(n):
  # condition de fin de récursion
  if(n <= 1):
      return n
  # calcul de l'élement suivant
  else:
      return (fibonacci(n-1) + fibonacci(n-2))