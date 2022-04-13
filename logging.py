import logging
logging.basicConfig(filename='mona.log',level=logging.DEBUG,format='%(acstime)s,%(levelname)s,(messange)s')
def area_of_circle(r):
    try:
        pi=3.14
        logging.info("you hav entered %c and %c sucessfully",r,pi)
        area= pi*r**2
        logging.info("execution occured",area)
    except Exception as e:
        logging.error("Error occured")
        logging.exception("excption occured",+str(e))
area_of_circle(20)