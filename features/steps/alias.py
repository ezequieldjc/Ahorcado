from behave import given, when, then

@given(u'Que ingreso la dificultad elegida')
def step_impl(context):
    context.browser.get('https://agiles2020-ahorcado.herokuapp.com/play/')

@when(u'Hago clic en siguiente')
def step_impl(context):
    context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[2]/div/div/form/div/div[2]/button").click()

@then(u'La dificultad mostrada es la correcta')
def step_impl(context):
    assert context.browser.current_url == 'https://agiles2020-ahorcado.herokuapp.com/play/alias'


