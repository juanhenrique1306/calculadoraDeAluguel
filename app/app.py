import os
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from models import Orcamento, TipoImovel
from services import CalculadoraOrcamento, CsvExporter

app = Flask(__name__)
app.secret_key = "dev-secret"  # ok para trabalho local

calc = CalculadoraOrcamento()
csv_exporter = CsvExporter()

EXPORT_DIR = os.path.join(os.path.dirname(__file__), "exports")
os.makedirs(EXPORT_DIR, exist_ok=True)


def _to_bool(value: str) -> bool:
    return value in ("on", "true", "1", "yes", "sim")


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/orcamento")
def gerar_orcamento():
    tipo_str = request.form.get("tipo", "apartamento").strip().lower()

    try:
        tipo = TipoImovel(tipo_str)
    except ValueError:
        flash("Tipo de imóvel inválido.")
        return redirect(url_for("index"))

    quartos = int(request.form.get("quartos", "1"))
    parcelas_contrato = int(request.form.get("parcelas_contrato", "1"))

    tem_garagem = _to_bool(request.form.get("tem_garagem", ""))
    tem_criancas = _to_bool(request.form.get("tem_criancas", ""))
    vagas_estudio = int(request.form.get("vagas_estudio", "0"))

    # Ajustes: se for estúdio, ignorar quartos/garagem/crianças
    if tipo == TipoImovel.ESTUDIO:
        o = Orcamento(tipo=tipo, vagas_estudio=vagas_estudio)
    else:
        o = Orcamento(
            tipo=tipo,
            quartos=quartos,
            tem_garagem=tem_garagem,
            tem_criancas=tem_criancas if tipo == TipoImovel.APARTAMENTO else True
        )

    mensal = calc.calcular_mensal(o)
    contrato_total = calc.contrato_total()
    valor_parcela_contrato = calc.contrato_parcela(parcelas_contrato)

    return render_template(
        "resultado.html",
        orcamento=o,
        mensal=mensal,
        contrato_total=contrato_total,
        parcelas_contrato=parcelas_contrato,
        valor_parcela_contrato=valor_parcela_contrato
    )


@app.post("/exportar-csv")
def exportar_csv():
    # Recebe o valor mensal já calculado (vem do resultado.html)
    mensal = float(request.form.get("mensal", "0"))
    filename = "orcamento_12_parcelas.csv"
    filepath = os.path.join(EXPORT_DIR, filename)

    csv_exporter.exportar_12_meses(filepath, mensal)

    return send_file(filepath, as_attachment=True, download_name=filename)


if __name__ == "__main__":
    app.run(debug=True)
