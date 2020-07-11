from behave import given, when, then

@given(u'Que ingreso al ranking')
def step_impl(context):
    context.browser.get('https://agiles2020-ahorcado.herokuapp.com/rank')

@when(u'Comparo el ranking1 con el ranking 2')
def step_impl(context):
    ranking1 = context.browser.find_element_by_xpath(f"/html/body/div/div/table/tbody/tr[1]/td[3]")
    ranking2 = context.browser.find_element_by_xpath(f"/html/body/div/div/table/tbody/tr[3]/td[3]")
    

@then(u'El ranking1 es mayor o igual al ranking2')
def step_impl(context):
    ranking1 = context.browser.find_element_by_xpath(f"/html/body/div/div/table/tbody/tr[1]/td[3]").text
    ranking5 = context.browser.find_element_by_xpath(f"/html/body/div/div/table/tbody/tr[9]/td[3]").text
    ranking10 = context.browser.find_element_by_xpath(f"/html/body/div/div/table/tbody/tr[19]/td[3]").text
    assert int(ranking1) >= int(ranking5) and int(ranking5) >= int(ranking10)