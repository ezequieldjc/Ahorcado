import os
import threading
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())


#Driver para Chrome v83
#https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39/
#Modificar variable driver segun la ruta personal

#driver = r"C:\chromedriver_win32\chromedriver.exe"
driver = r"/home/travis/virtualenv/python3.8.2/bin/chromedriver"

app = "https://agiles2020-ahorcado.herokuapp.com/play/"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")




def before_all(context):
    context.server = simple_server.WSGIServer(("", 5000), WSGIRequestHandler)
    context.server.set_app(app)
    context.pa_app = threading.Thread(target=context.server.serve_forever)
    context.pa_app.start()

    context.browser = webdriver.Chrome(options=chrome_options, executable_path=r"/home/travis/virtualenv/python3.8.2/bin/chromedriver")
    context.browser.set_page_load_timeout(time_to_wait=200)


def after_all(context):
    context.browser.quit()
    context.server.shutdown()
    context.pa_app.join()
