from pytube import YouTube
from instaloader import Instaloader, Post
from pathlib import Path
from os import startfile, remove
from pywebio.input import input, select
from pywebio.output import put_text, clear
import re

def sanitize_filename(name):
    # Remove caracteres inválidos do nome do arquivo
    return re.sub(r'[\\/*?:"<>|]', "", name)

def download_youtube(video_link, download_option, path_to_download):
    video_url = YouTube(video_link)
    
    if download_option in ["Video Completo", "Ambos"]:
        video_stream = video_url.streams.get_highest_resolution()
        sanitized_title = sanitize_filename(video_url.title)
        video_file_path = path_to_download / f"{sanitized_title} - video.mp4"
        video_stream.download(output_path=str(path_to_download), filename=video_file_path.name)
        put_text('Video baixado com sucesso'.title()).style('color:blue;font-size:50px')
        
    if download_option in ["Apenas Áudio", "Ambos"]:
        audio_stream = video_url.streams.filter(only_audio=True).first()
        sanitized_title = sanitize_filename(video_url.title)
        audio_file_path = path_to_download / f"{sanitized_title} - audio.mp4"
        audio_stream.download(output_path=str(path_to_download), filename=audio_file_path.name)
        put_text('Áudio baixado com sucesso'.title()).style('color:blue;font-size:50px')
    
def download_instagram(video_link, path_to_download):
    loader = Instaloader()
    post = Post.from_shortcode(loader.context, video_link.split('/')[-2])
    loader.download_post(post, target=str(path_to_download))
    
    # Remove arquivos desnecessários
    for file in path_to_download.iterdir():
        if file.suffix != '.mp4':
            remove(file)
    
    put_text('Video do Instagram baixado com sucesso'.title()).style('color:blue;font-size:50px')

def video_download():
    while True:
        platform = select("Escolha a plataforma:", options=["YouTube", "Instagram"])
        video_link = input('Informe o link do video:  ')
        
        if video_link.startswith("https://"):
            path_to_download = Path('./downloads')
            
            # Cria o diretório se ele não existir
            path_to_download.mkdir(parents=True, exist_ok=True)
            
            if platform == "YouTube":
                download_option = select("Escolha a opção de download:", options=["Video Completo", "Apenas Áudio", "Ambos"])
                put_text('Fazendo download ....'.title()).style('color:red;font-size:50px')
                download_youtube(video_link, download_option, path_to_download)
                
            elif platform == "Instagram":
                put_text('Fazendo download do video do Instagram ....'.title()).style('color:red;font-size:50px')
                download_instagram(video_link, path_to_download)
            
            # Limpa as mensagens anteriores
            clear()
            
            # Abre o diretório onde os arquivos foram baixados
            startfile(path_to_download.resolve())
            
            # Limpa as mensagens novamente
            clear()

if __name__ == '__main__':
    video_download()
