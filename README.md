# PI_Grupo19
(2601-PROJETO INTEGRADOR: DESENVOLVIMENTO LOW CODE EM CIÊNCIA DE DADOS) - GRUPO 19, 2026.1

# Tema do Projeto
Quais fatores realmente influenciam a qualidade do ar? Uma análise integrada com ciência de dados.

# Integrantes: 

Débora Aparecida Marques Ferreira  
Erick Cardozo Melo  
Huéslei de Miranda Moura  
Leonardo Borges Coleto Correia  


# 2) Definição da base de dados:

**Introdução**
    O crescimento urbano acelerado, aliado ao aumento da frota de veículos, expansão industrial e avanço do desmatamento, tem intensificado os problemas relacionados à qualidade do ar nas cidades. Esses fatores contribuem diretamente para o aumento da poluição atmosférica, impactando negativamente o meio ambiente e a saúde da população. Segundo a World Health Organization (2021), a poluição do ar é responsável por milhões de mortes prematuras anualmente, sendo considerada um dos maiores riscos ambientais à saúde humana.
    Além disso, o crescimento urbano desordenado e a intensificação das atividades econômicas têm ampliado os níveis de emissão de poluentes, especialmente em países em desenvolvimento. De acordo com o World Bank (2020), o aumento da urbanização está diretamente associado à degradação ambiental e à piora da qualidade do ar, exigindo políticas públicas mais eficazes e sustentáveis.
No contexto ambiental, o desmatamento também desempenha um papel relevante, uma vez que reduz a capacidade de absorção de dióxido de carbono (CO₂) e contribui para o agravamento das mudanças climáticas. Conforme destacado pelo Intergovernmental Panel on Climate Change (2022), a perda de cobertura florestal intensifica os impactos ambientais e compromete o equilíbrio climático global.
    Dessa forma, a qualidade do ar, frequentemente medida pelo índice AQI (Air Quality Index), torna-se um importante indicador das condições ambientais urbanas. No entanto, a relação entre variáveis como emissões de CO₂, densidade populacional, áreas verdes e investimentos ambientais ainda não é completamente compreendida de forma integrada.
    Nesse sentido, a utilização de técnicas de ciência de dados surge como uma ferramenta essencial para analisar grandes volumes de dados, identificar padrões e compreender os fatores que mais influenciam a qualidade do ar. Segundo a European Environment Agency (2023), o uso de análise de dados tem se mostrado fundamental para o monitoramento ambiental e para o suporte à tomada de decisões em políticas públicas.

**O Problema:** O aumento acelerado da urbanização, aliado ao crescimento da frota de veículos, expansão industrial e avanço do desmatamento, tem gerado impactos significativos na qualidade do ar em diversas cidades ao redor do mundo.
Apesar dos investimentos públicos em políticas ambientais, ainda há incerteza sobre quais fatores realmente exercem maior influência na degradação da qualidade do ar, dificultando a tomada de decisões eficazes por parte de gestores públicos. Nesse contexto, surge a seguinte questão: Quais são os principais fatores ambientais e urbanos que mais impactam a qualidade do ar (AQI) nas cidades, e como eles se relacionam entre si?

**Objetivo Geral**
Analisar os principais fatores ambientais, urbanos e econômicos que influenciam a qualidade do ar (AQI), utilizando técnicas de ciência de dados.

**Objetivo Especifico**
- Explorar e descrever os dados relacionados à qualidade do ar e variáveis ambientais
- Identificar correlações entre as variáveis do dataset
- Avaliar o impacto de fatores como:
    - Emissões de CO₂;
    - Crescimento de veículos;
    - Desmatamento;
    - Áreas verdes.
- Construir um modelo preditivo para estimar o AQI
- Identificar as variáveis mais relevantes na previsão da qualidade do ar

**Motivação:** 
Compreender essas relações é fundamental para:
- Apoiar políticas públicas mais eficientes;
- Direcionar investimentos ambientais de forma estratégica;
- Reduzir impactos à saúde da população;
- Promover desenvolvimento urbano sustentável.

