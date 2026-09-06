from app.models.download_info import DownloadInfo

downloads = []
contador_id =1

def salvar_download(download: DownloadInfo):
    global contador_id
    download.id = contador_id
    downloads.append(download)
    contador_id += 1


def listar_downloads():
    return downloads

def buscar_download_por_id(id: int):
    for download in downloads:
        if download.id == id:
            return download
    return None
