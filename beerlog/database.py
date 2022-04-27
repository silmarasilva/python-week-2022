# Quando mais você conseguir separar as coisas (desacoplar) pelo domínio mais fácil será para manter no futuro. O ideal é fazer em outro módulo.

# A função create_engine cria um objeto que consegue se comunicar com o banco de dados.

#sqlite é um banco de dados que funciona na base de arquivo

from sqlmodel import create_engine
from beerlog.config import settings
from beerlog import models

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)



