Feature: Dificultad
    """
        La dificultad ingresada es la que se muestra durante el juego
    """
    Scenario: Prueba de éxito para la dificultad ingresada
        Given Que navego para jugar en la página
        And Ingreso un nombre de usuario
        And Hago clic en Siguiente
        And Selecciono dificultad Media
        When Hago clic en siguiente
        Then La dificultad mostrada es la correcta