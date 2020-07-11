Feature: Dificultad
    """
        La dificultad ingresada es la que se muestra durante el juego
    """
    Scenario: Prueba de éxito para la dificultad ingresada
        Given Que ingreso la dificultad elegida
        When Hago clic en siguiente
        Then La dificultad mostrada es la correcta