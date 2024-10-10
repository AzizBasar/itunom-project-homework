


# therading uygulayabilmek için threading kütüphanesini, 1 saniye aralıklarla kodun çalışabilmesi için time kütüphanesini açtım
import time
import threading

# öncelikle bir class tanımladım ve 'self' fonksiyonu ile değişkenlik sağladım, "running " fonksiyonuyla döngüyü başlattım
class Vehicle():
  def __init__(self,name,location,altitude,speed,aspect='north'):
    self.name = name
    self.location = location
    self.altitude = altitude
    self.speed = speed
    self.aspect = aspect
    self.running = True
 
 # "move" fonksiyonu ile güncellenecek olan "location" bilgisine "speed" miktarını ekledim
  def move(self):
     self.location += self.speed
     
  # "update" fonksiyonu ile kinematik bilgilerinin güncellenmesini sağladım ve hangi bilgilerin yazılmasını sırasıyla belirledim
  def update_kinematik(self):
     while self.running:
      self.move()
      print (f" {self.name},location:{self.location} , altitude: {self.altitude} , speed: {self.speed}, aspect: {self.aspect}" )
      time.sleep(1)

# oluşturduğum "vehicle" sııfından üç adet nesne atayıp "super()__init__" fonksiyonuyla miras almasını sağladım
class quadcopter(Vehicle):
   def __init__(self,name, location=2.564745 , altitude=120, speed=35, aspect='north'):
      super().__init__(name,location, altitude, speed, aspect)

class iha(Vehicle):
   def __init__(self,name, location=3.968667, altitude=300, speed=25, aspect='sorth'):
      super().__init__(name,location, altitude, speed, aspect)

class drone(Vehicle):
   def __init__(self,name, location=5.754365, altitude=50, speed=40, aspect='northwest'):
      super().__init__(name,location, altitude, speed, aspect)

# "nesne"leri kendi isimleriyle atanmasını sağladım ve komutun, araçaların ismiyle başlaması için "name=" kullandım
quadcopter = quadcopter(name= quadcopter)
iha = iha(name= iha)
drone = drone(name= drone)

# iş parçacıklarını başlattım ve "target" fonksiyonu ile thread'lerin güncellenen kinematik bilgisine yönlendirdim
thread_quadcopter=threading.Thread (target=quadcopter.update_kinematik)
thread_iha=threading.Thread (target=iha.update_kinematik)
thread_drone=threading.Thread (target=drone.update_kinematik) 

# iş parçacıklarını başlattım
thread_quadcopter.start()
thread_iha.start()
thread_drone.start()
 
# "join" fonksionuyla iş parçacıklarının çalıştırılıp birbirini beklemesini sağladım
thread_quadcopter.join()
thread_iha.join()
thread_drone.join()