from urllib.parse import unquote as urldecode
import re

def parse_url(string):
    url_encod_characters = ['%08', '%09', '%0A', '%0D', '%20', '%21', '%22', '%23', '%24', '%25', '%26',
                            '%27', '%28', '%29', '%2A', '%2B', '%2C', '%2D', '%2E', '%2F', '%30', '%31', '%32', '%33',
                            '%34', '%35', '%36', '%37', '%38', '%39', '%3A', '%3B', '%3C', '%3D', '%3E', '%3F', '%40',
                            '%41',
                            '%42', '%43', '%44', '%45', '%46', '%47', '%48', '%49', '%4A', '%4B', '%4C', '%4D', '%4E',
                            '%4F',
                            '%50', '%51', '%52', '%53', '%54', '%55', '%56', '%57', '%58', '%59', '%5A', '%5B', '%5C',
                            '%5D', '%5E',
                            '%5F', '%60', '%61', '%62', '%63', '%64', '%65', '%66', '%67', '%68', '%69', '%6A', '%6B',
                            '%6C', '%6D',
                            '%6E', '%6F', '%70', '%71', '%72', '%73', '%74', '%75', '%76', '%77', '%78', '%79', '%7A',
                            '%7B', '%7C',
                            '%7D', '%7E', '%A2', '%A3', '%A5', '%A6', '%A7', '%AB', '%AC', '%AD', '%B0', '%B1', '%B2',
                            '%B4', '%B5', '%BB', '%BC',
                            '%BD', '%BF', '%C0', '%C1', '%C2', '%C3', '%C4', '%C5', '%C6', '%C7', '%C8', '%C9', '%CA',
                            '%CB', '%CC', '%CD', '%CE', '%CF',
                            '%D0', '%D1', '%D2', '%D3', '%D4', '%D5', '%D6', '%D8', '%D9', '%DA', '%DB', '%DC', '%DD',
                            '%DE', '%DF', '%E0', '%E1', '%E2',
                            '%E3', '%E4', '%E5', '%E6', '%E7', '%E8', '%E9', '%EA', '%EB', '%EC', '%ED', '%EE', '%EF',
                            '%F0', '%F1', '%F2', '%F3', '%F4',
                            '%F5', '%F6', '%F7', '%F8', '%F9', '%FA', '%FB', '%FC', '%FD', '%FE', '%FF']
    ptr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.', '_', '~', ':', '/', '?', '#', '[', ']', '@', '!',
           '$', '&', '(', ')', '*', '+', ',', ';', '=']
    global attr
    methods = (
        'getElementsByTagName', 'write', 'getElementById', 'alert', 'prompt', 'eval', 'fromCharCode', 'fetch',
        'confirm')

    tags = ['frame', 'form', 'div', 'style', 'video', 'img', 'input', 'textarea', 'iframe', 'script', 'meta', 'applet',
            'object', 'embed', 'link', 'svg']
    attrs = ['href', 'archive', 'http-equiv', 'lowsrc', 'content', 'data', 'data-*', 'dir', 'download', 'form',
             'formaction', 'method', 'dir', 'accept', 'onsubmit', 'poster', 'src', 'background', 'bgcolor', 'content',
             'min',
             'action', 'autofocus', 'id', 'class', 'codebase', 'novalidate', 'srcset', 'required', 'target',
             'pattern''cite', 'classid', 'profile', 'charset', 'style', 'list', 'manifest', ]
    eventHandlersAttrs = ['onbeforedeactivate', 'onbeforeeditfocus', 'onbeforepaste', 'onbeforeprint', 'onabort',
                          'onactivate', 'onafterprint',
                          'onafterupdate', 'onbeforeactivate', 'onbeforecopy', 'onbeforecut', 'onchange', 'onclick',
                          'oncontextmenu', 'oncontrolselect', 'oncopy',
                          'onbeforeunload', 'onbeforeupdate', 'onblur', 'onbounce', 'oncellchange', 'ondragleave',
                          'ondragover', 'ondragstart', 'ondrop', 'onerror',
                          'oncut', 'ondataavailable', 'ondatasetchanged', 'ondatasetcomplete', 'ondblclick',
                          'ondeactivate',
                          'ondrag', 'ondragend', 'ondragenter',
                          'onmousedown', 'onmouseenter', 'onmouseleave', 'onmousemove', 'onmouseout', 'onerrorupdate',
                          'onfilterchange', 'onfinish', 'onfocus', 'onfocusin',
                          'onreadystatechange', 'onreset', 'onresize', 'onresizeend', 'onresizestart', 'onfocusout',
                          'onhashchange', 'onhelp', 'oninput', 'onkeydown',
                          'onkeypress', 'onkeyup', 'onload', 'onlosecapture', 'onmessage', 'onsearch', 'onselect',
                          'onselectionchange', 'onselectstart', 'onstart',
                          'onmovestart', 'onoffline', 'ononline', 'onpaste', 'onpropertychange', 'onmouseover',
                          'onmouseup',
                          'onmousewheel', 'onmove', 'onmoveend',
                          'onstop', 'onsubmit', 'onunload', 'onrowenter', 'onrowexit', 'onrowsdelete', 'onrowsinserted',
                          'onscroll']

    keywords_param = ['redirect', 'url', 'search', 'query', 'login', 'signup', 'contact']

    keywords_evil = ['pwd', 'pown', 'anonymous', 'control by', 'XSS', 'evil', 'hack', 'controled by', 'in control',
                     'under the control', 'h4ck', 'h@ck']

    data = {}
    data['url_ecode_length'] = len(string)
    data['url_ecode'] = string
    data['url_ecode_character2'] = 0
    for i in string:
        if i not in ptr:
            data['url_ecode_character2'] += 1
        else:
            continue

    string = urldecode(string)
    data['url_urldecode'] = string
    # data = {}
    # print(string)
    data['url_length'] = len(string)
    if ('<<' in string) or ('>>' in string):
        data['url_duplicated_characters'] = 1
    else:
        data['url_duplicated_characters'] = 0
    if any(i in string for i in '"\'>'):
        data['url_special_characters'] = 1
    else:
        data['url_special_characters'] = 0
    for tag in tags:
        if (re.search('<\s*' + tag + '.*>|<\s*/\s*' + tag + '\s*>', string, flags=re.IGNORECASE)):
            data['url_tag_' + tag] = 1
        else:
            data['url_tag_' + tag] = 0
    for attr in attrs:
        if (re.search(attr + '\s*=', string, flags=re.IGNORECASE)):
            data['url_attr_' + attr] = 1
        else:
            data['url_attr_' + attr] = 0
    for event in eventHandlersAttrs:
        if (re.search(event + '\s*=', string, flags=re.IGNORECASE)):
            data['url_event_' + event] = 1
        else:
            data['url_event_' + event] = 0

    if ('document.cookie' in string):
        data['url_cookie'] = 1
    else:
        data['url_cookie'] = 0
    # ------------------------------------------------------------
    data['url_redirection'] = any(
        i in string for i in ['document.documentURI', 'document.URLUnencoded', 'document.baseURI',
                              'window.history', 'window.location', 'window.navigate',
                              'document.URL', 'location', 'top.location', 'self.location',
                              'window.open'])
    # data['url_number_domain_2'] =0
    data['url_number_keywords_evil'] = sum(i in string.lower() for i in keywords_evil)
    data['url_number_keywords_param'] = sum(i in string.lower() for i in keywords_param)
    data['url_number_ip'] = len(re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(\.\d{1,3}\.\d{1,3})?', string))
    data['url_number_domain'] = len(re.findall(
        r'(([\w]+:)?//)?(([\d\w]|%[a-fA-f\d]{2,2})+(:([\d\w]|%[a-fA-f\d]{2,2})+)?@)?([\d\w][-\d\w]{0,253}[\d\w]\.)+[\w]{2,63}(:[\d]+)?(/([-+_~.\d\w]|%[a-fA-f\d]{2,2})*)*(\?(&?([-+_~.\d\w]|%[a-fA-f\d]{2,2})=?)*)?(#([-+_~.\d\w]|%[a-fA-f\d]{2,2})*)?',
        string))
    return data
if __name__ == '__main__':
    # call function
    page = {}
    page['url'] = 'http://cyber.law.harvard.edu/stockspam/public/onemsg.php?symbol=%3Ch1%3E%3Cscript%3Ealert%28/hacked/|cyber.law.harvard.edu'
    urlparsed = parse_url(page['url'])
    for keys, values in urlparsed.items():
        print('{0},{1}'.format(keys,values))
