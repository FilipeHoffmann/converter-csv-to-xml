# Converter CSV To XML
Aplicação Web para converter um aquivo CSV para XML utilizando Python.

## Tecnologias
* Python
  * Flask

## Estrutura do projeto

```
  .
  ├── static
  │   └── css
  │       └── styles.css
  ├── templates
  │   └── index.html
  ├── uploads
  ├── app.py
  ├── config.json
  └── README.md
```
## Como usar
Para começar a usar precisamos configurar a nossa máquina que iremos utilizar para hospedar nossa aplicação. Basta fazer as alterações no arquivo ``` config.json ``` conforme o exemplo a seguir:

```
{
    "host": "INSERIR O IP DA MÁQUINA",
    "port": INSERIR A PORTA DA MÁQUINA,
    "root": "INSERIR A TAG PRINCIPAL DO XML",
    "item": "INSERIR A TAG DE CADA ELEMENTO"
}
```
Após finalizar a configuração bastar executar o arquivo ```app.py```.

**Obs: O arquivo CSV, necessáriamente precisa ser separado por ";".**
