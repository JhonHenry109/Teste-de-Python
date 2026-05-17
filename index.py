alunos = [
    ("Joao", 7, 8),
    ("Maria", 6, 5),
    ("Pedro", 9, 10),
    ("Ana", 4, 6),
    ("Lucas", 8, 7),
    ("Julia", 5, 5),
    ("Carlos", 10, 9),
    ("Mariana", 6, 7),
    ("Gabriel", 3, 4),
    ("Larissa", 8, 8),
    ("Rafael", 7, 6),
    ("Beatriz", 9, 9),
    ("Bruno", 2, 5),
    ("Camila", 6, 6),
    ("Felipe", 10, 10),
    ("Isabela", 5, 7),
    ("Gustavo", 8, 9),
    ("Amanda", 4, 5),
    ("Diego", 7, 7),
    ("Leticia", 6, 8),
    ("Rodrigo", 9, 6),
    ("Fernanda", 3, 3),
    ("Eduardo", 8, 7),
    ("Patricia", 5, 6),
    ("Thiago", 7, 9),
    ("Vanessa", 10, 8),
    ("Leonardo", 4, 4),
    ("Aline", 6, 7),
    ("Matheus", 9, 10),
    ("Carolina", 5, 8)
]

for nome, n1, n2 in alunos:
    media = (n1 + n2) / 2
    
    if media >= 7:
        print(nome, "teve a media de", media, "Aprovado")
    else:
        print(nome, "teve a media de", media, "Reprovado")

    if media >= 7:
        with open("aprovados.csv", "a") as arquivo:
            arquivo.write(f"nome:  {nome}, teve a media de, {media}, aprovado.\n")
    else:
        with open("reprovados.csv", "a") as arquivo:
            arquivo.write(f"nome:  {nome}, teve a media de, {media}, reprovado.\n")