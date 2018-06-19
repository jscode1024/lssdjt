from flask_wtf import FlaskForm
from wtforms import TextField,SubmitField
class LssdjtForm(FlaskForm):
    lssdjt=TextField(
        label="历史上的今天",
        description='历史上的今天',
        render_kw={
            "class":"form-control",
            "placeholder":"请输入你想要查看的日期!",
            "id":"txtBeginDate"
        }

    )

class QqsmForm(FlaskForm):
    qqtext=TextField(
        label="输入QQ号",
        description="输入QQ号",
        render_kw={
            "class":"cmint",
            "placeholder":"请输入QQ号",
            "size":15,
            "class":"cmint",
            "maxlength":11
        }
    )
    qqsubmit=SubmitField(
        label="开始测试",
        description="开始测试",
        render_kw={
            "class":"zbbtn2"
        }
    )