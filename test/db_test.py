import jaycode

crm = jaycode.init()
crm.SSH.connect("crm-dev.inp.kr","root","xptmxm12")
crm.DB.connect("root","xptmxm12","test_jdh")

row = {
    "center" : "테스트",
    "user_name" : "tt"
}

crm.DB.insert(row,"receive_history")