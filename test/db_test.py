import jaycode

crm = jaycode.init()
crm.SSH.connect("crm-dev.inp.kr","root","xptmxm12")
crm.DB.connect("root","xptmxm12","test_jdh")

row = {
    "seq" : 7,
    "table" : "receive_history"
}

crm.DB.delete(row)