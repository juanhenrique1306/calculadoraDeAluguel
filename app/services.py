import csv
from app.models import Orcamento, TipoImovel


class CalculadoraOrcamento:
    CONTRATO_TOTAL = 2000.0
    MAX_PARCELAS_CONTRATO = 5

    def calcular_mensal(self, o: Orcamento) -> float:
        if o.tipo == TipoImovel.APARTAMENTO:
            mensal = 700.0
            if o.quartos == 2:
                mensal += 200.0
            if o.tem_garagem:
                mensal += 300.0
            if not o.tem_criancas:
                mensal *= 0.95
            return mensal

        if o.tipo == TipoImovel.CASA:
            mensal = 900.0
            if o.quartos == 2:
                mensal += 250.0
            if o.tem_garagem:
                mensal += 300.0
            return mensal

        # Estúdio
        mensal = 1200.0
        # 2 vagas = 250; extras = 60 cada
        if o.vagas_estudio >= 2:
            mensal += 250.0
            extras = o.vagas_estudio - 2
            if extras > 0:
                mensal += extras * 60.0
        # Se 0 ou 1 vaga, o PDF não define; então fica sem adicional.
        return mensal

    def contrato_total(self) -> float:
        return self.CONTRATO_TOTAL

    def contrato_parcela(self, parcelas: int) -> float:
        p = max(1, min(parcelas, self.MAX_PARCELAS_CONTRATO))
        return self.CONTRATO_TOTAL / p


class CsvExporter:
    def exportar_12_meses(self, filepath: str, valor_mensal: float) -> None:
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["parcela", "valor"])
            for i in range(1, 13):
                writer.writerow([i, f"{valor_mensal:.2f}"])
