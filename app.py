from flask import Flask, render_template, request, send_from_directory
import triangle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    classification = ''
    if request.method == 'POST':
        tipo = request.form.get('tipo')
        valor1 = float(request.form.get('valor1'))
        valor2 = float(request.form.get('valor2'))
        valor3 = float(request.form.get('valor3'))

        if tipo == 'lado':
            if triangle.validate_sides(valor1, valor2, valor3):
                classification = triangle.classify_by_sides(valor1, valor2, valor3)
                triangle.create_triangle_image_by_sides(valor1, valor2, valor3)
                return render_template('index.html', classification=classification, image='triangle.png')
            else:
                return render_template('index.html', error='Valores de lado não formam um triângulo válido!')
        else:
            if triangle.validate_angles(valor1, valor2, valor3):
                classification = triangle.classify_by_angles(valor1, valor2, valor3)
                triangle.create_triangle_image_by_angles(valor1, valor2, valor3)
                return render_template('index.html', classification=classification, image='triangle.png')
            else:
                return render_template('index.html', error='Valores de ângulo não formam um triângulo válido!')
        
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_image(filename):
    return send_from_directory('static', filename)