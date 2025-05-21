from core.database import SessionLocal
from models.winx import Winx
from models.mundos import MundoMagico

# Cria uma nova sessão
db = SessionLocal()

# Cria o mundo mágico de Magix (ou qualquer outro)
magix = MundoMagico(nome="Magix", descricao="Centro do universo mágico", habitado_por="Fadas, bruxas e especialistas")
db.add(magix)
db.commit()
db.refresh(magix)

# Lista de Winx com dados mágicos
winx_fadas = [
    Winx(
        nome="Bloom",
        poder_principal="Chama do Dragão",
        transformacao_favorita="Enchantix",
        planeta_origem="Domino",
        mundo_id=magix.id
    ),
    Winx(
        nome="Stella",
        poder_principal="Luz do Sol",
        transformacao_favorita="Cosmix",
        planeta_origem="Solaria",
        mundo_id=magix.id
    ),
    Winx(
        nome="Flora",
        poder_principal="Natureza",
        transformacao_favorita="Harmonix",
        planeta_origem="Linféia",
        mundo_id=magix.id
    ),
    Winx(
        nome="Tecna",
        poder_principal="Tecnologia",
        transformacao_favorita="TecnoMagix",
        planeta_origem="Zênith",
        mundo_id=magix.id
    ),
    Winx(
        nome="Musa",
        poder_principal="Música",
        transformacao_favorita="Melodix",
        planeta_origem="Melody",
        mundo_id=magix.id
    ),
    Winx(
        nome="Aisha (Layla)",
        poder_principal="Fluido",
        transformacao_favorita="Sirenix",
        planeta_origem="Andros",
        mundo_id=magix.id
    )
]

# Adiciona todas no banco
db.add_all(winx_fadas)
db.commit()
db.close()

print("✨ Banco populado com as Winx! Voa, fada!") 
