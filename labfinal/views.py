from django.shortcuts import render
import pandas as pd

# Create your views here.
def home(request):

    if request.method == "GET":
        return render(request, 'labfinal/index.html')

    elif request.method == "POST":
        code = request.POST['u-code']

        operators = {'=': 'Assignment op', '+': 'Addition op', '-': 'Subtraction op', '/': 'Division op',
                     '*': 'Multiplication op', '<': 'Lessthan op', '>': 'Greaterthan op', '(':'Other 1',')':'Other 2','{':'Other 3','}':'Other 4'}
        operators_key = list(operators.keys())

        data_type = {'int': 'integer type', 'float': 'Floating point', 'if' : 'Compare' , 'char': 'Character type', 'long': 'long int', 'print':'Other 5'}
        data_type_key = list(data_type.keys())

        punctuation_symbol = {':': 'colon', ';': 'semi-colon', '.': 'dot', ',': 'comma'}
        punctuation_symbol_key = list(punctuation_symbol.keys())

        identifier = {'a': 'id_1', 'b': 'id_2', 'c': 'id_3', 'd': 'id_4','d': 'id_5'}
        identifier_key = list(identifier.keys())

        count = 0
        program = code.split("\n")
        s_name = []
        token_type = []
        value = []
        symbol_id = []


        for line in program:
            count = count + 1
            tokens = line.split(' ')

            for token in tokens:
                if token in operators_key:
                    s_name.append(token)
                    token_type.append(token)
                    symbol_id.append(operators[token])
                    value.append("-")

                if token in data_type_key:
                    # value1 = data_type_key.index(token)
                    s_name.append(token)
                    token_type.append(token)
                    symbol_id.append(data_type[token])
                    value.append("-")
                    # token_type.append(data_type[value1])

                if token in punctuation_symbol_key:
                    # value2 = punctuation_symbol_key.index(token)
                    s_name.append(token)
                    token_type.append("other")
                    symbol_id.append(punctuation_symbol[token])
                    value.append("-")


                if token in identifier_key:
                    # value3 = identifier_key.index(token)
                    s_name.append(token)
                    token_type.append("id")
                    symbol_id.append(identifier[token])
                    value.append("-")


                if token.isdigit():
                    s_name.append(token)
                    token_type.append("number")
                    symbol_id.append("Value")
                    value.append(token)





        df = pd.DataFrame(list(zip(s_name,symbol_id,token_type,value)),
                          columns=['Symbol Name', 'Symbol Id','Token type','Value'])
        print(df)
        #

        # df.to_csv("output.csv")
        context = {
            'code_new' : df
        }
        return render(request, 'labfinal/table.html', context)

        ##########################