# Importa a classe WebDriver da biblioteca Selenium, que é responsável por interagir com os navegadores.
from selenium import webdriver

# Importa a classe Service do Selenium para o Chrome e a renomeia como ChromeService.
from selenium.webdriver.chrome.service import Service as ChromeService
# Importa o ChromeDriverManager do pacote webdriver_manager para gerenciar a versão do Chromedriver.
from webdriver_manager.chrome import ChromeDriverManager

# Importa a classe Service do Selenium para o Edge e a renomeia como EdgeService.
from selenium.webdriver.edge.service import Service as EdgeService
# Importa o EdgeChromiumDriverManager do pacote webdriver_manager para gerenciar a versão do Edgedriver.
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Importa o módulo os para manipulação de caminhos de arquivos e diretórios.
import os

'''
Este código é um script Python que utiliza a biblioteca Selenium para automatizar os navegadores Chrome e Edge com opções e preferências específicas.
O código define o diretório de download para ambos navegadores.
O código também baixa e instala a versão mais recente do Chromedriver e do Edgedriver, no diretório especificado.
O objetivo do código é fornecer uma maneira de iniciar e controlar facilmente os navegadores Chrome e Edge com opções e preferências específicas.
'''

def ExecuteChrome(headless=False):
    '''
    Inicia uma instância do WebDriver do Chrome com opções personalizadas.

    Returns:
        browser (WebDriver): Instância do WebDriver do Chrome.
    '''
    
    # Usado para definir várias opções para o navegador.
    options = webdriver.ChromeOptions()

    # Define o caminho onde os arquivos baixados serão salvos
    caminho_download = os.getcwd()

    # Configura as preferências
    prefs = {
        "download.default_directory": caminho_download,
        "disable-web-security": True
        }
    
    # Método usado para adicionar as prefs as opções do Chrome.
    options.add_experimental_option("prefs", prefs)
    
    # Iniciar o navegador com a janela maximizada.
    options.add_argument("--start-maximized")

    # Iniciar o navegador em modo headless (sem interface gráfica).
    if headless:
        options.add_argument("--headless")

    # Caminho absoluto onde o Chromedriver será baixado. Neste caso será criado a pasta 'bin' e o Chromedriver ficará dentro dela.
    CHROMEDRIVER_PATH = os.path.abspath('bin')
    
    # Baixa e instala a versão mais recente do Chromedriver no caminho especificado.
    service = ChromeService(ChromeDriverManager(path=CHROMEDRIVER_PATH).install())

    # Inicia uma instância do WebDriver do Chrome com as opções configuradas.
    browser = webdriver.Chrome(service=service, options=options)

    return browser


def ExecuteEdge(headless=False):
    '''
    Inicia uma instância do WebDriver do Edge com opções personalizadas.

    Returns:
        browser (WebDriver): Instância do WebDriver do Edge.
    '''
    
    # Usado para definir várias opções para o navegador.
    options = webdriver.EdgeOptions()

    # Define o caminho onde os arquivos baixados serão salvos.
    caminho_download = os.getcwd()

    # Configura as preferências.
    prefs = {
            'download.default_directory': caminho_download,
        }
    
    # Método usado para adicionar as prefs as opções do Edge.
    options.add_experimental_option('prefs', prefs)

    # Iniciar o navegador com a janela maximizada.
    options.add_argument('--start-maximized')

    # Iniciar o navegador em modo headless (sem interface gráfica).
    if headless:
        options.add_argument("--headless")

    # Caminho absoluto onde o Edgedriver será baixado. Neste caso será criado a pasta 'bin' e o Edgedriver ficará dentro dela.
    EDGEDRIVER_PATH = os.path.abspath('bin')

    # Baixa e instala a versão mais recente do Edgedriver no caminho especificado.
    service = EdgeService(EdgeChromiumDriverManager(path=EDGEDRIVER_PATH).install())

    # Inicia uma instância do WebDriver do Edge com as opções configuradas.
    browser = webdriver.Edge(service=service, options=options)

    return browser
