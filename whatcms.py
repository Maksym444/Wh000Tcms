#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import requests
import json
import sys
import os
import random
from platform import platform
import io
import shutil
import argparse


banner_font = '''
     Author : Dj()k4r
     CMS Identificator With whatcms.org API

 '''

def check_dirb():
    dirb = shutil.which ('dirb')
    if dirb==None:
        sys.exit('{0} Install dirb, befoure use!')

def check_system():
    if platform() =="Linux":
        sys.exit("{0} You should use Linux!")

def check_python_version():
    version_py = sys.version[0]
    if '3' not in version_py:
        print(banner_font)
        sys.exit('{0} Please Run cmsid.py with python3!')

home_dir=os.path.abspath('.')

def send_requests_url():
    try:
        url = args.url
        key = '746f350b4b16644cd12fdb77a8ea14155c083cd3269036b30126e423ba0d7d61ffdd4f'
        r = requests.get('https://whatcms.org/APIEndpoint/Detect?key=' + key+ '&url=' + url)
        content_requests = r.text
        obj = json.loads(content_requests)
        code = obj['result']['code']
        if code == 200:
            print('CMS found!')
        else:
            print("CMS didn`t found!")
        msg = obj['result']['msg']
        if msg == "Success":
            name = obj['result']['name']
            version = obj['result']['version']
            print('Requests Successfull !')
            print('CMS Name : %s' % (name))
            print('CMS Version : %s' % (version))
            with open(os.path.abspath('CMSList/uselist.txt'), 'r') as f:
                cms_list = [line.strip() for line in f]
                if name in cms_list:
                    print ("Scanning begin!!!")
                    os.system ('dirb %s %s/CMSList/%s.txt > %s/Result/Scanning.txt -r'% (url,home_dir,name, home_dir)) #work with reply
                    print("Scanning finish!!!")
                    word = "CODE:"
                    with io.open('%s/Result/Scanning.txt' % (home_dir)) as file:
                        for lines in file:
                            if word in lines:
                                f = open('Result.txt', 'w')
                                f.writelines(lines + "\n")
                                print(lines, "\n","------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------","\n", end='')
                                f.close()
                else:
                    print ("Sorry, we haven't structure of this CMS(((")
        elif msg =='Too Many Requests':
            print('To quick, try to do a little bit later!!!')
        elif msg == 'Failed: CMS or Host Not Found(((':
            print('Seems, that CMS unrecognized!!!')

    except Exception as error_send_requests:
            print(error_send_requests)

def send_requests_file():
    try:
        s= args.file
        f=open(s)
        fd=f.readlines()
        for elem in fd:
            url = elem
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("")
            print(url)
            key = '746f350b4b16644cd12fdb77a8ea14155c083cd3269036b30126e423ba0d7d61ffdd4f'
            r = requests.get('https://whatcms.org/APIEndpoint/Detect?key=' + key+ '&url=' + url)
            time.sleep(20)
            content_requests = r.text
            obj = json.loads(content_requests)
            code = obj['result']['code']
            if code == 200:
                print('CMS found!')
            else:
                print("CMS didn`t found!")
            msg = obj['result']['msg']
            if msg == "Success":
                name = obj['result']['name']
                version = obj['result']['version']
                print('Requests Successfull !')
                print('CMS Name : %s' % (name))
                print('CMS Version : %s' % (version))
            elif msg =='Too Many Requests':
                print('To quick, try to do a little bit later!')
            elif msg == 'Failed: CMS or Host Not Found':
                print('Seems, that CMS unrecognized!')

    except Exception as error_send_requests:
            print(error_send_requests)

def banner_show():
    try:
            theme = ''
            choice_banner = [theme]
            random_choice_banner = random.choice(choice_banner)
            if random_choice_banner ==theme:
                os.system(random_choice_banner)
                print(banner_font)

    except Exception as error_banner:
        print(error_banner)

def main():
    check_python_version()
    check_dirb()
    banner_show()
    send_requests_url()
    send_requests_file()
    check_system()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=" Author : Dj()k4r CMS Identificator With whatcms.org API")
    parser.add_argument('-file', help='Add file with domains to check')
    parser.add_argument('-url', help='Add one url with http or https if requared')
    args = parser.parse_args()
    main()
