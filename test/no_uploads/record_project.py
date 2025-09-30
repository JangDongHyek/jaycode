import jaycode
from datetime import datetime

def normalize_path(path: str) -> str:
    """경로가 './'로 시작하면 제거"""
    if path.startswith("./"):
        return path[2:]
    return path

gasan = jaycode.init()
crm = jaycode.init()

gasan.SSH.connect(hostname='gasan.sm-tmcall.kr',port=22,username='root',password='vhtmzh12')
exit()
crm.SSH.connect("crm-dev.inp.kr","root","xptmxm12")
crm.DB.connect("root","xptmxm12","test_jdh")

# 데이터 조회
rows = crm.DB.query("select * from receive_history")

# ssh로 녹취파일 가져오기
row = rows[0]
record_path = '/home/gasan-dev/www/' + normalize_path(row['record_path'])
file_name = f"{row['seq']}_녹음파일"
save_path = gasan.SSH.get_file(remote_path=record_path,name=file_name)
row['get_file'] = "true"
crm.DB.update(rows[0],"receive_history")

# 녹취파일 wav파일로 변환 및 파일명 설정
dt = row['record_date'].strftime("%Y%m%d%H%M%S")
crm.File.m4a_to_wav(save_path,
        f"{dt}_{row['user_id']}_{row['user_id']}_pt값_{row['customer_name']}_{row['customer_code']}_{row['customer_phone']}_내선.wav")
row['conversion'] = "true"
crm.DB.update(rows[0],"receive_history")

#전송로직 * 전송후 가져온파일 및 변환파일은 삭제처리되게