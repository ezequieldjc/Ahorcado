from behave import given, when, then

@given(u'Que ingreso al juego')
def step_impl(context):
    context.browser.get('https://agiles2020-ahorcado.herokuapp.com/play/')
    
@given(u'Ingreso un usuario')
def step_impl(context):
    context.browser.find_element_by_name('name').send_keys('NombreUsuario')
    context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[2]/div/div/form/div/div[2]/button").click()

@given(u'Selecciono dificultad medio')
def step_impl(context):
    context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[2]/div/div/form[2]/div/div[2]/label").click()
    context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[2]/div/div/form[2]/div/button").click()


@when(u'Arriesgo una palabra erronea')
def step_impl(context):
    context.browser.find_element_by_xpath(f'/html/body/div/div/div/div[2]/div/div/form[2]/div/div[1]/div/input').send_keys('--')
    #context.browser.find_element_by_name('ingreso').send_keys('NombreUsuario')
    context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[2]/div/div/form[2]/div/div[2]/button").click()
    
@then(u'Juego perdido')
def step_impl(context):
    text = context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[2]/div/div/h1").text
    assert text[:18] == "Hasta aca llegaste"