from PIL import Image
import pytesseract
import os
import glob       
import string

vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'
restaura_cor_original = '\033[0;0m'
negrito = '\033[1m'
reverso = '\033[2m'
fundo_preto = '\033[40m'
fundo_vermelho = '\033[41m'
fundo_verde = '\033[42m'
fundo_amarelo = '\033[43m'
fundo_azul = '\033[44m'
fundo_magenta = '\033[45m'
fundo_ciano = '\033[46m'
fundo_branco = '\033[47m'

def banner():
    print "========================================================================"
    print "|       lll                                    dd                      |"
    print "|       lll   eee   gggggg   eee  nn nnn       dd  sss                 |"
    print "|       lll ee   e gg   gg ee   e nnn  nn  dddddd s                    |"
    print "|------------------------------------------------------------------>   |"
    print "|       lll eeeee  ggggggg eeeee  nn   nn dd   dd  sss                 |"
    print "|       lll  eeeee      gg  eeeee nn   nn  dddddd     s                |"
    print "|                   ggggg                          sss                 |"
    print "========================================================================"
    print "                                                   Google Tesseract v1.0"
    print ""  

os.system('clear')
banner()

for i in (glob.glob("img/*.png") or glob.glob("img/*.jpg")):
    text = pytesseract.image_to_string(Image.open(i), lang='por')
    
    print(branco + '====== Texto na Imagem ===================================\n')
    print(branco + '--Nome :: '+amarelo+i+'\n')
    print(amarelo + '====== Texto na Imagem ===================================\n')
    print (amarelo + text)
    
    nome = string.replace(i,'img/','')
    nome = string.replace(nome,'.jpg','')
    nome = string.replace(nome,'.png','')
    
    arquivo = open('text/%s.txt'%nome,'w')
    arquivo.write(text.encode('utf-8'))
    arquivo.close()
