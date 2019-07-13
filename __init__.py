import os
import re
import json
import cudatext as app
from cudax_nodejs import run_node
from cuda_fmt import get_config_filename

tool_js = os.path.join(os.path.dirname(__file__), 'autoprefixer.js')

def do_format_ex(text, is_css):

    fn = get_config_filename('CSS AutoPrefixer')
    s = open(fn, 'r').read()
    #del // comments
    s = re.sub(r'(^|[^:])//.*'  , r'\1', s)   
    opt = json.loads(s)
    opt['is_css'] = is_css
    opt = json.dumps(opt)        
    
    try:
        return run_node(text, [tool_js, opt])
    except Exception as e:
        app.msg_box('Error while running Node.js \n'+str(e), app.MB_OK+app.MB_ICONERROR)

def do_format_css(text):
    
    return do_format_ex(text, True)

def do_format_scss(text):
    
    return do_format_ex(text, False)
