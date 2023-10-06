CTF Semana #3 (Wordpress CVE)

Tarefas:

1. Reconhecimento - Após uma análise do website, chegando a uma página que listava os plugins usados e a versão dos mesmos. pesquisei por CVE's relacionados a estes. Após esta, deparei-me com o CVE-2021-34646.

2. Pesquisa por vulnerabilidades - Pesquisei por CVE's relacionados a estes. 

3. Escolha da vulnerabilidade - Após esta, deparei-me com o CVE-2021-34646. Uma vulnerabilidade pertinente ao plugin "Booster for WooCommerce WordPress plugin".

4. Encontrar um exploit - Tendo conhecimento do CVE, iniciei uma pesquisa por exploits resultantes desta vulnerabilidade. Encontrei um [website](https://www.wordfence.com/blog/2021/08/critical-authentication-bypass-vulnerability-patched-in-booster-for-woocommerce/) a descrever os detalhes de um possível exploit.

5. Explorar a vulnerabilidade - Seguindo os passos do exploit, comecei por enviar o pedido de verificação da conta com id=1. Escolhi este id porque logicamente, sendo a primeira ou segunda conta criada, esta foi usada como testes pelos desenvolvedores do website e por consequência têm privilégios de administrador. Realizei este pedido entrando no URL "http://ctf-fsi.fe.up.pt:5001/?wcj_user_id=1". Anotei em que segundo realizei esta ação usando um relógio em Unix Timestamp em tempo real.
Após o envio de confirmação de conta, o usuário recebe um URL no seu e-mail ao qual, acedendo, é gerado uma sessão autenticada nessa mesma conta. De acordo com o código-fonte do plugin, este URL de confirmação é codificado de de acordo com o id da conta e o tempo no qual o pedido foi realizado. Desta maneira, assumindo que realizei o pedido de confirmação no segundo "1696622768", o link seria construído da segunte forma:

 - É realizada a conversão do Timestamp para MD5 Hash. O valor "1696622768" é codificado para "6b8214322afb07366f3ef2a75ab4e70d".
 - A contrução de um JSON é realizada, encodado com os pares "key"\_"value" seguintes: "id"\_"1" e "code"_"6b8214322afb07366f3ef2a75ab4e70d".
 - De seguida, a conversão do mesmo JSON body para base64 é realizada: "ewoiaWQiOiAxLAoiY29kZSI6ICI2YjgyMTQzMjJhZmIwNzM2NmYzZWYyYTc1YWI0ZTcwZCIKfQ=="
 - Por ultimo, este payload é usado como valor do URL "wcj_verify_email" e, se o tempo de realização de pedido estiver correto, uma sessão autenticada na conta de id=1 é iniciada.
 - Desta forma, foi utilizado o seguinte URL: "http://ctf-fsi.fe.up.pt:5001/?wcj_verify_email=ewoiaWQiOiAxLAoiY29kZSI6ICI2YjgyMTQzMjJhZmIwNzM2NmYzZWYyYTc1YWI0ZTcwZCIKfQ=="

Quando realizei este exploit, precisei de tentar com três diferentes valores de tempo pois por motivos de atraso temporal, tanto pela parte do servidor de receção do pedido, como pelo atrado do relógio de Unix Timestamp, mas após a terceira tentativa fui recebido com uma página de confirmação de verificação de conta, na qual verifiquei que estava logado com a mesma conta. Por fim, acedi ao quadro de mensagens privadas de administradores e capturei a bandeira lá presente.
