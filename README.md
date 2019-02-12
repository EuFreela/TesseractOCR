# TesseractOCR
Biblioteca de reconhecimento ótico de caracteres da Google, Open Source

<p>
  <b>Tesseract</b> é um software de reconhecimento ótico de caracteres de código aberto (Licença Apache 2.0)[1], originalmente desenvolvido pela Hewlett-Packard e foi por um tempo mantido pelo Google; atualmente o projeto está hospedado no GitHub.

Se aplica a imagens em formato tiff com texto puro em uma única coluna, convertendo a saída em um arquivo txt. Não possui mecanismos para reconhecimento de layout, desta forma não é recomendável para textos que possuam imagens, fórmulas ou mais de uma coluna. 
</p>

<hr>

### INSTALL


### EXEMPLE
<p>
Insira na pasta "img" as imagens com texto que deseja extrair.
No diretório "txt" extarão os textos extraídos das imagens.
  <b>Obs:</b> Os nomes para os arquivos textos respeitam os nomes dados às imagens. Serão criados os arquivos ".txt" nomeados com o mesmo nome das imagens carregadas

Existem 3 imagens de teste dentro do diretório "img". Ao ser processado serão gerados 3 arquivos textos no diretório "txt" que correspondem ao texto retirado da imagem. 

Esse script é útil quando há documentos digitalizados que precisam serem digitados. Um amigo me pediu para digitar algumas musicas suas, porém, são muitas. Esse é o recurso que utilizei depois de scanear todo o caderno. Bastou inserir as imagens na pasta e processar 600 imagens. Uma mão na roda!

Ainda é preciso utilizar uma rede neural para treinar o algoritmo de acordo com a caligrafia de cada fulano. Prtanto, quanto mais doida a caligrafia, deixa de ser mais preciso.

Start:
</p>
<pre>
python google_text_provider.py
</pre>

<img src="https://i.postimg.cc/qvvq8D1N/Captura-de-tela-em-2019-02-12-16-07-33.png">
<img src="https://i.postimg.cc/t4wShw9k/Captura-de-tela-em-2019-02-12-16-03-27.png">

