import os
import platform

def clear_screen():
    command = "cls" if platform.system().lower()=="windows" else "clear"
    os.system(command)

def showWelcome():
    clear_screen()
    print("\033[96m {}\033[00m" .format("""
 WWWWWWWW                           WWWWWWWW                    lllllll
W::::::W                           W::::::W                    l:::::l
W::::::W                           W::::::W                    l:::::l
W::::::W                           W::::::W                    l:::::l
 W:::::W           WWWWW           W:::::W     eeeeeeeeeeee     l::::l     cccccccccccccccc   ooooooooooo      mmmmmmm    mmmmmmm       eeeeeeeeeeee
  W:::::W         W:::::W         W:::::W    ee::::::::::::ee   l::::l   cc:::::::::::::::c oo:::::::::::oo  mm:::::::m  m:::::::mm   ee::::::::::::ee
   W:::::W       W:::::::W       W:::::W    e::::::eeeee:::::ee l::::l  c:::::::::::::::::co:::::::::::::::om::::::::::mm::::::::::m e::::::eeeee:::::ee
    W:::::W     W:::::::::W     W:::::W    e::::::e     e:::::e l::::l c:::::::cccccc:::::co:::::ooooo:::::om::::::::::::::::::::::me::::::e     e:::::e
     W:::::W   W:::::W:::::W   W:::::W     e:::::::eeeee::::::e l::::l c::::::c     ccccccco::::o     o::::om:::::mmm::::::mmm:::::me:::::::eeeee::::::e
      W:::::W W:::::W W:::::W W:::::W      e:::::::::::::::::e  l::::l c:::::c             o::::o     o::::om::::m   m::::m   m::::me:::::::::::::::::e
       W:::::W:::::W   W:::::W:::::W       e::::::eeeeeeeeeee   l::::l c:::::c             o::::o     o::::om::::m   m::::m   m::::me::::::eeeeeeeeeee
        W:::::::::W     W:::::::::W        e:::::::e            l::::l c::::::c     ccccccco::::o     o::::om::::m   m::::m   m::::me:::::::e
         W:::::::W       W:::::::W         e::::::::e          l::::::lc:::::::cccccc:::::co:::::ooooo:::::om::::m   m::::m   m::::me::::::::e
          W:::::W         W:::::W           e::::::::eeeeeeee  l::::::l c:::::::::::::::::co:::::::::::::::om::::m   m::::m   m::::m e::::::::eeeeeeee
           W:::W           W:::W             ee:::::::::::::e  l::::::l  cc:::::::::::::::c oo:::::::::::oo m::::m   m::::m   m::::m  ee:::::::::::::e
            WWW             WWW                eeeeeeeeeeeeee  llllllll    cccccccccccccccc   ooooooooooo   mmmmmm   mmmmmm   mmmmmm    eeeeeeeeeeeeee

    """))
