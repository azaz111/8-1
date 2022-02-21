import os , time
from subprocess import PIPE,Popen
from argparse import ArgumentParser

def plot(scolco,dirs,monitorind):
   #print(scolco +' : '+ dirs)
   while True:
      if len(os.listdir(monitorind)) < int(scolco) :
         time.sleep(5)
         print('Запускаю Плотинг')
         os.system(f'cd &&./bladebit/build/bladebit -n 1 -f b8e1d57e3e2dbb40ac8f2b257b762d05fcfc5b79c32a22255424644b7d183daa7c454624783f2d959c02eb1d2a4ba3a3 -p 91ea997633345082b15f83b957449180037030b6b7485f07ed4ee7558d08d3efbccf2c3d68ba724f5b3a8281a0055e27 {dirs}')       
      else:
         print('\r Статуст : {}'.format('Ожидаю  передачи '), end='')  
      time.sleep(20)


if __name__ == '__main__':
    parse = ArgumentParser(description=' Включаем плоттер в зависимрсти от заданного количества .')
    parse.add_argument('--scolco', default='3', help='Укажи количество плотов в папке .')
    parse.add_argument('--pach', default='/disk1', help='Путь в который плотить .')
    parse.add_argument('--monitorind', default='/disk1', help='Путь по которому мониторить .')
    args = parse.parse_args()
    plot(
       scolco=args.scolco,
       dirs=args.pach,
       monitorind=args.monitorind
    )