**Justificativa:**
A utilização de técnicas de ciência de dados permite:
- Identificar padrões ocultos nos dados;
- Quantificar o impacto de cada variável;
- Criar modelos preditivos;
- Transformar dados em decisões práticas.

**Informações sobre a Base de Dados**

A base de dados envolvida possui informações do qual relaciona a qualidade do ar e o desmatamento de quatro cidades: Rio de Janeiro (Brasil), Shenzhen (China), Mumbai (India), Cologne (Alemanha) e Montreal (Canadá). Os dados trazem valores quantificados sobre:

**- Qualidade do ar:** índice geral da qualidade do ar (AQI), e de dois tipos de materiais particulados (MP2.5 e MP10):
    **1.*** Os materiais particulados mais finos possuem diâmetro inferiores a 2,5 micrômetros (MP2.5), responsável principalemte por complicações à saúde humana como, doenças respiratórias graves, doenças cardiovasculares, dano pulmonar e sara e, mortalidade prematura. O efeito ao meio ambiente e clima envolve as mudanças climáticas e a visibilidade (névoa seca).
    **2.** Materiais particulados mais grossos, neste caso, 10 micrômetros (MP10), são responsável por também doenças respiratórias e cardiovasculares, mas também agravam doenças crônicas, toxicidade por metais pesados (cancerígenos), dioxinas, furanos e benzopirenos (cancerígenos). O efeito ao meio ambiente acarreta em danos materiais (sujeira e corrosão a infraestruturas), alterações climáticas e redução da visibilidade.

**- Meio ambiente (florestas):** taxa de desmatamento e de reflorestamento;
**- Crescimento urbano e industrial:** o crescimento urbano relacionando o número de veículos e indústrias;
**- Investimento e estrutura:** o orçamento ambiental (em dólar) e densidade populacional (pessoas/km^2);
**- Emissões e qualidade ambiental:** Emissões de CO2 (em milhões de toneladas) e o percentual de áreas verdes;
**- Qualidade de vida:** Índice de expectativa de vida.

**Metodologia**

Com esses dados serão realizados análises cruzando as informações obtidas e expressada por demonstrações gráficas identificando:
    **1.** O que mais influencia o AQI (poluição do ar)?
    **2.** Desmatamento impacta a qualidade do ar?
    **3.** Cidades com mais áreas verdes têm melhor expectativa de vida?
    **4.** O crescimento de veículos piora a poluição?
    **5.** Quais fatores mais contribuem para a piora da qualidade do ar (AQI)?
    
A pesquisa será conduzida com base em técnicas de ciência de dados, seguindo as seguintes etapas:
  1. Coleta e preparação dos dados
   - Utilização de um dataset contendo informações sobre qualidade do ar, desmatamento, emissões e fatores urbanos.

  2. Limpeza e tratamento
    - Remoção de valores ausentes, padronização dos dados e seleção de variáveis relevantes.

  3. Análise exploratória (EDA)
    - Aplicação de estatísticas descritivas e visualizações gráficas para identificação de padrões e relações entre variáveis.

  4. Modelagem preditiva
    - Aplicação de algoritmos de machine learning, como regressão e Random Forest, para prever o índice AQI.

  5. Avaliação do modelo
    - Utilização de métricas como R² para avaliar o desempenho do modelo.

  6. Interpretação dos resultados
    - Análise da importância das variáveis para identificar os principais fatores que impactam a qualidade do ar.

**Cronograma**



**REFERÊNCIAS**
WORLD HEALTH ORGANIZATION. Air pollution and health. Geneva: WHO, 2021.
WORLD BANK. Urban development overview. Washington, DC: World Bank, 2020.
INTERGOVERNMENTAL PANEL ON CLIMATE CHANGE. Climate Change 2022: Impacts, Adaptation and Vulnerability. Cambridge: Cambridge University Press, 2022.
EUROPEAN ENVIRONMENT AGENCY. Air quality in Europe – 2023 report. Copenhagen: EEA, 2023.
