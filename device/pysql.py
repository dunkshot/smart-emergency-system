import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='rds...ap-northeast-2.rds.amazonaws.com',
                            user='user????',
                            password='password????',
                            db='database????',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

f = open('output.txt', 'r')
lines = f.readlines()
for line in lines:
    rr=str.split(line)
    print (rr)
    print (rr[0])
    print (rr[1])
caseID = case00001
#i=rr.index('맥박')  #'맥박'검색 > 배열 번호 i에 저장

if '혈압' in rr:
    cursor.execute("UPDATE state SET pressure = %s WHERE caseID = %s ;", rr[rr.index('혈압')+1], caseID)
    print("UPDATE 혈압")

if '맥박' in rr:
    cursor.execute("UPDATE state SET heartrate = %s WHERE caseID = %s ;", rr[rr.index('맥박')+1], caseID)
    print("UPDATE 맥박")

if '체온' in rr:
    cursor.execute("UPDATE state SET temperature = %s WHERE caseID = %s ;", rr[rr.index('체온')+1], caseID)
    print("UPDATE 체온")

if '이름' in rr:
    cursor.execute("UPDATE patient SET P_name = %s WHERE caseID = %s ;", rr[rr.index('이름')+1], caseID)
    print("UPDATE 이름")

if '증상' in rr:
    cursor.execute("UPDATE state SET symptom = %s WHERE caseID = %s ;", rr[rr.index('증상')+1], caseID)
    print("UPDATE 증상")

if '산소포화도' in rr:
    cursor.execute("UPDATE state SET oxygen = %s WHERE caseID = %s ;", rr[rr.index('산소포화도')+1], caseID)
    print("UPDATE 산소포화도")


#c.execute("insert into project values(%s,%s,%s)") %(a,b,c)
connection.commit()
connection.close()