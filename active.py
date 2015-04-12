import MySQLdb
import csv
mydb = MySQLdb.connect(host='localhost', user='root', passwd='mysql', db='gainsight')
cursor = mydb.cursor()
days = cursor.execute("select distinct(day) from TrendingProducts ")
days = cursor.fetchall()
hour = cursor.execute("select distinct(hour) from TrendingProducts")
hour = cursor.fetchall()
user = cursor.execute("select timestamp,activeUsers from UsersTracking order by timestamp DESC limit 30")
user = cursor.fetchall()
with open('active.csv','w') as fp:
    for i in user:
        a= csv.writer(fp, delimiter=',')
        a.writerow([i[0],i[1]])
  





