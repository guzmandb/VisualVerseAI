from flask import Flask, render_template, request
import PIL
import tensorflow as tf
import keras_cv
import lyricsgenius
import imageio
import os
import pytube
from keras_cv.models import StableDiffusion
from PIL import Image
from moviepy.editor import VideoFileClip, AudioFileClip


app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    from flask import Flask, render_template, request
    import PIL
    import tensorflow as tf
    import keras_cv
    import lyricsgenius
    import imageio
    import os
    import pytube
    from keras_cv.models import StableDiffusion
    from PIL import Image
    from moviepy.editor import VideoFileClip, AudioFileClip
    archivo_letra=request.files['archivo_letra']
    archivo_ruta = "./letras/" + archivo_letra.filename
    archivo_letra.save(archivo_ruta)
    
    ###### UTILIZAR TODA LA MEMORIA
    import tensorflow as tf
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
            try:
                # Configura TensorFlow para utilizar toda la memoria de la GPU
                for gpu in gpus:
                    tf.config.experimental.set_memory_growth(gpu, True)
                logical_gpus = tf.config.experimental.list_logical_devices('GPU')
                print(len(gpus), "GPU(s) físicas,", len(logical_gpus), "GPU(s) lógicas")
            except RuntimeError as e:
                print(e)

    ###### UTILIZAR TODA LA CPU
    
    os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"

    ###### GENERADOR DE IMAGEN POR CADA PARRAFO
    from keras_cv.models import StableDiffusion
    from PIL import Image

    # Leer las letras desde el archivo
    with open("./letras/letras.txt", "r", encoding="utf-8") as file:
        lyrics = file.read()

    # Dividir el texto en párrafos
    paragraphs = lyrics.split("\n\n")

    # Generar una imagen por cada párrafo
    model = StableDiffusion(img_height=512, img_width=512, jit_compile=True)
    for i, paragraph in enumerate(paragraphs):
        # Generar la imagen a partir del párrafo
        img = model.text_to_image(
            prompt=paragraph,
            batch_size=1,
            num_steps=6,
            seed=123
        )
        # Guardar la imagen con un nombre único
        image_path = f"./imagenes/image_{i}.png"
        Image.fromarray(img[0]).save(image_path)
        print(f"Imagen guardada en '{image_path}'.")

    print("Proceso completado.")

    import os
    import imageio
    image_folder = "./imagenes/"
    output_video = "./videos/video.mp4"
        
    # Obtener la lista de archivos de imagen en la carpeta
    image_files = sorted([file for file in os.listdir(image_folder) if file.endswith(".png")])
    # Crear una lista de imágenes
    images = []
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        images.append(imageio.imread(image_path))
        print(f"Leyendo imagen: {image_file}")
    
    # Enlace del video de YouTube
    link = request.form['linkyoutube']

    # Descargar el video
    yt = pytube.YouTube(link)
    stream = yt.streams.get_highest_resolution()
    stream.download()

    # Obtener la duración del video
    duration = yt.length
    print("La duración del video es:", duration, "segundos")

    streams = yt.streams.filter(only_audio=True)
    audio_path = None

    # Intentar descargar el audio en diferentes formatos
    for stream in streams:
        if stream.mime_type == 'audio/mp4':
            # Descargar en formato M4A
            audio_path = stream.download(output_path='.', filename='audio')
            break
        elif stream.mime_type == 'audio/webm':
            # Descargar en formato WEBM
            audio_path = stream.download(output_path='.', filename='audio')
            break

    if audio_path:
        # Convertir el audio a formato MP3 si es necesario

        # Obtener la ruta del archivo descargado
        audio_mp3_path = audio_path.replace('.mp4', '.mp3')
        audio_webm_path = audio_path.replace('.webm', '.mp3')
        audio_path = audio_mp3_path if audio_mp3_path != audio_path else audio_webm_path

        # Renombrar el archivo al formato MP3
        
        os.rename(audio_path, './audios/audio.mp3')

        print("Archivo de audio descargado: audio.mp3")
    else:
        print("No se encontró ninguna opción de formato de audio disponible.")
            
        # Calcular el número de imágenes por segundo para lograr la duración deseada
    
    # Duración en segundos\
    desired_duration = duration  
    num_images = len(images)
    fps = num_images / desired_duration
        
    
    # Guardar el video utilizando imageio con la duración ajustada
    imageio.mimwrite(output_video, images, fps=fps)

    from moviepy.editor import VideoFileClip, AudioFileClip

    # Rutas de los archivos de video y audio
    video_path = "./videos/video.mp4"
    audio_path = "./audios/audio.mp3"

    # Cargar el video y el audio
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # Asegurarse de que la duración del audio sea igual o menor a la duración del video
    if audio_clip.duration > video_clip.duration:
        audio_clip = audio_clip.subclip(0, video_clip.duration)

    # Agregar el audio al video
    video_clip = video_clip.set_audio(audio_clip)

    # Guardar el nuevo video con el audio agregado
    output_path = "./videos/video_con_audio.mp4"
    video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    video_final = "./videos/video_con_audio.mp4"
    ##### SUBS PRIMEROS CON TODA LA LINEA
    from moviepy.editor import VideoFileClip
    from moviepy.editor import TextClip
    from moviepy.editor import CompositeVideoClip

    # # Ruta del archivo de video
    video_path1 = "./videos/video_con_audio.mp4"

    # # Ruta del archivo de subtítulos en formato txt
    subtitles_path = "./letras/letras.txt"

    # # Cargar el video
    video_clip = VideoFileClip(video_path1)


    # # Crear el clip de subtítulos
    
    def agregar_subtitulos(video_path, subtitle_path, output_path):
        # Cargar el video
        video = VideoFileClip(video_path)

        # Cargar el archivo de subtítulos
        with open(subtitle_path, 'r') as file:
            subtitles = file.readlines()

        # Dividir los subtítulos en dos partes
        midpoint = len(subtitles) // 2
        subtitles_part1 = subtitles[:midpoint]
        subtitles_part2 = subtitles[midpoint:]

        # Crear un clip de texto con la primera mitad de los subtítulos
        subtitle_clip_part1 = TextClip(''.join(subtitles_part1), fontsize=20,color="white",stroke_width=1, stroke_color='black').set_position(('center', 'center'))

        # Ajustar la duración del clip de subtítulos para que coincida con la mitad del video
        subtitle_clip_part1 = subtitle_clip_part1.set_duration(video.duration / 2)

        # Crear un clip de texto con la segunda mitad de los subtítulos
        subtitle_clip_part2 = TextClip(''.join(subtitles_part2), fontsize=20, color="white",stroke_width=1, stroke_color='black').set_position(('center', 'center'))

        # Ajustar la duración y el inicio del clip de subtítulos para que aparezca en la segunda mitad del video
        subtitle_clip_part2 = subtitle_clip_part2.set_duration(video.duration / 2).set_start(video.duration / 2)

        # Combinar el video y los clips de subtítulos
        final_clip = CompositeVideoClip([video, subtitle_clip_part1, subtitle_clip_part2])

        # Guardar el video resultante
        final_clip.write_videofile(output_path, codec='libx264')

        # Liberar los recursos
        final_clip.close()
        video.close()

    # Ruta del archivo de video MP4
    videos_path1 = './videos/video_con_audio.mp4'

    # Ruta del archivo de subtítulos en formato de texto
    subtitle_path1 = './letras/letras.txt'

    # Ruta de salida para el video resultante con los subtítulos
    output_path1 = './videos/video_con_subtitulos.mp4'

    # Agregar subtítulos al video
    agregar_subtitulos(videos_path1, subtitle_path1, output_path1)

        # Combinar el video y el clip de subtítulos
    # final_clip = CompositeVideoClip([video_clip, subtitles_clip])

    #     # Ruta de salida para el video con subtítulos
    # output_path = "./videos/video_con_subtitulos.mp4"

    #     # # Guardar el nuevo video con subtítulos
    # final_clip.write_videofile(output_path, codec="libx264")
    print("Video creado correctamente.")
    

    return render_template('results.html', video_path="./videos/video_con_subtitulos.mp4")


if __name__ == '__main__':
    app.run()