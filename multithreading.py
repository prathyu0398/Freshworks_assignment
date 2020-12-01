import threading
import initial as x

t1 = threading.Thread(target=x.create, args=("yepppie",20,10))
t2=threading.Thread(target=x.delete, args=("gy"))

t1.start()

t2.start()

t1.join()

t2.join()
