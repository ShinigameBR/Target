import json

with open('dados.json') as f:
    conteudo = f.read()
    faturamento_mensal = json.loads(conteudo)


def calcula_faturamento(n):
    valores_faturamento = [dia['valor'] for dia in n]
    menor_faturamento = min(valores_faturamento)
    maior_faturamento = max(valores_faturamento)
    media_faturamento = sum(valores_faturamento) / len(valores_faturamento)
    dias_acima_media = len(
        [valor for valor in valores_faturamento if valor > media_faturamento])

    return menor_faturamento, maior_faturamento, media_faturamento, dias_acima_media


menor_faturamento, maior_faturamento, media_faturamento, dias_acima_media = calcula_faturamento(
    faturamento_mensal)
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Média dos valores de faturamento: {media_faturamento:.4f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
