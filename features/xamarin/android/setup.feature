Funcionalidade: Realizar o setup do teste para Android

  Cenário: Setup do Android
    Dado que quero testar um app android
    E a versão da plataforma é 7.1.1
    E o nome do device é emulator-5554
    E o app a ser testado é Zamium.Droid.apk
    E o servidor está em http://localhost:4723/wd/hub
    Quando tento inicializar o teste
    Então recebo um status ok
