# Rossmann Store Salaes Project
# Sobre a empresa
Rossmann é uma das maiores redes de drogarias da Europa, possuindo cerca de 56.200 mil funcionários e mais de 4.000 mil lojas em toda a Europa. Em 2019 seu faturamento foi superior a 10 bilhões de euros na Alemanha, Polônia, Hungria, República Tcheca, Turquia, Albânia, Kosovo e Espanha. 

# Problema de negócio
Com o sucesso da marca e crescimento no faturamento a Rossmann dentro do seu plano estratégico de crescimento reformar suas lojas a fim de renovar a estética e padronizar elas em linha com a proposta do time de arquitetura. Para que esse projeto seja executado a equipe de negócios da Rossmann precisa contar com as previsões de vendas das lojas para as próximas 6 semanas. Atualmente esse previsão é feita através de uma planilha em excel considerando a média das vendas, não sendo possível ter uma noção do volume de vendas e oscilações correspondentes a cada loja. Diante desse problema a empresa decidiu contratar um cientista de dados para auxiliar na busca de uma solução para esse gargalo no projeto. Durante a reunião realizada para debater este problema ficou a cargo do cientista de dados montar um modelo de previsão de venda com base em machine learning para responder esta questão de negócio.
#### Questão de negócio da Rossmann: Quanto cada loja venderá nas próximas 6 semanas?

# Resultados de negócio

# Premissas do negócio
Os dias em que as lojas estavam fechadas não foram considerados.
<br /> Foi considerado apenas valores maiores que 0 no campo Sales
<br /> Como foi assumido que existe um concorrente, caso não tenha uma data em que o copetidor abriu sua loja ou dados relacionados aos periodos promocionais, assumi-se a data da loja, assumindo a premissa que algumas variáveis derivadas do tempo são de extrema relavância para a representação de um comportamento.

# Planejamento da solução
Coleta de dados via [Kagle](https://www.kaggle.com/harlfoxem/housesalesprediction)
<br /> Entendimento de negócio
<br />Tratamento de [dados](https://github.com/obregonrodrigo/house-rocket-insights/tree/main/notebooks)
<br /> - Tranformação de variaveis
<br /> - Limpeza
<br /> - Entendimento
<br />Exploração de dados | confira o dashboard [Versão 1 - Heroku](https://analytics-house-rocket-21.herokuapp.com/)
<br />Seleção de Recursos
<br />Machine Learning Modelling
<br /> - Hyperparameter fine tunning
<br />Resultados para o negócio
<br />Telegram Boot
<br />Conclusão

# Insights do negócio
Principais insights de dados
<br />Imóveis qualificados para compra com vista para água representam menos de 1% do lucro esperado.
<br />Aproximadamente 60% das propriedades ficaram disponíveis para compra na primavera ou no verão.
<br />Imóveis reformados tem um valor 17,80% mais elevado que imóveis não reformados.
<br />Imóveis com 2 banheiros são 37,99% mais caros do que aqueles com até 1 banheiro.
<br />Imóveis com porão tem um valor 27,84% mais elevado que imóveis sem porão.

# Conclusão
