from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledText

text_content = '''
首要说明:
    此脚本主要是拿来跑几百关的开荒的，日活只是充话费送的赠品(如果你发现日活的逻辑很蠢，而且时不时会出错，不用怀疑，就是很蠢)
    此脚本是基于模拟器的,DMMPlayer端、手机端、网页端请绕行
    (理论上只要能连上adb，什么模拟器都行，不过写的时候是基于MuMu模拟器12)
必要的设置！必要的设置！必要的设置!:
    首先你需要将adb端口和adb路径设置为你自己的，否则无法正确连接
        adb端口一般默认16384，你可以通过点击模拟器的'三条杠'按钮,然后再点'问题诊断'来查看
        adb路径在你模拟器路径下，你可以参考脚本默认的路径设置来寻找自己的路径位置
    其次你需要设置你的模拟器分辨率为1280x720分辨率(设置->其他)，并开启后台挂机时保活运行(设置->其他)
    
基本使用说明:
    主线开荒、星月塔开荒->点击即可
        会以自动战斗模式，使用你当前的队伍进行战斗（请注意在进入战斗的页面提前选择好你的队伍！！！）
        战斗输了会自动退出脚本
        如果你没有选择开启自动补充体力，在体力耗尽后也会退出
    日常任务部分,你需要自己选择想要完成的内容，然后点击按钮。
        其中'主线任务选项'只会自动跑一次你所GOD打过的,最新的主线normal难度关卡
        其余内容会自动跑完你所有剩余的次数（例如两次技能关卡）
    通用开荒部分
        如字面意思:
            如果是类似主线这种打星星的模式可以使用通用体力型开荒
            如果是类似新月塔的模式，可以使用通用塔型开荒
        注意！
            因为这两个通用开荒没写进入页面部分，请自行进入相应开荒页面
                体力型的开荒页面是你能看到已完成和未完成星星的页面
                塔型的开荒页面是有个准备出击按钮的页面

一些已知问题:
    因为我自动打不到最后一关，所以不知道开荒结束之后的页面长什么样，所以没写开荒完毕的退出
        ps:理论上设置了识别失败次数过多会自动退出，所以应该也是会自动退出的
    图像识别受到分辨率、亮度等等的影响，如果你无法正常执行脚本，请先尝试修改识别精度，仍然无法正常执行的话只能放弃使用此脚本了
        在这种情况下，你也可以试试另一位写的脚本，项目地址:https://github.com/zhtoatao/Shiny_Thursday_Scrip/tree/a16ee4e705be68a472e7fbcd10ca8b89b5365b4a
    非正常运行我尽可能写了，但也不能面面俱到，对于一些非常见的问题我并没有写
        例如:开启了自动回复体力，但是(没药+钻不够/钻的回复次数到达了上限)，会导致脚本卡住（因为正常识别到了，只是无法点击）
        再比如:你没有配队就开始跑脚本了 
'''

def get_frame(notebook):

    global text_content

    frame = ttk.Frame(notebook)

    scrolled_text = ScrolledText(frame,padding=10,autohide=True)
    scrolled_text.pack(fill= BOTH, expand=True)
    scrolled_text.insert(END, text_content)

    return frame

