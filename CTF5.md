CTF Semana #5 (Buffer Overflow)

Após a leitura introdutória deste CTF, baixamos os ficheiros necessários para o seu desenvolvimento.

**Desafio #1:**

Ispencionando o código-fonte do desafio, verificamos que o programa prepara num buffer chamado "meme_file" o nome de um ficheiro que irá ser lido. Também inicializa um buffer de 32 bytes chamado "buffer".

De seguida, o programa chama a função "scanf()" que recebe stream information do usuário e escreve-a num buffer. Neste caso, recebe a stream e tranforma-a numa formatted string de 40 characters e escreve-a na variável "buffer" mencionada previamente.

Por fim, o programa tenta abrir o ficheiro cujo nome é igual ao presente na variável "meme_file" e chama a função "fgets" para escrever 32 bytes presentes no ficheiro na variável "buffer". Assim que é verificado que esta função ocorreu com sucesso, os conteúdos de "buffer" são imprimidos na consola.

Tendo em conta esta funcionalidade e o código presente no ficheiro "exploit-example.py", desenvolver o exploit para este programa tornou-se bastante claro. Apenas teriamos de escrever 40 bytes para o stream a ser escrito em buffer e ter a certeza que os últimos 8 bytes, aqueles que seriam fora do buffer da variável "buffer" seriam exatamente a palavra "flag.txt" seguido de um "null terminator" para que o programa reescrevesse os conteúdos de "meme_file" para o ficheiro pretendido. Assim, o nosso payload constitiu-se de 32 bytes filler, que seriam guardados na variável "buffer", e 8 bytes a soletrar "flag.txt", segundo a ASCII table, seguido de um "\\0" para proporcionar ao programa a informação de quando parar de ler o conteúdo de "meme_file". Após testar com o ficheiro local e obter o "flag_placeholder", desativamos a flag "debug" presente no exploit e realizamos o ataque no servidor, obtendo assim a flag.


**Desafio #2:**

Com mais uma inspeção do código, verificamos que este seria parecido com o presente no desafio 2, com a diferença de que este agora presentava um buffer chamado "val" de 4 bytes entre as variáveis "buffer" e "meme_file" que agora presentava 9 bytes em vez de 8. 

Para além disso, o código presentava uma condição para poder aceder à funcionalidade de leitura do ficheiro presente em "meme_file" na forma de verificação de igualdade entre um valor predefinido e o valor presente em "val" uma vez interpretando este como um pointer de um valor inteiro.

Por fim, o valor de bytes lidos pela função de leitura de stream de input seria agora 45 bytes, diferente dos 40 do desafio anterior.

Devido às similaridades entre os desafios, copiamos o exploit utilizado no desafio 1 para uso neste desafio. O payload utilizado diferenciou-se apenas nos bytes escrito após os 32 bytes filler, mais uma vez utilizados para maximizar o buffer da variável "buffer". Os 4 bytes escritos de seguida foram os bytes descrevendo o valor predefinido comparado com o buffer da variável "val". Estes foram escritos com o cuidado de inverter a sua ordem de escrita devido à arquitetura do processador ser "little endian", o que proporciona a leitura dos bytes mais significativos à direita e lendo para a esquerda ate encontrar o byte menos significativo. Desta forma, foi escrito com sucesso em cima do buffer de "val" o valor da confição de acesso à leitura do ficheiro. Mais uma vez, foram escritos 9 bytes para o buffer de "meme_file" na forma da soletração da palavra "flag.txt\\0", abrindo assim o ficheiro "flag.txt" no lugar do ficheiro "mem.txt" originalmente pretendido pelo programa. MAis uma vez, os primeiros 32 bytes do conteúdo do ficheiro aberto foram escritos para o buffer da variável "buffer" e, após verificar a funcionalidade localmente com a utilização de um ficheiro "flag.txt" local e a escrita da string "flag_placeholder" na consola do programa, desativou-se o modo debug, atacando o servidor com o exploit desenvolvido. Desta forma, obtemos a flag.
