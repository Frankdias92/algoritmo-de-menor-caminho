import heapq

grafo = {
    "CEASA": {"Alecrim": 12, "Lagoa Nova": 7},
    "Alecrim": {"Coronel Estevam": 3},
    "Coronel Estevam": {"Petropolis": 4},
    "Lagoa Nova": {"Petropolis": 7, "Salgado Filho": 7},
    "Salgado Filho": {"Tirol": 4},
    "Tirol": {"Hermes da Fonseca": 3},
    "Hermes da Fonseca": {"Petropolis": 3},
    "Petropolis": {"Nordestao": 2},
    "Nordestao": {},
}


def dijkstra(grafo, inicio):

    distancias = {vertice: float("inf") for vertice in grafo}
    distancias[inicio] = 0

    caminhos = {vertice: [] for vertice in grafo}
    caminhos[inicio] = [inicio]

    fila = [(0, inicio)]

    while fila:
        distancia_atual, vertice_atual = heapq.heappop(fila)

        if distancia_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo[vertice_atual].items():
            nova_distancia = distancia_atual + peso

            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia

                caminhos[vizinho] = caminhos[vertice_atual] + [vizinho]

                heapq.heappush(fila, (nova_distancia, vizinho))

    return distancias, caminhos


distancias, caminhos = dijkstra(grafo, "CEASA", "Nordestao")

print("=" * 50)
print("ALGORITMO DE DIJKSTRA")
print("=" * 50)

print(f"\nOrigem: CEASA")
print(f"Destino: Nordestao")

print(f"\nMenor custo encontrado: {distancias['Nordestao']}")

print("\nMelhor caminho:")
print(" -> ".join(caminhos["Nordestao"]))
