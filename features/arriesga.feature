Feature: Arriesga
    """
        Se arriesga una palabra incorrecta, y se espera la UI de fallo
    """
    Scenario: Prueba de éxito para cuando se arriesga una palabra erronea
        Given Que ingreso al juego
        And Ingreso un usuario
        And Selecciono dificultad medio
        When Arriesgo una palabra erronea
        Then Juego perdido