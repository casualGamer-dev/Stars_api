from flask import Flask, request, jsonify
from planet import final_planet_list

app=Flask(__name__)
@app.route('/')
def index():
    return jsonify({
        'data': final_planet_list,
        'status':'success'
    }), 200
@app.route("/planet")
def planet():
    name=request.args.get('name')
    planet_data=next(item for item in final_planet_list if item['name']==name)
    return jsonify({
        'data': planet_data,
        'status':'success'
    }), 200
if __name__ == '__main__':
    app.run()    