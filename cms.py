import requests
import sys
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import Fore

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
listSite = sys.argv[1]
op = [i.strip() for i in open(listSite, "r").readlines()]
fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN


def check(site):
    try:
        ####TAMBAHONO DEWE SU####
        wordpress = requests.get(site + "/wp-includes/js/jquery/jquery.js", verify=False, allow_redirects=False,
                                 timeout=10)
        wordpress1 = requests.get(site + "", verify=False, allow_redirects=False, timeout=10)
        joomla = requests.get(site + "/administrator/", verify=False, allow_redirects=False, timeout=10)
        joomla1 = requests.get(site + "/media/system/js/core.js", verify=False, allow_redirects=False, timeout=10)
        opencart = requests.get(site + "/admin/view/javascript/common.js", verify=False, allow_redirects=False,
                                timeout=10)
        opencart1 = requests.get(site + "/store/admin/view/javascript/common.js", verify=False, allow_redirects=False,
                                 timeout=10)
        opencart2 = requests.get(site + "/shop/admin/view/javascript/common.js", verify=False, allow_redirects=False,
                                 timeout=10)
        laravel = requests.get(site + "/vendor/phpunit/phpunit/composer.json", verify=False, allow_redirects=False,
                               timeout=10)  # only laravel phpunit
        if 'jQuery Foundation' in wordpress.content:
            print("{}# {}" + site + "{} | {}Wordpress").format(fg, fw, fw, fg)
            open('Wordpress.txt', 'a').write(site + "\n")
        elif '/wp-inclues/' in wordpress1.content or '/wp-content' in wordpress1.content:
            print("{}# {}" + site + "{} | {}Wordpress").format(fg, fw, fw, fg)
            open('Wordpress.txt', 'a').write(site + "\n")
        elif 'mod-login-username' in joomla.content:
            print("{}# {}" + site + "{} | {}Joomla").format(fg, fw, fw, fg)
            open('Joomla.txt', 'a').write(site + "\n")
        elif 'writeDynaList' in joomla1.content:
            print("{}# {}" + site + "{} | {}Joomla").format(fg, fw, fw, fg)
            open('Joomla.txt', 'a').write(site + "\n")
        elif 'getURLVar' in opencart.content:
            print("{}# {}" + site + "{} | {}Opencart").format(fg, fw, fw, fg)
            open('Opencart.txt', 'a').write(site + "\n")
        elif 'getURLVar' in opencart1.content:
            print("{}# {}" + site + "{} | {}Opencart").format(fg, fw, fw, fg)
            open('Opencart.txt', 'a').write(site + "/store/ \n")
        elif 'getURLVar' in opencart2.content:
            print("{}# {}" + site + "{} | {}Opencart").format(fg, fw, fw, fg)
            open('Opencart.txt', 'a').write(site + "/shop/ \n")
        elif 'sebastian@phpunit.de' in laravel.content:
            print("{}# {}" + site + "{} | {}Laravel PHPunit").format(fg, fw, fw, fg)
            open('PHPunit.txt', 'a').write(site + " \n")
        else:
            print("{}# {}" + site + "{} | {}Other CMS").format(fg, fw, fw, fc)
            open('OtherCMS.txt', 'a').write(site + " \n")
    except Exception as e:
        print("{}# {}" + site + "{} | {}" + str(e) + "").format(fr, fw, fw, fr)


kekw = Pool(666)  # thread
kekw.map(check, op)
kekw.close()
kekw.join()
