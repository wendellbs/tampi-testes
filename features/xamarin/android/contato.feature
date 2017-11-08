Funcionalidade: Realizar o cadastro de contatos

  Esquema do Cenário: Cadastro de um contato válido
    Dado que quero cadastrar um contato
    E estou na tela Page_Main
    Quando eu clico no botao Button_Add
    Então sou direcionado para a tela Page_User
    E preencho o campo Field_Name com o valor <nome>
    E preencho o campo Field_Email com o valor <email>
    Quando eu clico no botao Button_Save
    Então sou direcionado para a tela Page_Main

    Exemplos: Dados para cadastro de contatos.
      | nome    | email                |
      | Andre   | andre@email.com.br   |
      | Daniel  | daniel@email.com.br  |


  Esquema do Cenário: Cadastro de um contato inválido
    Dado que quero cadastrar um contato
    E estou na tela Page_Main
    Quando eu clico no botao Button_Add
    Então sou direcionado para a tela Page_User
    E preencho o campo Field_Name com o valor <nome>
    E preencho o campo Field_Email com o valor <email>
    Quando eu clico no botao Button_Save
    Então aparece uma mensagem de Erro
    E eu clico no botao OK pelo xpath /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button
    E pressiono o botao voltar no celular
    E sou direcionado para a tela Page_Main

    Exemplos: Dados para cadastro de contatos.
      | nome    | email               |
      | Rafael  | rafael@email.com.br |
      | Amanda  | amanda.email.com.br |
