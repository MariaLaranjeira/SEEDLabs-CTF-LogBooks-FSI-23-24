Através da análise do ficheiro index.php fornecido, concluiu-se que o início de sessão no website indicado é feito a partir de uma query em sql que busca o user cujo username e palavra passe coincidam com as fornecidas no form de login:

```sql
SELECT username FROM user WHERE username = '".$username."' AND password = '".$password."'
```

Observou-se também que não existe qualquer comando de sanitização de input, o que possibilita a inserção de caracteres especiais que permitam a realização deste ataque. 
Sabendo que o objetivo é conseguir obter acesso ao website enquanto administrador, assumiu-se que o username do mesmo seja "admin", tal como foi feito no logbook de sql injection. Sabendo-se apenas o username, já é possível a query devolver o user pretendido, simplesmente, de acordo com o comando, ainda seria necessária a palavra passe para a concretização da query, pelo que é esse passo que se procurou evitar. Analisando-se o restante código do ficheiro index foi também possível concluir, pelo último segmento de html, que o preenchimento da caixa de texto correspondente à password é obrigatório.

```html
<input type = "password" class = "form-control"
   name = "password" placeholder = "password" required></br>

```

Posto isto, procedeu-se à construção da string maliciosa. Primeiramente escreveu-se *admin*, para a query poder encontrar o user. Posteriormente, inseriu-se uma plica (*admin'*), de modo a fechar a string possibilitando a escrita de código em sql. Para terminar, sabendo que através do ficheiro index.php foi possível concluir que a versão de sql utilizada foi SQLite e que, nesta versão, um comentário no código é iniciado com "--" , inseriu-se este segmento de modo a descartar todo o restante código remetente à password. Assim a string utilizada foi a seguinte:
**admin'--**
De modo a realizar o ataque inseriu-se esta string no campo de username e sabendo que a palavra passe é "required", inseriu-se uma string aleatória de modo a que esse campo não ficasse vazio (no caso, "a")
Desta forma foi possível obter acesso ao website enquanto administrador e recolher a flag.
