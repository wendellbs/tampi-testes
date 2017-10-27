# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# from pwa_driver import PwaDriver
from android_driver import AndroidDriver

@given(u'que quero testar um app android')
def step_impl(context):
    context.config.driver = AndroidDriver()
    context.config.driver.platform_name = 'Android'

@given(u'a versão da plataforma é {platform_version}')
def step_impl(context, platform_version):
    context.config.driver.platform_version = platform_version

@given(u'o nome do device é {device_name}')
def step_impl(context, device_name):
    context.config.driver.device_name = device_name

@given(u'o app a ser testado é {app}')
def step_impl(context, app):
    context.config.driver.app = '/root/tmp/' + app

@given(u'o servidor está em {remote}')
def step_impl(context, remote):
    context.config.driver.remote = remote

@when(u'tento inicializar o teste')
def step_impl(context):
    context.config.driver.open()

@then(u'recebo um status ok')
def step_impl(context):
    pass

@given(u'que quero efetuar o login')
def step_impl(context):
    pass

@given(u'estou na tela {screen}')
def step_impl(context, screen):
    context.config.driver.screen_assert_equal(screen)

@when(u'clico no xpath {campo}')
@given(u'clico no xpath {campo}')
def step_impl(context, campo):
    # import pdb ; pdb.set_trace()
    # context.config.driver.find_element_by_xpath('@AutomationId=Field_Username')
    context.config.driver.find_element_by_xpath(campo).click()

@then('sou direcionado para a tela de {screen}')
def step(context, screen):
    context.config.driver.screen_assert_equal(screen)
