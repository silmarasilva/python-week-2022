# Modelagem de dados
#dataclass é uma função que permite que a gente defina os nosso próprios objetos em python e esses objetos são classes de dados. Toda vez que você precisa armazenar dados em python dataclass é o jeito mais fácil que existe pra fazer isso no python3. 
# Cada cerveja tem um nome, um estilo, um sabor, uma imagem e um custo.
# Com o select e a classe com a notação do type é possível criar instruções SQL como print(select(Beer))
# Objeto brewdog é uma nova instância da classe Beer.
# Rodar um modulo no modo iterativo: python3 -i beerlog/models.py. Ele irá abrir o terminal python e iniciar o programa (rodar para testar: Beer, brewdog, dir(brewdog), browdog.cost brewdog.name) ou print(select(Beer).where(Beer.name == "Brewdog")). O SQLModel utiliza por baixo o sqlalchemy, com uma modelagem mais tranquila.

#__________________________________________________

from typing import Optional
from typing_extensions import runtime
from sqlmodel import SQLModel, Field
from sqlmodel import select
from pydantic import validator
from statistics import mean
from datetime import datetime

class Beer (SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

# O def abaixo é uma função associda à class beer, quando temos uma função associada a uma classe nós chamamos de método.

#Sempre que tivermos um @ estamos falando de um decorator que é quando você pega um código que consegue ser aplicado em cima de funções e classes

    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v

    @validator ("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean([values["flavor"], values["image"], values["cost"]])
        return int(rate)
try:
    brewdog = Beer(name="Bewdog", style ="NEIPA", flavor=6, image=8, cost=8)
except RuntimeError:
    print("Zica de mais")