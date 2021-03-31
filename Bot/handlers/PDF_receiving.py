from loader import bot, logger

import os

from pdf2image import convert_from_path

@logger.catch()
def convertPdf(pdfPath, imgMainDir, src):
    imgPath = imgMainDir + '/' + src[0]#треба. щоб перша цифра назви файлу вказувала на курс
    if not os.path.exists(imgPath):
        os.mkdir(imgPath)
    pages = convert_from_path(pdfPath + '/' + src, 200)
    
    for i, page in enumerate(pages):
        path = f'{imgPath}/{i+1}.jpg'
        page.save(path, 'JPEG')
        logger.info(f'JPRG {path} created')
    
    os.remove(pdfPath + '/' + src)#видалення pdf-файлу пісял розбиття


@bot.message_handler(content_types = ['document'])
@logger.catch
def file_receiving(message):
  #use admins id
  save_dir = 'Data/stud_files/PDFs'#директорія з pdf файлами
  if str(message.chat.id) == 'your id':#цю частину дороблю потім
    src = message.document.file_name
    if '.pdf' in src:#перевіркана типу фвйлу
      file_id_info = bot.get_file(message.document.file_id)
      downloaded_file = bot.download_file(file_id_info.file_path)
      with open(save_dir + "/" + src, 'wb') as new_file:
        new_file.write(downloaded_file)
      logger.info(f'filename is {message.document.file_name}')
      bot.send_message(message.chat.id, 'pdf downloaded')

      convertPdf(save_dir,'Data/stud_files/JPGs', src)#орзбиття документу на фото
    else:
      bot.send_message(message.chat.id, 'another type of file sended')
    