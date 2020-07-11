from behave import given, when, then

@given(u'Que navego para jugar en la página')
def step_impl(context):
    context.browser.get('https://agiles2020-ahorcado.herokuapp.com/play/')

@given(u'Ingreso un nombre de usuario')
def step_impl(context):
    context.browser.find_element_by_name('name').send_keys('NombreUsuario')

@given(u'Hago clic en Siguiente')
def step_impl(context):
    context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[2]/div/div/form/div/div[2]/button").click()

@given(u'Selecciono dificultad Media')
def step_impl(context):
    context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[2]/div/div/form[2]/div/div[2]/input").click()

@when(u'Hago clic en siguiente')
def step_impl(context):
    context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[2]/div/div/form[2]/div/button").click()

@then(u'La dificultad mostrada es la correcta')
def step_impl(context):
    text = context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[1]/div/p[1]").text
    assert text == "DIFICULTAD: 2"


