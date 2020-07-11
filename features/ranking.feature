Feature: Ranking_ordenado
    """
        El Ranking Feature probara que los ranking se muestren oredenados de forma decreciente
    """
    Scenario: Prueba que los rankings se encuentren ordenados
        Given Que ingreso al ranking
        When Comparo el ranking1 con el ranking 2
        Then El ranking1 es mayor o igual al ranking2
