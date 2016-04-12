#coding:utf-8
#author:leafrainy (http://blog.gt520.com)
#version:0.1
#time:2016-04-11

from flask import Flask,render_template,request,abort, redirect
import sqlite3
import time

app = Flask(__name__)

#首页
@app.route('/')
def app_index():
	#配置标题
	config ={"title":"Leafrainy's Todolist"}
	#待办列表
	todo_list_sql = "select * from things where status=0 order by id desc"
	todo_list_data = M(todo_list_sql,1)

	#完成列表最近10条
	todo_ok_sql = "select * from things where status=1 order by changetime desc limit 10"
	todo_ok_data = M(todo_ok_sql,1)

	return render_template("index.html",todo_list_data=todo_list_data,todo_ok_data=todo_ok_data,config=config)


#添加
@app.route('/add',methods=['POST'])
def add_thing():
	userid = 1
	thing = request.args.get("thing")
	if thing :
		addtime = int(time.time())
		add_sql = "insert into things (userid,thing,addtime) values ("+str(userid)+",'"+thing+"',"+str(addtime)+")"
		M(add_sql,0)
		return "1"
	else:
		return "0"

#修改状态
@app.route('/update',methods=['POST'])
def update():
	id = request.args.get("id")
	status = request.args.get("status")
	changetime = int(time.time())

	if status == "1":
		return "0"
	else:
		status = 1

	update_sql = "update things set status="+str(status)+",changetime="+str(changetime)+" where id="+str(id)
	M(update_sql,0)
	return "1"

#封装数据库方法
def M(sql,have_return):
	conn = sqlite3.connect('todo.db')
	cursor = conn.cursor()
	if have_return == 1:
		conn.row_factory = sqlite3.Row
		cursor.execute(sql)
		things = []
		thing = {}
		for row in cursor:
			things.append({'id':row[0],'userid':row[1],'thing':row[2],'addtime':time.strftime("%m-%d %H:%M:%S",time.localtime(row[3])),'changetime':time.strftime("%m-%d %H:%M:%S",time.localtime(row[4])),'status':row[5]})
	else:
		cursor.execute(sql)
	conn.commit()
	cursor.close()
	conn.close()
	if have_return == 1:
		return things
 
#错误处理
@app.errorhandler(404)
def erro_404(e):
	return "404了喵~"

@app.errorhandler(405)
def erro_405(e):
	return "405,what are u 弄啥来，喵~"

if __name__ == '__main__':
	#app.debug = True
	app.run(host='0.0.0.0', port='80')