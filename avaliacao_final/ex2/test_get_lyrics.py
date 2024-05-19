import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def write_lyrics_in_file(lyrics):
    with open("letra.md", "w", encoding="UTF-8") as arquivo:
            arquivo.write(f'{lyrics}')

def test_get_lyrics():

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--mute-audio')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-infobars')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--no-sandbox')
    options.add_argument('--no-zygote')
    options.add_argument('--log-level=3')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-web-security')
    options.add_argument('--disable-features=VizDisplayCompositor')
    options.add_argument('--disable-breakpad')

    servico = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(
        options=options,
        service=servico
        )

    driver.get('https://www.letras.mus.br/djavan/11337')
    time.sleep(1)

    lyric_content = driver.find_element(By.ID, "js-lyric-content")
    div_lyric = lyric_content.find_element(By.CLASS_NAME, "lyric-original")
    paragraphs = div_lyric.find_elements(By.XPATH, ".//p")

    lyric = ""
    for p in paragraphs:
        lyric += f'{p.text}\n'

    print("Oceano: ", lyric)

    # cria um arquivo chamado "letra.md" com a letra da música 
    write_lyrics_in_file(lyric)

    driver.close()
    driver.quit()

# Terminal: py test_get_lyrics.py
test_get_lyrics()