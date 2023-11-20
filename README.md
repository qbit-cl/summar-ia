# Summar-ia

Este repositorio, denominado "Summar-ia," contiene un código en Python que combina las funcionalidades de Google Cloud Speech-to-Text y OpenAI para realizar tareas de transcripción de audio y generación de texto. A continuación, se proporciona una descripción detallada del código.

## Transcripción de Audio con Google Cloud Speech-to-Text

1. **Importación de Bibliotecas:**
   - Utiliza el módulo `speech_v1p1beta1` de la biblioteca `google.cloud` para la API de Speech-to-Text de Google Cloud.
   - Importa el módulo `OpenAI` para interactuar con la API de OpenAI.

2. **Configuración del Cliente de Google Cloud Speech-to-Text:**
   - Autentica y crea un cliente de Speech-to-Text utilizando un archivo de clave de servicio (`key.json`).

3. **Lectura del Archivo de Audio:**
   - Abre y lee el contenido del archivo de audio llamado "Audio.mp3."

4. **Creación de Objeto de Audio para Transcripción:**
   - Crea un objeto `speech.RecognitionAudio` con el contenido del archivo de audio.

5. **Configuración de Reconocimiento:**
   - Define la configuración de reconocimiento, incluyendo frecuencia de muestreo, código de idioma (español de Chile) y habilita la puntuación automática.

6. **Transcripción del Audio:**
   - Utiliza el cliente de Speech-to-Text para transcribir el audio con la configuración especificada.

## Generación de Texto con OpenAI

7. **Configuración del Cliente de OpenAI:**
   - Configura un cliente de OpenAI con una clave de API válida.

8. **Generación de Texto con GPT-3.5-turbo:**
   - Utiliza el modelo de lenguaje `gpt-3.5-turbo` para generar texto en respuesta a un mensaje de usuario. El mensaje incluye la transcripción obtenida del audio.

9. **Impresión de la Respuesta de OpenAI:**
   - Imprime la respuesta generada por OpenAI, que podría contener un apunte basado en la transcripción del audio.

## Enlaces a Documentación:

- [Documentación de la API de Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text/docs)
- [Documentación de la API de OpenAI](https://beta.openai.com/docs/)

**Notas Importantes:**
- Se debe proporcionar una clave de API válida de OpenAI en el código (`api_key="API_KEY"`) para utilizar la API de OpenAI.
- El archivo de clave de servicio de Google Cloud (`key.json`) debe estar presente y contener las credenciales adecuadas para el cliente de Speech-to-Text.
