from browser import Browser
from pages.home_page import Home_page
from pages.my_wireframe_page import My_wireframe


def before_all(context):
    context.browser = Browser()
    context.browser.maximise_windows()
    # aici vom instantia obiectele din folderul pages (adica atunci cand vom adauga fisier in
    # folderul pages vom instantia acici obiectele din ele)
    context.home_page = Home_page()#aici nu pusesem ()
    context.my_wireframe_page = My_wireframe()



def after_all(context):
    context.browser.close_browser()