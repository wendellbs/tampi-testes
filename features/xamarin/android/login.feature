Funcionalidade: Realizar o login

  Cenário: Efetuando o login válido
    Dado que quero efetuar o login
    # E estou na tela de login
    # E preencho o campo de id login__input-email com o valor yuri@teste.com
    # E preencho o campo de id login__input-password com o valor senha_do_yuri@teste.com
    # Quando clico no automation_id Field_Username
    E preencho o campo Field_Username com o valor abc
    E preencho o campo Field_Password com o valor 1234
    Quando eu clico no botao Button_Login
    Então sou direcionado para a tela de Listagem de Contatos

  