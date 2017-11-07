Funcionalidade: Realizar o setup do teste para Android

  Cenário: Setup do Android
    Dado que quero testar um app Android
    E a versão da plataforma é 6.0
    E o nome do device é Nexus_4_API_23
    E o app a ser testado é Zamium.Droid.apk
    E o servidor está em http://localhost:4723/wd/hub
    Quando tento inicializar o teste
    Então recebo um status ok
