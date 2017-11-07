Funcionalidade: Realizar o login

  Cenário: Efetuando o login inválido
    Dado que quero efetuar o login
    E estou na tela Page_Login
    E preencho o campo Field_Username com o valor Marcelo
    E preencho o campo Field_Password com o valor 12345
    Quando eu clico no botao Button_Login
    Então aparece uma mensagem de Antenção
    E eu clico no botao OK pelo xpath /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button

  Cenário: Efetuando o login válido
    Dado que quero efetuar o login
    E estou na tela Page_Login
    E preencho o campo Field_Username com o valor abc
    E preencho o campo Field_Password com o valor 1234
    Quando eu clico no botao Button_Login
    Então sou direcionado para a tela Page_Main
