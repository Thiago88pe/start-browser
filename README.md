# **Selenium Automation Script for Chrome and Edge**

Este projeto contém um script Python que utiliza a biblioteca Selenium para automatizar os navegadores Chrome e Edge com opções e preferências específicas.

O objetivo do script é fornecer uma maneira fácil de iniciar e controlar os navegadores Chrome e Edge por meio de automação, permitindo a personalização das opções e preferências de cada navegador.

## Recursos

* Automatiza a inicialização dos navegadores Chrome e Edge.
* Permite definir um diretório de download personalizado para cada navegador.
* Faz o download e instala a versão mais recente do Chromedriver e Edgedriver automaticamente.
* Opção para maximizar a janela do navegador ao iniciar.
* Opção para executar os navegadores em modo headless (sem interface gráfica).

## Pré-requisitos

* Python 3.9 ou superior.
* Biblioteca Selenium 4.10.0 ou superior (```pip install selenium```).
* Pacote webdriver_manager 3.8.6 ou superior (```pip install webdriver_manager```).
Certifique-se de ter o **Python** instalado em seu ambiente antes de prosseguir com a instalação das dependências.

## Instalação

1. Clone este projeto para o seu ambiente local:
```
git clone https://github.com/Thiago88pe/start-browser.git
```
2. Navegue até o diretório do projeto:
```
cd start-browser
```
3. Crie e ative um ambiente virtual (opcional, mas recomendado):
- No Windows:
```
python -m venv venv
cd venv\Script\activate
```
- No Linux/Mac:
```
python3 -m venv venv
source venv/bin/activate
```
A ativação do ambiente virtual pode variar dependendo do sistema operacional. Consulte a documentação oficial do Python para obter mais informações.

4. Instale as dependências necessárias:
```
pip install -r requirements.txt
```

Lembre-se de ativar o ambiente virtual sempre que for executar o script em seu ambiente local.

Se você optar por não utilizar um ambiente virtual, ignore a etapa 3 na seção de Instalação. No entanto, é recomendado o uso de um ambiente virtual para evitar conflitos entre dependências em diferentes projetos Python.

## Uso

Existem duas funções principais no script: ```ExecuteChrome()``` e ```ExecuteEdge()```. Cada função inicia uma instância do WebDriver do Chrome ou Edge, com opções e preferências personalizadas.

Você pode usar essas funções em seu próprio código para automatizar a interação com os navegadores Chrome e Edge. Aqui está um exemplo de uso:

```
from StartBrowser import ExecuteChrome

# Executa o navegador Chrome
chrome_browser = ExecuteChrome()
# ... faça algo com o navegador Chrome ...
```
```
from StartBrowser import ExecuteEdge

# Executa o navegador Edge
edge_browser = ExecuteEdge()
# ... faça algo com o navegador Edge ...
```
## Personalização

O script permite personalizar várias opções e preferências para cada navegador. Você pode modificar as opções e preferências padrão nas funções ```ExecuteChrome()``` e ```ExecuteEdge()```, de acordo com suas necessidades.

Além disso, você pode descomentar a linha ```options.add_argument("--headless")``` em cada função para executar os navegadores em modo headless. Isso pode ser útil para testes automatizados ou execução em segundo plano.

## Contribuição

Contribuições são bem-vindas! Se você encontrar problemas, tiver sugestões ou quiser adicionar novos recursos, fique à vontade para abrir uma issue ou enviar um pull request.