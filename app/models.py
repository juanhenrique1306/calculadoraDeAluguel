from dataclasses import dataclass
from enum import Enum


class TipoImovel(str, Enum):
    APARTAMENTO = "apartamento"
    CASA = "casa"
    ESTUDIO = "estudio"


@dataclass
class Orcamento:
    tipo: TipoImovel
    quartos: int = 1
    tem_garagem: bool = False
    tem_criancas: bool = True
    vagas_estudio: int = 0
