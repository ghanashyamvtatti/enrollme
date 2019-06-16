import requests
from bs4 import BeautifulSoup
import smtplib
import re
import properties
import time

jar = requests.cookies.RequestsCookieJar()

cFile = open('cookies.txt', 'r')
for line in cFile:
    if not line.startswith('#'):
        data = re.split(r'\t', line.strip())
        if data.__len__() >= 7:
            jar.set(data[5], data[6], domain=data[0], path=data[2])


def check_course_status(course_id='win10divDERIVED_REGFRM1_SSR_STATUS_LONG$1'):
    """
    Query Albert to check if course is available
    :param course_id:
    :return:
    """
    global jar
    url = 'https://sis.portal.nyu.edu/psp/ihprod_10/EMPLOYEE/SA/c/SA_LEARNER_SERVICES_2.SSR_SSENRL_CART.GBL'
    resp = requests.get(url, cookies=jar)
    soup = BeautifulSoup(resp.text, 'html.parser')
    status = soup.find(id=course_id).find('img').attrs['alt']
    # print(status)
    if status != 'Closed':
        message = f"The course you're looking for is currently {status}"
        email_me(message)
        exit(0)


def email_me(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(properties.EMAIL_ADDR, properties.EMAIL_PASS)
    server.sendmail(properties.EMAIL_ADDR, properties.EMAIL_ADDR, message)
    server.quit()


if __name__ == '__main__':
    while True:
        check_course_status()
        time.sleep(30)
