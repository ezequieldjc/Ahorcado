from behave import given, when, then

@given(u'Que navego para jugar en la página')
def step_impl(context):
    context.browser.get('https://agiles2020-ahorcado.herokuapp.com/play/')

@given(u'Ingreso un nombre de usuario')
def step_impl(context):
    context.browser.find_element_by_name('name').send_keys('NombreUsuario')

@when(u'Hago clic en el botón Siguiente')
def step_impl(context):
    context.browser.find_element_by_xpath(f"//input[@type='submit' and @value='Submit']").click()


@then(u'El inicio del juego es exitoso')
def step_impl(context):
    assert context.browser.current_url == 'https://agiles2020-ahorcado.herokuapp.com/play/aliasB'
    assert 'Login successful !!' in context.browser.page_source


