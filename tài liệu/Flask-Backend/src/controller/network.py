from flask import Blueprint, request, jsonify
from ..models import Ddns
from .. import db
from src.utils.ddns import ddnsDynu

routes = Blueprint('network', __name__)

@routes.route('/ddns', methods=['POST',"GET"])
def ddnsSetting():
    method = request.method
    if method == "GET":
        all_DDNS = ["noip.com","dynu.com","duckdns.org"]
        for name in all_DDNS:
            is_iface = Ddns.query.filter_by(name=name)
            if is_iface.first() is None:
                new_user = Ddns(**{"name":name})
                db.session.add(new_user)
                db.session.commit()
        find_id = request.args.get("id")
        if find_id is None:
            data = Ddns.query.all()
        else:
            data = Ddns.query.filter_by(id=find_id).first()
        if data is None:
            return jsonify({"error": "Invalid id"}), 404
        return jsonify({"success": "get data success", "data": data}), 200

    if method == "POST":
        newdata = request.json
        data_find = Ddns.query.filter_by(id=newdata.get("id"))
        first_ = data_find.first()
        if first_:
            data_find.update(newdata)
            isError = None
            if newdata.get("status") == True:
                for item in ["1.1.1.1",None]:
                    resp = ddnsDynu(first_).update_ip(item)
                    if resp is None or "bad" in resp.text:
                        isError = True
            if isError:
                return jsonify({"error": "authen failed"}), 500
            else:
                db.session.commit()
        return jsonify({"success": "update ddns setting success"}), 200