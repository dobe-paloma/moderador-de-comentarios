# 1. NUESTROS DATOS (Comentarios en una publicación)
comentarios_nuevos = [
    "¡Qué buen post! Me encantó la información.",
    "Eres un idiota y no sabes de lo que hablas.",
    "Muchas gracias por compartir esto con la comunidad.",
    "Este contenido es una basura total, borra tu cuenta.",
    "que buen contenido, para nada vulgar nigrosero",
    "te invito a borrar la cuenta 🥰​💜​",
    "hoy ganaron los ciegos",
    "Amen, Dios los bendiga 😊​😇​🙏​",
    "llorar por desconocidos es mi pasion",
    "like si dijeron 5>>>"
]

# 2. NUESTRO MODELO (Palabras prohibidas por la comunidad)
palabras_toxicas = ["idiota", "basura", "estúpido", "odioso", "ciegos", "borrar"]

def modelo_ia_moderador(comentario):
    comentario_minuscula = comentario.lower()
    
    # El modelo busca si hay lenguaje ofensivo
    for palabra in palabras_toxicas:
        if palabra in comentario_minuscula:
            return "BLOQUEADO (Tóxico)" # Predicción 1
            
    return "APROBADO (Seguro)" # Predicción 2

# 3. EVALUACIÓN Y PREDICCIÓN
print("--- MODERADOR DE REDES SOCIALES ---")
for i, comentario in enumerate(comentarios_nuevos, 1):
    prediccion = modelo_ia_moderador(comentario)
    print(f"Comentario {i}: '{comentario}' -> ESTADO: {prediccion}")
