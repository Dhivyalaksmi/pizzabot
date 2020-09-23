from flask import jsonify


def generateResponse(data, msg):
    response_data = {}
    data_list = []
    try:
        for i in data:
            temp = {}
            temp["orderid"] = i[0]
            temp["typeofpizza"] = i[1]
            temp["pizzaname"] = i[2]
            temp["toppings"] = i[3]
            temp["nameofcustomer"] = i[4]
            temp["mobileno"] = i[5]
            temp["address"] = i[6]
            temp["orderstatus"] = i[7]
            temp["orderedtime"] = i[8]
            data_list.append(temp)
            response_data["data"] = data_list

        response_data["msg"] = msg
        print(f"Respone data : {response_data}")
        return jsonify(response_data)
    except IndexError as e:
        print(e)
        return str(e)
