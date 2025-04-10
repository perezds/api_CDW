from core.configs import DBBaseModel
from core.database import engine
from models import winx, mundos, transformacao, episodio, poder, vilao

def create_tables() -> None:
    print("🔧 Criando tabelas do banco do Clube das Winx...")

    DBBaseModel.metadata.drop_all(bind=engine)
    DBBaseModel.metadata.create_all(bind=engine)

    print("✅ Tabelas criadas com sucesso! Que a magia comece! ✨")

if __name__ == "__main__":
    create_tables()
