import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, send_file, current_app

from app.models import Orcamento, TipoImovel
from app.services import CalculadoraOrcamento, CsvExporter

main_bp = Blueprint("main", __name__)

calc = CalculadoraOrcamento()
csv_exporter = CsvExporter()


def _to_bool(value: str) -> bool:
    return value in ("on", "true", "1", "yes", "sim")


@main_bp.get("/")
def index():
    return render_template("index.html")


@main_bp.post("/orcamento")
def gerar_orcamento():
    tipo_str = (request.form.get("tipo") or "").strip().lower()

    try:
        tipo = TipoImovel(tipo_str)
    except ValueError:
        flash("Tipo de imóvel inválido.")
        return redirect(url_for("main.index"))

    quartos = int(request.form.get("quartos", "1"))
    parcelas = int(request.form.get("parcelas_contrato", "1"))

    tem_garagem = _to_bool(request.form.get("tem_garagem", ""))
    tem_criancas = _to_bool(request.form.get("tem_criancas", ""))
    vagas_estudio = int(request.form.get("vagas_estudio", "0"))

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
    valor_parcela = calc.contrato_parcela(parcelas)

    return render_template(
        "resultado.html",
        orcamento=o,
        mensal=mensal,
        contrato_total=contrato_total,
        parcelas_contrato=parcelas,
        valor_parcela_contrato=valor_parcela
    )


@main_bp.post("/exportar-csv")
def exportar_csv():
    mensal = float(request.form.get("mensal", "0"))

    export_dir = current_app.config["EXPORT_DIR"]
    os.makedirs(export_dir, exist_ok=True)

    filename = "orcamento_12_parcelas.csv"
    filepath = os.path.join(export_dir, filename)

    csv_exporter.exportar_12_meses(filepath, mensal)

    return send_file(filepath, as_attachment=True, download_name=filename)
