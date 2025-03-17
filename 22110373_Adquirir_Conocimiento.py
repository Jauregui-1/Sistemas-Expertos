#Rodriguez Jauregui Jared   22110373

import json  # Importamos la librería JSON para manejar archivos de datos estructurados en formato JSON.

# Definimos el nombre del archivo donde se almacenará la base de conocimiento del chatbot.
DB_FILE = "knowledge.json"

# Función para cargar la base de conocimiento desde un archivo JSON.
# Si el archivo no existe, se crea una base de datos con respuestas predeterminadas.
def load_knowledge():
    try:
        # Intentamos abrir y leer el archivo JSON con la base de conocimiento
        with open(DB_FILE, "r") as file:
            return json.load(file)  # Cargamos el contenido JSON en un diccionario
    except FileNotFoundError:
        # Si el archivo no existe, retornamos una base de conocimiento inicial con respuestas predeterminadas
        return {
            "Hola" : "Hola, como estas?",
            "Como estas?": "Bien, gracias. Y tu?",
            "De que te gustaria hablar?": "Podemos hablar de cualquier tema que desees."
        }

# Función para guardar la base de conocimiento en un archivo JSON
def save_knowledge(knowledge):
    with open(DB_FILE, "w") as file:
        json.dump(knowledge, file, indent=4)  # Guardamos el diccionario en formato JSON con una indentación de 4 espacios

# Función principal del chatbot
def chat():
    knowledge = load_knowledge()  # Cargamos la base de conocimiento al iniciar el chat
    print("Chatbot: ¡Hola! Escribe 'salir' para terminar la conversación.")
    
    while True:  # Bucle infinito para permitir interacción continua con el chatbot
        user_input = input("Tú: ")  # Pedimos la entrada del usuario
        
        if user_input.lower() == "salir":  # Si el usuario escribe "salir", se termina el chat
            print("Chatbot: ¡Hasta luego!")
            break  # Salimos del bucle
        
        if user_input in knowledge:  # Si la pregunta ya está en la base de conocimiento
            print(f"Chatbot: {knowledge[user_input]}")  # Respondemos con la respuesta almacenada
        else:
            # Si no conocemos la respuesta, pedimos al usuario que nos enseñe una
            print("Chatbot: No conozco esa respuesta. ¿Cómo debería responder?")
            new_response = input("Tú: ")  # El usuario ingresa la respuesta deseada
            
            # Guardamos la nueva pregunta y respuesta en la base de conocimiento
            knowledge[user_input] = new_response
            save_knowledge(knowledge)  # Guardamos la base de conocimiento actualizada en el archivo JSON
            
            print("Chatbot: ¡Gracias! Ahora lo recordaré para la próxima vez.")

# Verificamos si el script se ejecuta directamente
if __name__ == "__main__":
    chat()  # Iniciamos el chatbot
