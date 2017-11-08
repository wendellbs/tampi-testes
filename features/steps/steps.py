# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
from os.path import abspath, dirname
from sys import path
from time import sleep
from utils.constants import AndroidKeys
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

@given(u'que quero testar um app {type_app}')
def step_impl(context, type_app):
    context.config.platform_name = type_app

@given(u'a versão da plataforma é {platform_version}')
def step_impl(context, platform_version):
    context.config.platform_version = platform_version

@given(u'o nome do device é {device_name}')
def step_impl(context, device_name):
    context.config.device_name = device_name

@given(u'o app a ser testado é {app}')
def step_impl(context, app):
    context.config.app = app

@given(u'o servidor está em {remote}')
def step_impl(context, remote):
    context.config.remote = remote

@when(u'tento inicializar o teste')
def step_impl(context):
    desired_caps = {}
    desired_caps['platformName'] = context.config.platform_name
    desired_caps['platformVersion'] = context.config.platform_version
    desired_caps['deviceName'] = context.config.device_name
    desired_caps['app'] = PATH('./../../apps/' + context.config.app)
    driver = webdriver.Remote(context.config.remote, desired_caps)
    context.config.driver = driver
    context.config.driver.implicitly_wait(10)

@then(u'recebo um status ok')
def step_impl(context):
    pass

@given(u'que quero cadastrar um contato')
def step_impl(context):
    pass

@given(u'estou na tela {screen}')
def step_impl(context, screen):
    context.config.driver.find_element_by_accessibility_id(screen)

@when(u'eu clico no botao {botao}')
@given(u'eu clico no botao {botao}')
def step_impl(context, botao):
    try:
        context.config.driver.hide_keyboard()
    except:
        pass

    context.config.driver.find_element_by_accessibility_id(botao).click()

@given('sou direcionado para a tela {screen}')
@then('sou direcionado para a tela {screen}')
def step(context, screen):
    context.config.driver.find_element_by_accessibility_id(screen)

@then(u'preencho o campo {campo} com o valor {valor}')
@given(u'preencho o campo {campo} com o valor {valor}')
def step_impl(context, campo, valor):
    context.config.driver.find_element_by_accessibility_id(campo).click()
    context.config.driver.find_element_by_accessibility_id(campo).send_keys(valor)

@then(u'aparece uma mensagem de {mensagem}')
def step_impl(context, mensagem):
    pass

@then(u'eu clico no botao {botao} pelo xpath {xpath}')
def step_impl(context, botao, xpath):
    context.config.driver.find_element_by_xpath(xpath).click()

@then(u'pressiono o botao {botao} no celular')
def step_impl(context, botao):
    if botao == "voltar":
        context.config.driver.press_keycode(AndroidKeys.BACK)
    elif botao == "recentes":
        context.config.driver.press_keycode(AndroidKeys.RECENT_APPS)
    sleep(3)

@given(u'que quero efetuar o login')
def step_impl(context):
    pass
