import unittest

import requests


class ApiTest(unittest.TestCase):
    API_URL="http://127.0.0.1:5000"

    def test_get_welcome_msg(self):
        WElCOME_URL="{}/welcome".format(self.API_URL)
        r=requests.get(WElCOME_URL)
        self.assertEqual(r.status_code,200)
        data=r.content.decode('utf-8')
        self.assertEqual(data,"Welcome to Pizza House")
        
        


    def test_take_order(self):
        ORDER_OBJ={"order":["pizza1"]}
        ORDER_URL="{}/order".format(self.API_URL)
        r=requests.post(ORDER_URL,json=ORDER_OBJ)
        self.assertEqual(r.status_code,201)



    def test_getAllOrders(self):
        getAll_URL="{}/getorders".format(self.API_URL)
        r=requests.get(getAll_URL)
        self.assertEqual(r.status_code,200)
        

#         output=[
#     {
#         "_id": {
#             "$oid": "6347aa91dc14f7d70f90bb58"
#         },
#         "order": [
#             "Pizza1",
#             "Pizza2"
#         ]
#     },
#     {
#         "_id": {
#             "$oid": "6347aaf7dc14f7d70f90bb59"
#         },
#         "order": [
#             "Pizza1",
#             "Pizza2",
#             "pizza3"
#         ]
#     },
#     {
#         "_id": {
#             "$oid": "6347c165f436443ae9668dba"
#         },
#         "order": [
#             "pizza1"
#         ]
#     },
#     {
#         "_id": {
#             "$oid": "6347c184f436443ae9668dbb"
#         },
#         "order": [
#             "pizza1"
#         ]
#     }
# ]
#         self.assertEqual(r.json(),output)




    def test_get_order_by_id(self):  
        GET_BY_ID_URL = "{}/getorders/{}".format(self.API_URL,"6347aa91dc14f7d70f90bb58")
        r=requests.get(GET_BY_ID_URL)
        self.assertEqual(r.status_code,200)
        order={'order': ['Pizza1', 'Pizza2']}
        self.assertEqual(order,r.json())

        
if __name__=="__main__":
    unittest.main()

