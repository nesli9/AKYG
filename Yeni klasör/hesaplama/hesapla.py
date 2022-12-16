from flask import Flask, render_template, request

Flask_App = Flask(__name__) 

@Flask_App.route('/', methods=['GET'])
def index():
    

    return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():
    

    error = None
    result = None

    
    first_input = request.form['Giris1']  
    second_input = request.form['Giris2']
    operation = request.form['islem']

    try:
        input1 = float(first_input)
        input2 = float(second_input)

        
        if operation == "+":
            result = input1 + input2

        elif operation == "-":
            result = input1 - input2

        elif operation == "/":
            result = input1 / input2 

        elif operation == "*":
            result = input1 * input2

        else:
            operation = "%"
            result = input1 % input2

        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result=result,
            calculation_success=True
        )
        
    except ZeroDivisionError:
        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result="yanlış giriş",
            calculation_success=False,
            error="Sıfırı bölemezsiniz"
        )
        
    except ValueError:
        return render_template(
            'index.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result="yanlış giriş",
            calculation_success=False,
            error="Hata"
        )

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()
