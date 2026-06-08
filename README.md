#Integrantes 
Murillo Akira rm:561886
Igor Dominiski rm:562055
Rodrigo Abubakir rm:561479



# ARTEMIS-LOG — Roteamento Inteligente de Suprimentos em Base Lunar

 **GS — Dynamic Programming** | FIAP
 **Economia Espacial / Logística em uma Base Lunar no Polo Sul**

---

## 1. Definição do Problema

A criação de uma base lunar permanente no Polo Sul (parte da nova
infraestrutura econômica fora da Terra apresentada no kick-off) traz
um desafio crítico de logística:


A base será composta por vários módulos (habitats, laboratórios,
planta de oxigênio, reservatório de água, oficinas, etc.) espalhados
por um terreno acidentado, com **crateras, áreas de sombra permanente,
zonas de poeira e regiões sem cobertura de comunicação.

Sempre que um suprimento (peça, água, oxigênio, medicamento, alimento)
precisa ir de um módulo a outro, surge a pergunta:

Qual é a rota de menor custo que um rover autônomo deve percorrer
para entregar o suprimento com segurança e o menor gasto possível de
energia?

O "custo" de cada trecho combina distância + dificuldade do terreno +
consumo de energia + risco operacional.

---

## 2. Estrutura Utilizada — Grafo + Fila de Prioridade + Pilha

A base lunar é modelada como um GRAFO ponderado bidirecional:

- **Nós (vértices)** → módulos da base
- **Arestas** → rotas físicas entre módulos
- **Pesos** → custo combinado de cada rota

### Tamanho da estrutura (> 30 informações ✅)

| Elemento                      | Quantidade |
|-------------------------------|:----------:|
| Módulos da base (nós)         | **18**     |
| Rotas entre módulos (arestas) | **30**     |
| **Total de informações**      | **48**     |

### Módulos modelados

`PP` Porto de Pouso · `DEP` Depósito Central · `HAB1` Habitat 1 ·
`HAB2` Habitat 2 · `LAB` Laboratório · `EST` Estufa Hidropônica ·
`OXI` Planta de Oxigênio · `AGU` Extração de Gelo · `ENE` Usina Solar ·
`COM` Torre de Comunicação · `MED` Módulo Médico · `OFI` Oficina ·
`MIN` Mineração · `FAB` Fábrica (Impressão 3D) · `HEL` Heliporto ·
`OBS` Observatório · `RES` Reservatório de Água · `GAR` Garagem.

Além do grafo, o projeto usa:

- 🟢 **Fila de Prioridade (`heapq`)** → escolher sempre o módulo de
  menor custo acumulado durante o Dijkstra.
- 🟢 **Pilha (LIFO)** → reconstruir o caminho ótimo de trás pra frente
  a partir do dicionário de predecessores.

---

## ⚙️ 3. Lógica de Resolução

Usamos o algoritmo de **Dijkstra** (caminho mínimo em grafos com pesos
não-negativos), que é o algoritmo clássico para esse tipo de problema
e é uma aplicação direta de **programação dinâmica** — cada distância
mínima `d[v]` é construída a partir das soluções ótimas dos vizinhos:

```
d[v] = min ( d[u] + peso(u, v) )    para todo u vizinho de v
```

### Passo a passo

1. Inicializa todas as distâncias como ∞ e a distância da origem como 0.
2. Coloca a origem na **fila de prioridade**.
3. Enquanto a fila não estiver vazia:
   - Retira o nó de **menor custo** acumulado.
   - Para cada vizinho, calcula o novo custo. Se for menor que o
     atual, atualiza a distância e registra o predecessor.
4. Ao final, percorre os predecessores do destino até a origem
   usando uma **pilha** para reconstruir o caminho na ordem correta.

### Complexidade
`O((V + E) · log V)` — eficiente mesmo se a base lunar crescer para
centenas de módulos.

---

## 🧩 4. Funções `def` Criadas

| Função                  | Responsabilidade                                         |
|-------------------------|----------------------------------------------------------|
| `construir_grafo()`     | Monta o dicionário de adjacência a partir das listas.    |
| `dijkstra()`            | Calcula as menores distâncias usando fila de prioridade. |
| `reconstruir_caminho()` | Usa **pilha** para refazer o caminho ótimo.              |
| `planejar_entrega()`    | Função de alto nível que orquestra tudo.                 |
| `imprimir_relatorio()`  | Apresenta o resultado de forma legível.                  |
| `main()`                | Roda 4 cenários reais de entrega na base.                |

---

## ▶️ Como executar

Requisitos: **Python 3.8+** (somente biblioteca padrão, sem dependências
externas).

```bash
python3 base_lunar.py
```

### Exemplo de saída

```
================================================================
 ARTEMIS-LOG  |  Planejador de Entregas na Base Lunar
================================================================
 Origem  : PP    - Porto de Pouso (chegada de cargueiros da Terra)
 Destino : MED   - Módulo Médico / Enfermaria
----------------------------------------------------------------
 Custo total da rota : 11
 Nº de trechos       : 3
 Rota ótima:
    1. PP    -> Porto de Pouso
    2. DEP   -> Depósito Central de Suprimentos
    3. HAB1  -> Habitat Tripulação 1
    4. MED   -> Módulo Médico / Enfermaria
================================================================
```

---

## 🌍 Impacto e Conexão com o Tema

A solução se conecta diretamente aos pontos levantados no kick-off:

- ✅ **Logística** → distribuição automática de suprimentos.
- ✅ **Automação e robótica** → guia rovers autônomos.
- ✅ **Operação com recursos limitados** → minimiza energia/risco.
- ✅ **Aplicável à Terra** → mesma lógica resolve roteirização de
  drones de entrega, caminhões de socorro em desastres ou ambulâncias
  em grandes cidades.

> _"A próxima grande startup pode nascer tentando resolver um
> problema em Marte."_ — kick-off da GS.

---
