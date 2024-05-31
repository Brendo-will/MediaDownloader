
# MediaDownloader

Este projeto permite baixar vídeos do YouTube e Instagram utilizando as bibliotecas `pytube` e `instaloader`. Você pode escolher entre baixar o vídeo completo ou apenas o áudio do YouTube, e baixar vídeos do Instagram.

## Funcionalidades

- Baixar vídeos completos do YouTube
- Baixar apenas o áudio de vídeos do YouTube
- Baixar vídeos do Instagram

## Requisitos

- Python 3.6+
- pytube
- instaloader
- pywebio

## Instalação

1. Clone o repositório:
git clone https://github.com/Brendo-will/MediaDownloader.git
cd MediaDownloader

2. Crie um ambiente virtual (opcional, mas recomendado):
python -m venv venv
source venv/bin/activate # No Windows use `venv\Scripts\activate`

3. Instale as dependências:
pip install -r requirements.txt

##Uso 
1. Execute o script:
python youtube_instagram_downloader.py

## Estrutura do projeto 
MediaDownloader/
├── downloads/
├── youtube_instagram_downloader.py
├── requirements.txt
└── README.md

downloads/: Diretório onde os vídeos baixados serão salvos.
youtube_instagram_downloader.py: Script principal para baixar vídeos do YouTube e Instagram.
requirements.txt: Lista de dependências do projeto.
README.md: Este arquivo de documentação.

