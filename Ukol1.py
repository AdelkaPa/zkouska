from flask import Flask, request

Ukol1 = Flask('muj-server')


@Ukol1.route("/todo", methods=['GET', 'DELETE', 'POST'])
def todo():
    mista = {
        'Place1': 'Paris',
        'Place2': 'Edinburgh',
        'Place3': 'Budapest',
        'Place4': 'London',
        'Place5': 'Vaduz',
        'Place6': 'Reykjavik',
    }
   #if request.method == 'GET':


   # pozadovane_misto = str(request.args[])
    print(request)
    return mista
       # pozadovane_startovni_cislo = int(request.args['startovni_cislo'])
    #skore = ucastnici[pozadovane_startovni_cislo]
    #return f"skore ucastnika {pozadovane_startovni_cislo} je {skore}"

if __name__ == "__main__":
    Ukol1.run()