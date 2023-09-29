# Trabalho realizado nas Semanas #2 e #3

CVE-2021-3156

A vulnerabilidade CVE-2021-3156 é um erro de segurança que afeta o Sudo, a command line utility do Unix e outros sistemas operativos baseados em Unix, como, por exemplo, o linux.
O Sudo é utilizado para conceder alguns privilégios de root a utilizadores não privilegiados para que estes possam executar comandos específicos. Este CVE é uma falha de buffer overflow na heap e permite que um user que não tenha privilégios de root execute código como um user privilegiado, comprometendo a segurança do sistema.
Esta vulnerabilidade afeta das versões 1.8.2 à 1.8.31p2 e da 1.9.0 até 1.9.5p1.

Foi reportada em 2021, no entanto, foi introduzida em 2011. Embora não tenha havido nenhuma bug-bounty relacionada com este CVE, é considerada uma vulnerabilidade crítica devido ao seu potencial para conceder privilegias de root. Aquando da sua descoberta, foi lançada uma correção para resolver a vulnerabilidade e o projeto Sudo avisou os utilizadores para atualizarem as suas instalações.

Foi constatado que numa das funções do código fonte do sudo existia um ciclo que teoricamente poderia resultar num buffer overflow. Isso não acontece normalmente, pois os objetos utilizados por esta função são primeiro sujeitos a um parsing desempenhado por uma outra função pela qual passam primeiro, que salvaguarda este erro. Foi possível encontrar,contudo, uma combinação de flags MODE que permite que uma das funções seja executada sem a outra, com "sudoedit -s <string>".

O exploit consiste em usar força bruta para testar as várias combinações possíveis de comprimento de variáveis que são controláveis pelo user (algumas variáveis de ambiente LC e o buffer), de modo a encontrar qual destas combinações organiza a heap de maneira a que após o buffer se encontre um alvo de importância para ser overwritten pelo overflow : Heap feng shui (a arte de manipular o layout da heap a nosso favor).

Após correr o script de brute force analisaram-se os crashes registados e determinaram-se as funções relevantes. Um exemplo de uma das funções exploradas foi a "nss_lookup_function", uma função vital, responsável pela seleção das funções que são carregadas e executadas e que carrega livrarias dinâmicas. Torna-se possível assim controlar que livrarias são carregadas, correr código, e executar comandos priveligiados.
