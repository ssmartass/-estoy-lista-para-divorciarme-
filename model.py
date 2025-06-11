# model.py

# Este es un modelo muy básico que evalúa si alguien parece emocionalmente preparado para divorciarse,
# basado en una serie de 5 respuestas en escala de 0 a 10.

def evaluar_respuestas(respuestas):
    """
    Recibe una lista de 5 números (entre 0 y 10) que representan:
    1. Siento que ya lo he intentado todo
    2. Me siento segura económicamente sola
    3. Tengo apoyo emocional fuera de mi pareja
    4. Duermo mejor sola
    5. Estoy en paz con la idea del cambio

    Devuelve un mensaje de reflexión personalizado.
    """

    pesos = [0.25, 0.25, 0.2, 0.15, 0.15]  # ponderaciones para cada pregunta
    puntuacion = sum([r * p for r, p in zip(respuestas, pesos)])

    print("Puntuación total:", puntuacion)

    if puntuacion >= 7:
        return "Parece que estás emocionalmente preparada. Busca apoyo profesional para seguir avanzando."
    else:
        return "Todavía hay aspectos importantes que explorar. Tal vez aún no estás lista. Cuídate."

# Ejemplo de uso:
if __name__ == "__main__":
    respuestas_ejemplo = [9, 8, 6, 5, 7]  # Puedes cambiar estos valores para probar
    resultado = evaluar_respuestas(respuestas_ejemplo)
    print("Resultado:", resultado)
