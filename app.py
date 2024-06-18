from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def pag_inicial():
    return render_template('index.html')

@app.route('/pag_2')
def pag_2():
    return render_template('pag_2.html')

@app.route('/ir_para_pag_2')
def ir_para_pag_2():
    return redirect(url_for('pag_2'))

if __name__ == '__main__':
    app.run(debug=True)

from flask import session

class Carrinho:
    def __init__(self):
        self.carrinho = session.get('carrinho', {})

    def adicionar_item(self, produto_id, quantidade):
        if produto_id not in self.carrinho:
            self.carrinho[produto_id] = 0
        self.carrinho[produto_id] += quantidade
        session['carrinho'] = self.carrinho

    def remover_item(self, produto_id):
        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            session['carrinho'] = self.carrinho

    def obter_itens(self):
        return self.carrinho.items()

    def obter_total(self):
        total = 0
        for produto_id, quantidade in self.carrinho.items():
            preco = obter_preco(produto_id)
            total += preco * quantidade
        return total

    def limpar_carrinho(self):
        self.carrinho = {}
        session['carrinho'] = self.carrinho
