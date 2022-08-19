import os
import time
import random
import keyboard
import pyautogui
from colorama import Fore
from colorama import Style
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as CondicaoExperada


# INIT------------------------------------------------------------------------------------------------------#


close = False
attention_window = pyautogui.confirm('Atencão: Por Favor Não Ultilize Seu Computador Enquanto A Altomacão '
                                     'Estiver "In_Running".\n\nDito Isso, Podemos Iniciar A Altomacão?')
if attention_window == 'Cancel':
    close = True


if not close:
    class ForWork:

        def __init__(self):
            self.exit = False
            options = Options()
            options.add_argument("lang=pt-BR")
            self.driver = webdriver.Chrome(executable_path=r"drivers/chromedriver.exe", options=options)
            self.driver.set_window_rect(0, 0)
            self.driver.set_window_size(1000, 800)
            self.waint = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=
            [NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            self.link_playlist = "https://www.youtube.com/playlist?list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj"
            self.others_links = ['https://www.youtube.com/', 'https://translate.google.com.br/?hl=pt-BR',
                                 "https://mail.google.com/mail/u/0/#inbox", "https://pixlr.com/br/e/",
                                 "https://opengameart.org/"]
            print(Fore.YELLOW + "- Ignore o erro acima" + Style.RESET_ALL)
            print(Fore.GREEN + "- Navegador aberto e configurado" + Style.RESET_ALL)
            self.driver.get(self.link_playlist)

        def Start(self):
            self.Playlist()
            self.OpenLinks()
            self.CloseWindows()

        def Playlist(self):
            print(Fore.BLUE + "- Abrindo sua playlist" + Style.RESET_ALL)
            try:
                self.driver.get(self.link_playlist)
                random_button = self.waint.until(CondicaoExperada.element_to_be_clickable(
                    (By.XPATH, '//ytd-menu-renderer/div/ytd-button-renderer/a/yt-icon-button/button/yt-icon')))
                time.sleep(random.randint(2, 4))
                random_button.click()
                print(Fore.GREEN + "- Playlist aberta" + Style.RESET_ALL)
            except:
                print(Fore.RED + "  - Não conseguimos encontrar sua playlist. Possiveis erros:\n"
                                 "  - A conta da playlist escolhida não esta logada no youtube.\n"
                                 "  - Dispositivo não conectado a internet.\n"
                                 "  - Erro do progamador.(Fale com ele).\n"
                                 "  - Link da playlist esta incorreto." + Style.RESET_ALL)

        def OpenLinks(self):
            print(Fore.BLUE + "- Abrindo os outros links" + Style.RESET_ALL)
            try:
                self.LogicForOpenLinks(self.others_links)
                print(Fore.GREEN + "- Todos os links foram abertos" + Style.RESET_ALL)

            except:
                print(Fore.RED + "  - Não conseguimos abrir os links.Possiveis erros:\n"
                                 "  - Dispositivo não conectado a internet.\n"
                                 "  - Erro do progamador.(Fale com ele).\n"
                                 "  - Link fornecido esta incorreto." + Style.RESET_ALL)

        @staticmethod
        def LogicForOpenLinks(list_links):
            pyautogui.PAUSE = 1
            for link in list_links:
                pyautogui.hotkey("ctrl", "t")
                pyautogui.write(link)
                pyautogui.press("enter")
                time.sleep(0.5)

        def CloseWindows(self):
            time.sleep(1)
            pyautogui.hotkey("ctrl", "tab")

    bot = ForWork()
    bot.Start()
    pyautogui.alert("A Altomacão Acabou De Ser Finalizada. Tenha Um Bom Dia.")
