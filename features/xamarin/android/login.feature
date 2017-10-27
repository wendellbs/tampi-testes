Funcionalidade: Realizar o login com sucesso

  Cenário: Efetuando o login válido
    Dado que quero efetuar o login
    E estou na tela Zap Conecta
    # E preencho o campo de id login__input-email com o valor yuri@teste.com
    # E preencho o campo de id login__input-password com o valor senha_do_yuri@teste.com
    Quando clico no xpath android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.Button
    Então sou direcionado para a tela de Listagem de Contatos
