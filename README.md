# Rossmann Store Salaes Project
# Sobre a empresa
Rossmann é uma das maiores redes de drogarias da Europa, possuindo cerca de 56.200 mil funcionários e mais de 4.000 mil lojas em toda a Europa. Em 2019 seu faturamento foi superior a 10 bilhões de euros na Alemanha, Polônia, Hungria, República Tcheca, Turquia, Albânia, Kosovo e Espanha. 

# Problema de negócio
Com o sucesso da marca e crescente aumento do faturamento a Rossmann dentro do seu plano estratégico de crecimento tem a necessidade de melhorar o modo como estabelece a previsão de vendas das lojas. Essa previsão serve como base para estabelecimento de metas a serem alcançadas dentro das lojas. Gerentes que conseguem atingir as metas estabelecidas ganham um bônus além de chances maiores de promoção. Atualmente a previsão de vendas é feita através de uma planilha em excel considerando a média das vendas, não sendo possível ter uma noção do volume de vendas e oscilações correspondentes a cada loja acarretando em distorções na hora de estabelecer as metas. Diante desse problema a empresa decidiu contratar um cientista de dados para auxiliar na busca de uma solução para esse gargalo no projeto. Durante a reunião realizada para debater este problema ficou a cargo do cientista de dados montar um modelo de previsão de venda com base em machine learning para responder esta questão de negócio.
#### Questão de negócio da Rossmann: Quanto cada loja venderá nas próximas 4 semanas?

# Resultados de negócio
Através de um bot no telegram é possível realizar a consulta da previsão de venda esperada para as próximas 4 semas, loja a loja.
<br /><br />Confira o boot [aqui](https://t.me/Butlerbob_bot)
<br />(Digite o número de uma loja com uma / na frente. Exemplo: /22)

# Premissas do negócio
Os dias em que as lojas estavam fechadas não foram considerados.
<br /> Foi considerado apenas valores maiores que 0 no campo Sales;
<br /> Foi assumido que 1 mês possui 4 semanas;
<br /> Como foi assumido que existe um concorrente, caso não tenha uma data em que o copetidor abriu sua loja ou dados relacionados aos periodos promocionais, assumi-se a data da loja, assumindo a premissa que algumas variáveis derivadas do tempo são de extrema relavância para a representação de um comportamento.

# Planejamento da solução
Coleta de dados via [Kagle](https://www.kaggle.com/c/rossmann-store-sales)
<br /> Entendimento de negócio
<br />Tratamento de [dados](https://github.com/obregonrodrigo/Rossmann-store-sales-project/tree/main/notebooks)
<br /> - Tranformação de variaveis
<br /> - Limpeza
<br /> - Entendimento
<br />Exploração de [dados](https://github.com/obregonrodrigo/Rossmann-store-sales-project/tree/main/notebooks)
<br />Seleção de Recursos
<br />Machine Learning Modelling - Escolhido o Random Forest Regressor
<br /> - Hyperparameter fine tunning 
<br />Resultados para o negócio
<br />[Telegram Boot](https://t.me/Butlerbob_bot)
<br />Conclusão

# Insights do negócio
Principais insights de dados
<br />Após o dia 10 do mês lojas vendem mais.
<br />Lojas do tipo 'extended assortment' que possuem um sortimento de produtos mais elevado vendem menos que lojas do tipo 'basic'.
<br />Promoções que duram um grande espaço de tempo vendem regularmente durante um tempo e depois suas vendas vão caindo.
<br />Com o passar dos anos após a sua abertura lojas tendem a vender menos.
<br />Lojas vendem menos nos finais de semana.

# Conclusão
Através do modelo desenvolvido é possível fazer a predição de vendas das próximas 4 semanas, servindo de apoio para a elaboração de metas da Rossmann.
