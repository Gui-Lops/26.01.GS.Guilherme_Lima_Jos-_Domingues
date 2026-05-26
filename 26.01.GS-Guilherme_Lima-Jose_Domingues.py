#                Guilherme Lima - 569226
# Representante: José Domingues - 568586  

# Listas para armazenar os dados
tipos_eventos = []
paises = []
regioes = []
cidades = []
areas_afetadas = []
intensidades = []
ocorrencias = []

# 1. Entrada de Dados
while True:
    try:
        quantidade_eventos = int(input("Insira a quantidade de eventos registrados: "))
        if quantidade_eventos <= 0:
            print("A quantidade de eventos deve ser um número positivo.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

for i in range(quantidade_eventos):
    print(f"\n--- Evento {i + 1} ---")
    tipos_eventos.append(input("Tipo de evento (ex: desmatamento, queimadas, etc.): "))
    paises.append(input("País: "))
    regioes.append(input("Região: "))
    cidades.append(input("Cidade: "))

    while True:
        try:
            area = float(input("Área afetada (km²): "))
            if area <= 0:
                print("A área afetada deve ser maior que zero.")
            else:
                areas_afetadas.append(area)
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número para a área.")

    while True:
        try:
            intensidade = int(input("Intensidade (1 a 10): "))
            if 1 <= intensidade <= 10:
                intensidades.append(intensidade)
                break
            else:
                print("A intensidade deve estar entre 1 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro para a intensidade.")

    while True:
        try:
            ocorrencia = int(input("Número de ocorrências: "))
            if ocorrencia < 0:
                print("O número de ocorrências não pode ser negativo.")
            else:
                ocorrencias.append(ocorrencia)
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro para o número de ocorrências.")

# 3. Análise de Dados

# a. Total de eventos registrados
total_eventos = len(tipos_eventos)

# b. Soma total das áreas afetadas
soma_areas_afetadas = 0
for area in areas_afetadas:
    soma_areas_afetadas += area

# c. Média das intensidades
media_intensidades = 0
if total_eventos > 0:
    soma_intensidades = 0
    for intensidade in intensidades:
        soma_intensidades += intensidade
    media_intensidades = soma_intensidades / total_eventos

# d. Evento com maior área afetada
maior_area = 0
indice_maior_area = -1
if total_eventos > 0:
    maior_area = max(areas_afetadas)
    indice_maior_area = areas_afetadas.index(maior_area)

# e. Região com maior número de ocorrências
regioes_ocorrencias = {}
for i in range(total_eventos):
    regiao = regioes[i]
    ocorrencia = ocorrencias[i]
    if regiao in regioes_ocorrencias:
        regioes_ocorrencias[regiao] += ocorrencia
    else:
        regioes_ocorrencias[regiao] = ocorrencia

regiao_maior_ocorrencias = "N/A"
maior_num_ocorrencias_regiao = -1
if regioes_ocorrencias:
    for regiao, num_ocorrencias in regioes_ocorrencias.items():
        if num_ocorrencias > maior_num_ocorrencias_regiao:
            maior_num_ocorrencias_regiao = num_ocorrencias
            regiao_maior_ocorrencias = regiao

# f. Densidade média (ocorrências ÷ área)
densidade_media = 0
if soma_areas_afetadas > 0:
    total_ocorrencias = 0
    for ocorrencia in ocorrencias:
        total_ocorrencias += ocorrencia
    densidade_media = total_ocorrencias / soma_areas_afetadas

# g. Quantidade de eventos acima da média de intensidade
eventos_acima_media_intensidade = 0
if total_eventos > 0:
    for intensidade in intensidades:
        if intensidade > media_intensidades:
            eventos_acima_media_intensidade += 1

# h. Identifique o evento mais crítico considerando: maior intensidade e maior área
indice_evento_mais_critico = -1
if total_eventos > 0:
    # Para simplificar, vamos considerar um 'score' combinando intensidade e área
    # Poderíamos usar intensidade * área, ou uma abordagem mais complexa
    # Aqui, vamos priorizar intensidade e, em caso de empate, área.
    max_score = -1
    for i in range(total_eventos):
        # Uma forma simples de combinar: intensidade é mais importante, área é um desempate
        # Ou podemos usar um score ponderado, mas o enunciado sugere 'maior intensidade E maior área'
        # Vamos buscar o que tem maior intensidade, e se houver empate, o que tem maior área.
        current_score = intensidades[i] * 1000 + areas_afetadas[i] # Multiplicar por 1000 para dar peso maior à intensidade
        if current_score > max_score:
            max_score = current_score
            indice_evento_mais_critico = i

# 4. Relatório de Resultados
print("\n" + "=" * 40)
print("        RELATÓRIO DE ANÁLISE")
print("=" * 40)

print(f"\nTotal de eventos registrados: {total_eventos}")

print("\n" + "-" * 40)
print("Resumo Geral")
print("-" * 40)
print(f"Área total afetada: {soma_areas_afetadas:.2f} km²")
print(f"Média de intensidade: {media_intensidades:.2f}")

print("\n" + "-" * 40)
print("Análises")
print("-" * 40)
print(f"Região com maior número de ocorrências: {regiao_maior_ocorrencias}")
print(f"Quantidade de eventos acima da média de intensidade: {eventos_acima_media_intensidade}")
print(f"Densidade média de ocorrências: {densidade_media:.2f} ocorrências/km²")

print("\n" + "-" * 40)
print("Evento Mais Crítico")
print("-" * 40)
if indice_evento_mais_critico != -1:
    print(f"Tipo: {tipos_eventos[indice_evento_mais_critico]}")
    print(f"Local: {cidades[indice_evento_mais_critico]}, {regioes[indice_evento_mais_critico]}, {paises[indice_evento_mais_critico]}")
    print(f"Intensidade: {intensidades[indice_evento_mais_critico]}")
    print(f"Área afetada: {areas_afetadas[indice_evento_mais_critico]:.2f} km²")
else:
    print("Nenhum evento crítico identificado.")

print("\n" + "=" * 40)
print(f"Total de desastres registrados: {total_eventos}")
