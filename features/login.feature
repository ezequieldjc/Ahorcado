Feature: Login
    """
        El Login Feacture probara el ingreso del nombre en el juego
    """
    Scenario: Prueba de éxito para Ingresar Nombre
        Given Que navego para jugar en la página
        And Ingreso un nombre de usuario
        When Hago clic en el botón Siguiente
        Then El inicio del juego es exitoso



