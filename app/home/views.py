from flask import render_template,jsonify,redirect,url_for
from flask import request
from . import home
from urllib import parse
from urllib import request as reque
import json
from app.home.forms import LssdjtForm,QqsmForm
# from app.modles import Qqnums
# from app import db
def req_lssdjt_data(date=""):
    showapi_appid="37525"  #替换此值
    showapi_sign="ce83d29cc82d45858a267c80388a028e"   #替换此值
    url="http://route.showapi.com/119-42"
    send_data = parse.urlencode([
    ('showapi_appid', showapi_appid)
    ,('showapi_sign', showapi_sign)
        ,('date', date)

    ])

    req = reque.Request(url)
    try:
        response = reque.urlopen(req, data=send_data.encode('utf-8'), timeout = 10) # 10秒超时反馈
    except Exception as e:
        print(e)
    result = response.read().decode('utf-8')
    result_json = json.loads(result)
    if not result_json:
        return ''
    return result_json['showapi_res_body']['list']

def req_english_sentence():
    showapi_appid="55092"  #替换此值
    showapi_sign="d34df287c5fa4e3ba5d00d8964fa60ed"   #替换此值
    url="http://route.showapi.com/1211-1"
    send_data = parse.urlencode([
    ('showapi_appid', showapi_appid)
    ,('showapi_sign', showapi_sign)
        ,('count', "1")

    ])

    req = reque.Request(url)
    try:
        response = reque.urlopen(req, data=send_data.encode('utf-8'), timeout = 10) # 10秒超时反馈
    except Exception as e:
        print(e)
    result = response.read().decode('utf-8')
    result_json = json.loads(result)
    if not result_json:
        return ''
    return result_json['showapi_res_body']['data'][0]['english']

def req_qqcjx_data(qq=""):
    showapi_appid="55843"  #替换此值
    showapi_sign="2aaf332e150a4fc5ba236443166e19d0"   #替换此值
    url="http://route.showapi.com/863-1"
    send_data = parse.urlencode([
    ('showapi_appid', showapi_appid)
    ,('showapi_sign', showapi_sign)
        ,('qq', qq)

    ])

    req = reque.Request(url)
    try:
        response = reque.urlopen(req, data=send_data.encode('utf-8'), timeout = 10) # 10秒超时反馈
    except Exception as e:
        print(e)
    result = response.read().decode('utf-8')
    result_json = json.loads(result)
    if not result_json:
        return ''
    reuslt_dict={'desc':result_json['showapi_res_body']['desc'],'score':result_json['showapi_res_body']['score'],'grade':result_json['showapi_res_body']['grade'],'analysis':result_json['showapi_res_body']['analysis']}
    return reuslt_dict

def req_duanzi_data(page=''):
    showapi_appid="55056"  #替换此值
    showapi_sign="cb1abca0e38841ad964bf3d39e6402d1"   #替换此值
    url="http://route.showapi.com/341-1"
    send_data = parse.urlencode([
    ('showapi_appid', showapi_appid)
    ,('showapi_sign', showapi_sign)
        ,('page', page)
        ,('maxResult', "")

    ])

    req = reque.Request(url)
    try:
        response = reque.urlopen(req, data=send_data.encode('utf-8'), timeout = 10) # 10秒超时反馈
    except Exception as e:
        print(e)
    result = response.read().decode('utf-8')
    result_json = json.loads(result)
    if not result_json:
        return ''
    reuslt_dict={'allPages':result_json['showapi_res_body']['allPages'],'contentlist':result_json['showapi_res_body']['contentlist']}
    return reuslt_dict

@home.route('/')
def home_index():
    result=req_english_sentence()
    return render_template('home/index.html',result=result)

@home.route('/lssdjt/',methods=['GET'])
def home_lssdjt():
    form=LssdjtForm()
    result=req_lssdjt_data()
    month=result[0]['month']
    day=result[0]['day']
    return render_template('home/lssdjt.html',result=result,month=month,day=day,form=form)

@home.route('/lssdjt/api/<date>',methods=['POST'])
def api_lssdjt(date=""):
    result=req_lssdjt_data(date)
    return jsonify({'list':result})

@home.route('/lssdjt/<date>/',methods=['GET'])
def home_lssdjt_date(date):
    form=LssdjtForm()
    result=req_lssdjt_data(date)
    month=result[0]['month']
    day=result[0]['day']
    return render_template('home/lssdjt.html',result=result,month=month,day=day,form=form)


@home.route('/duanzi/list',methods=['GET'])
def home_duanzi():
    slogan=req_english_sentence()
    # 分页链接会自动添加p这个参数，表示页码
    page = request.args.get('p', '1')
    if not page:
        page = 1
    limit = 20
    result=req_duanzi_data(str(page))
    query = request.args.get('query', '')
    total=result['allPages']
    pager = {'total': int(total), 'limit':int(limit), 'curr_page': int(page)}
    return render_template('home/duanzi.html',result=result['contentlist'],slogan=slogan,query=query, p=pager)

@home.route('/qqsm/<qqnum>/',methods=['GET','POST'])
def home_qqsm(qqnum="none"):
    result=""
    form=QqsmForm()
    slogan=req_english_sentence()
    if request.method == 'POST':
        data=form.data
        # tag=Qqnums.query.filter_by(qqnum=data["qqtext"]).count()
        # if tag==1:
        #     return redirect(url_for("home.home_qqsm",qqnum=data["qqtext"]))
        # qq=Qqnums(data["qqtext"])
        # db.session.add(qq)
        # db.session.commit()
        return redirect(url_for("home.home_qqsm",qqnum=data["qqtext"]))
    if qqnum != 'none':
        result=req_qqcjx_data(str(qqnum))
    return render_template('home/qqsuanming.html',slogan=slogan,form=form,result=result,qqnum=qqnum)
'''
@home.route('/qqsm/<int:qqnum>/',methods=['GET','POST'])
def home_qqsmh(qqnum):
    form=QqsmForm()
    slogan=req_english_sentence()
    result=req_qqcjx_data(str(qqnum))
    return render_template('home/qqsm_jieguo.html',result=result,form=form,slogan=slogan,qqnum=qqnum)

    '''

    