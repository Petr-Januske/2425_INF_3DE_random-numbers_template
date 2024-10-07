import random

def generate_sequence(n):

    return [random.randint(1,100) for _ in range(n)]

# Otestování funkce
generate_sequence(10)  # Vygeneruje 10 náhodných čísel
