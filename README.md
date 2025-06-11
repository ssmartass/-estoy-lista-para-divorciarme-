# -estoy-lista-para-divorciarme-
Proyecto de IA emocional para ayudar a reflexionar sobre la preparación emocional ante un posible divorcio.
# ¿Estoy lista para divorciarme?

Proyecto de curso de desarrollo de IA — Final project for the Building AI course

## Summary

Este proyecto utiliza inteligencia artificial para acompañar emocionalmente a personas que se plantean el divorcio, ofreciéndoles una herramienta de reflexión personalizada y empática basada en sus respuestas. Proyecto de curso de desarrollo de IA.

## Background

Tomar la decisión de divorciarse puede ser uno de los procesos más complejos a nivel emocional, psicológico y social. No siempre se trata de una cuestión clara, y muchas personas atraviesan momentos de confusión, miedo o presión externa.

Este proyecto intenta ayudar a:
* Personas que no pueden permitirse terapia inmediata
* Quienes buscan un espacio anónimo de reflexión
* Gente que necesita una guía objetiva sobre sus emociones y circunstancias

Mi motivación nace del deseo de aplicar la IA en contextos sensibles, donde las personas puedan recibir orientación sin juicios ni diagnósticos tajantes.

## How is it used?

El usuario responde a una serie de preguntas en escala (0 a 10) y binarias (sí/no) relacionadas con:
- Estado emocional
- Red de apoyo
- Independencia económica
- Confianza, seguridad y bienestar personal

El sistema analiza las respuestas y devuelve:
- Una puntuación global (0 a 100) interpretada como "nivel de preparación emocional"
- Un mensaje de reflexión personalizado
- Sugerencias, como hablar con un terapeuta, planificar la independencia o revisar si hay presión externa

<img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Divorce_icon.svg" width="200">

## Data sources and AI methods

Este modelo está basado en datos sintéticos simulados para proteger la privacidad. El sistema se basa en:
- Regresión logística para clasificación binaria (lista/no lista)
- Análisis ponderado de respuestas mediante scoring lineal
- Umbrales definidos en función de patrones psicológicos publicados

Ejemplo de código:

```python
def evaluar_respuestas(respuestas):
    pesos = [0.25, 0.25, 0.2, 0.15, 0.15]  # ejemplo de ponderación para 5 preguntas
    puntuacion = sum([r * p for r, p in zip(respuestas, pesos)])
    if puntuacion >= 7:
        return "Parece que estás emocionalmente preparada. Busca apoyo profesional para seguir avanzando."
    else:
        return "Todavía hay aspectos importantes que explorar. Tal vez aún no estás lista. Cuídate."

# Ejemplo de uso
respuestas = [9, 8, 6, 5, 7]
print(evaluar_respuestas(respuestas))
Challenges
No puede reemplazar a un terapeuta, abogado o decisión personal.

La interpretación del modelo no debe tomarse como consejo definitivo.

Los sesgos culturales, económicos o de género pueden afectar la percepción de las preguntas.

El uso debe ser consciente y responsable.

What next?
Me gustaría desarrollar:

Una interfaz sencilla en móvil

Más preguntas adaptadas a distintas realidades (hijos, violencia, religión, migración)

Una red de apoyo con recursos reales (contactos de ayuda)

Necesitaré:

Colaboración con psicólogos y terapeutas

Testeo ético y con retroalimentación de usuarios reales

Revisión de lenguaje inclusivo y no manipulativo

Acknowledgments
Inspirado por relatos personales y testimonios reales.

Basado en principios éticos de IA empática.

Icono del proyecto: Divorce icon by Milken Institute / CC BY-SA 3.0

Agradecimientos al curso Building AI por abrir la puerta a proyectos con impacto humano.
