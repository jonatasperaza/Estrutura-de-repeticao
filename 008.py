from typing import List

from dataclasses import dataclass

@dataclass
class Atleta:
    inscricao: int
    altura: float


atletas: List[Atleta] = (lambda dados: ([Atleta(inscricao, altura) for inscricao, altura in dados]))((int(input("Insira sua inscrição: ")), float(input("Insira sua altura: "))) for i in range(5))

altura_atletas: List[float] = (lambda atletas: ([atleta.altura for atleta in atletas]))(atletas)
media_altura: float = (lambda a: sum(altura_atletas) / len(altura_atletas))(altura_atletas)
print(atletas)
print(f"média altura: {(media_altura)}")
#atletas {inscrição: 12312, altura: 1.80}
