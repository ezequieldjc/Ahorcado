from behave import given, when, then

@given(u'Que entro al juego')
def step_impl(context):
    context.browser.get('https://agiles2020-ahorcado.herokuapp.com/play/')

@given(u'Ingreso un user')
def step_impl(context):
    context.browser.find_element_by_name('name').send_keys('NombreUsuario')

@given(u'Clic en Siguiente')
def step_impl(context):
    context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[2]/div/div/form/div/div[2]/button").click()

@given(u'Selecciono dificultad Media')
def step_impl(context):
    context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[2]/div/div/form[2]/div/div[2]/label").click()
    #context.browser.find_element_by_id("Medio").click()

@when(u'Clic nuevamente en Siguiente')
def step_impl(context):
    context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[2]/div/div/form[2]/div/button").click()

@then(u'La dificultad mostrada es la correcta')
def step_impl(context):
    text = context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[1]/div/p[1]").text
    assert text == "DIFICULTAD: 2"