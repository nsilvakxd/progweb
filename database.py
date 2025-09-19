# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Define a string de conexão com o banco PostgreSQL.
#    Formato: "postgresql://<user>:<password>@<host>/<dbname>"
#    Substitua com suas credenciais. É uma boa prática usar variáveis de ambiente aqui.
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost/progwebIII"

# 2. Cria a "engine" do SQLAlchemy, que é o ponto de entrada para o banco de dados.
#    Ela gerencia as conexões com o banco.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 3. Cria uma fábrica de sessões (SessionLocal). Cada instância de SessionLocal
#    será uma sessão com o banco de dados. Pense nela como uma "conversa" temporária.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Cria uma classe Base. Nossos modelos de tabela do SQLAlchemy herdarão desta
#    classe para que o ORM possa gerenciá-los.
Base = declarative_base()