from flask import Flask, render_template, request


app = Flask(__name__)


# Rota responsável em chamar a pagina inicial
@app.route("/")
def index():
    return render_template("pg_calcular.html")

    
# Função responsável pela captação dos números digitados, e conversão de bases para validar se o número
# está entre 0-255 conforme enunciado.
@app.route("/rt_calcular", methods=['GET', 'POST'])
def f_calcular():
    # If responsável por salvar os valores digitados nas variáveis, e conversão para binário para validação.
    if (request.method == "POST"):
        recebe_primeiro = request.form["primeiro"]
        primeiro_bin = int(recebe_primeiro, 2)
        print(primeiro_bin)

        tipoOperacao=(request.form["operacao"])
        
        recebe_segundo = request.form["segundo"]
        segundo_bin = int(recebe_segundo, 2)
        print(segundo_bin)

        # If responsável pela validação se o valor digitado está entre 0-255 conforme enunciado.
        if (primeiro_bin <= 255):
            valor_um = primeiro_bin

            if (segundo_bin <= 255):
                valor_dois = segundo_bin

                # If responsável por verificar o valor da variável que carrega o botão da calculadora
                # e executa a operação matemática de acordo com o botão selecionado.
                if (tipoOperacao == "Somar"):
                    resultado_decimal = (primeiro_bin + segundo_bin)
                    resultado_binario = bin(valor_um + valor_dois)
                    resultado_final = (resultado_binario[2:])

                if (tipoOperacao == "Subtrair"):
                    resultado_decimal = (primeiro_bin - segundo_bin)
                    resultado_binario = bin(valor_um - valor_dois)
                    resultado_final = (resultado_binario[2:])

                if (tipoOperacao == "Multiplicar"):
                    resultado_decimal = (primeiro_bin * segundo_bin)
                    resultado_binario = bin(valor_um * valor_dois)
                    resultado_final = (resultado_binario[2:])

                if (tipoOperacao == "Dividir"):
                    resultado_decimal = (primeiro_bin // segundo_bin)
                    resultado_binario = bin(valor_um // valor_dois)
                    resultado_final = (resultado_binario[2:])

                if (tipoOperacao == "Resto Divisao"):
                    resultado_decimal = (primeiro_bin % segundo_bin)
                    resultado_binario = bin(valor_um % valor_dois)
                    resultado_final = (resultado_binario[2:]) 

                return render_template ("pg_calcular.html", resultado2=resultado_final, resultado10=resultado_decimal)

            # Else responsável por notificar o usuário caso o valor seja maior que 255 conforme enunciado
            else:
                error1 = ("Deve-se utilizar números entre 0 e 255")
                return render_template ("pg_calcular.html", error1 = error1)
        else:
            error2 = ("Deve-se utilizar números entre 0 e 255")
            return render_template ("pg_calcular.html", error2 = error2)


if __name__ == '__main__':
    app.run(debug=True)
