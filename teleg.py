import time
import re
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from splinter import Browser
import telebot
from telebot import custom_filters
import datetime
import selenium
import os
import threading


API_KEY = "TOKEN"
bot = telebot.TeleBot(API_KEY)
massage = None
idc = [0, 0, 0, 0]
myser = Service()

options = selenium.webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


def botthearding(chatid):
    corr = str()
    contra = str()
    credentials = []

    def webdriver():
        try:
            browser = Browser("chrome", service=myser)
        except:
            os.system("clear")
            error("chrome driver error")
            try:
                browser = Browser("firefox", service=myser)
            except:
                os.system("clear")
                error("geko driver error")
        return browser

    def error(tipe):
        listt = ["0", "Error:", tipe]
        timee = datetime.datetime.now()
        listt[0] = rf"{timee}"

        with open("errorlog.txt", "a") as log:
            log.write("\n".join(listt) + "\n" + "\n")

    def start():
        sent = bot.send_message(chatid, "Please enter your e-mail.")
        bot.register_next_step_handler(sent, passkwys)

    def passkwys(message):
        corr = message.text
        credentials.append(corr)
        sent = bot.send_message(chatid, "Please enter your password.")
        bot.register_next_step_handler(sent, paswardo)
        bot.delete_message(message.chat.id, message.message_id)
        return corr

    def paswardo(message):
        browser = webdriver()
        contra = message.text
        credentials.append(contra)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(chatid, "Processing, this may take a while")
        browser.visit(
            "https://login.usfq.edu.ec/adfs/ls/?SAMLRequest=jdG9asMwEADgvdB3MNotWY7syMIOhHYJpEvSduhSbOmSGGzJ0cmhj1%2blIbRjl%2bN%2bOPi4q9dzONkdnGfAkGyeG4LtOPhb%2fbnkXVFlwCteLoSRUpbCdF3Wgel4VQhOknfw2DvbkJxmJNkgzrCxGFobYivLFynnaSZfeam4ULmgeSlkUWQfJFkjgg9x98lZnEfwe%2fCXXsPbbtuQUwgTKsbGfsbDhcZwpmBmCpqZfGDDxNroZoM79pZdxdtrRuOMJF%2fjYLEhs7fKtdijsu0IqIJW%2b%2fXLVkWomrwLTruBrB4fkqT%2bYfv%2fLLZ3NFndiWUlYFlpk5pMFKnQFU9lWfDUlEZ3eZ4fpBQ0gI0nQdr5%2fngKOLUaqHbjL71mN0QE1ezvT1bf&RelayState=%2fd2l%2fhome&client-request-id=50e005f5-2af5-4e97-2c20-0780060000f8&pullStatus=0"
        )
        time.sleep(0.5)
        browser.find_by_id("userNameInput").fill(credentials[0])
        try:
            browser.find_by_id("nextButton").click()
        except:
            error("no next buttom")
        time.sleep(0.5)
        browser.find_by_id("passwordInput").fill(credentials[1])
        try:
            browser.find_by_id("submitButton").click()
        except:
            error("no submit buttom")
        time.sleep(1.4)
        # Incorrect password
        try:
            browser.find_by_text("Calendario").click()
        except:
            sent = bot.send_message(chatid, "Please enter your password.")
            credentials.pop(1)
            browser.quit()
            bot.register_next_step_handler(sent, paswardo)
        browser.find_by_id("ListPageViewSelector").click()
        snap = browser.html_snapshot("calendario.html")
        try:
            browser.find_by_css('div[class = "d2l-navigation-s-personal-menu"]').click()
            browser.find_by_text("Cerrar sesión").click()
        except:
            browser.quit()
            error("no end sesion")
            os.system.exit()

        with open(snap, "r", encoding="utf-8") as p:
            presoup = p.read()
            soup = BeautifulSoup(presoup, "html.parser")

            # Buscar todos los elementos <li>
        list_items = soup.find_all("li", class_="d2l-datalist-item")

        # Iterar sobre los elementos y extraer título y fecha de vencimiento
        for item in list_items:
            try:
                # Extraer el título
                title_div = item.find("div", class_="d2l-textblock")
                title = title_div.get_text() if title_div else None

                clase_div = item.find("div", class_="d2l-offscreen")
                clas = clase_div.get_text() if title_div else None

                # Extraer la fecha de vencimiento
                date_div = item.find("div", class_=re.compile(r"d2l-textblock d2l_.*"))
                date = date_div.get_text() if date_div else None

                bot.send_message(chatid, "{} {} {}".format(title, clas, date))
            except:
                pass

    start()


@bot.message_handler(commands=["start"])
def starting(message):
    idc[0] = message.chat.id
    hilo1 = threading.Thread(target=botthearding(idc[0]))
    hilo1.start()
    hilo1.join()


@bot.message_handler(content_types=["text"])
def handle_adios(message):
    bot.send_message(message.chat.id, "Adios!")


bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.add_custom_filter(custom_filters.TextStartsFilter())

bot.infinity_polling()
