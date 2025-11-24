from flask import jsonify, request
from flask_restx import Namespace, Resource, reqparse
from .. import db
import time

routes_ns = Namespace('Proxy Client', description='this is the api provided to your client, get the api_key at Manager in each proxy port')
parser = reqparse.RequestParser()
parser.add_argument('api_key', type=str, required=True, help='API key in edit or add proxy port')

@routes_ns.route('/proxy-info')
class proxy_info(Resource):
    @routes_ns.expect(parser)
    def get(self):
        api_key = request.args.get('api_key')
        host = request.host  # Lấy host (VD: asdsad.com:80 hoặc 192.168.1.10:5000)
        # base_url = request.base_url  # URL đầy đủ đến endpoint
        # url_root = request.url_root  # Gốc domain (gồm cả http:// hoặc https://)
        # print(host,base_url,url_root)
        
        # if api_key and len(api_key)<100 and len(api_key.strip())>0:
        #     find_key = ProxyManager.query.filter(ProxyManager.status!="stop").filter_by(api_key=api_key).first()
        #     if find_key:
        #         result = {"success":"ok","status":find_key.status,"proxys":{}}
        #         auth = ""
        #         if find_key.user and find_key.password:
        #             auth = f":{find_key.user}:{find_key.password}"
        #         if find_key.type_proxy == "http_socks":
        #             http_p,socks_p = find_key.port.split(",")
        #             result["proxys"]["http"] = f"{host}:{http_p}{auth}"
        #             result["proxys"]["socks"] = f"{host}:{socks_p}{auth}"
        #         else:
        #             result["proxys"][find_key.type_proxy] = f"{host}:{find_key.port}{auth}"
        #         if find_key.timestamp_min_change_ip_api:
        #             time_restart = find_key.timestamp_min_change_ip_api - int(time.time())
        #             if time_restart <= 0:
        #                 time_restart = 0
        #         else:
        #             time_restart = 0
        #         result["time_restart"] = time_restart
        #         return result,200
        
        return {"error":"validate error value"},500
