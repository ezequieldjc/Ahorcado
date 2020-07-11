Feature: Dificultad
    """
        La dificultad ingresada es la que se muestra durante el juego
    """
    Scenario: Prueba de éxito para la dificultad ingresada
        Given Que entro al juego
        And Ingreso un user
        And Clic en Siguiente
        And Selecciono dificultad Media
        When Clic nuevamente en Siguiente
        Then La dificultad mostrada es la correcta