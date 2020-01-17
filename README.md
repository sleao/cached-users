# Cached Users

Usar _cache_ é uma técnica comum para melhorar o tempo de execução de um software.

Um trecho sobre cache da _Wikipedia_:

> In computing, a cache is a hardware or software component that stores data so that future requests for that data can be served faster; the data stored in a cache might be the result of an earlier computation or a copy of data stored elsewhere.

Neste repositório há um exercício para praticar e experimentar os efeitos
de usar _cache_ para acelerar consulta de informações remotas, gravando
uma cópia local para valores conhecidos.

## Atividade

Escreva um programa que recebe como entrada um username e retorna as seguintes informações:

- e-mail
- website
- hemisfério (norte ou sul)

A fonte de dados original é a seguinte API:

https://jsonplaceholder.typicode.com/users

Para consultar as informações dela, use a biblioteca `requests`.

Para ler um parâmetro na entrada do seu programa veja a documentação do `sys.argv`:
https://docs.python.org/3/library/sys.html#sys.argv

---

Agora que o seu programa consulta informações na API e mostra os dados de
interesse na tela, adicione um _cache_ para evitar uma consulta quando a
informação for conhecida.

Existe alguns serviços que podem ser usados para isso, geralmente um
banco de dados ou algum serviço específico de cache
como o Memcached.

Para este exercício você pode usar um arquivo CSV.

CSV (comma-separated values) é um formato de arquivo que possui valores
separados por vírgulas ou algum outro separador.

Um exemplo com alguns dados referentes à este exercício:
```csv
mail,website,hemisferio,username
Sincere@april.biz,hildegard.org,sul,Bret
Shanna@melissa.tv,anastasia.net,sul,Antonette
```

Na biblioteca padrão do Python existe um módulo para ler e escrever
arquivos CSV:
https://docs.python.org/3/library/csv.html


## Regras

Sua solução deve funcionar com Python 3.6 ou mais recente.

Use a biblioteca `requests` para fazer requisições na API.

Seu programa deve usar o arquivo CSV como cache:

1. O arquivo começa vazio
2. Ao executar o programa uma vez para um determinado username deve adicionar apenas os dados do username consultado
3. Em consultas futuras desse username, deve retornar os dados do CSV, sem fazer consulta na API

## Dicas

Não tente resolver tudo de uma vez. Quebre o problema em etapas.

É melhor ter um programa lento que funciona do que ter um programa performático que não funciona.
