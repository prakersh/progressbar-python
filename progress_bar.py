import os
def update_progress(progress, maxi):
    per =  int(progress*100/maxi)
    leni = os.get_terminal_size().columns - 4
    bar = int(leni*per/100)
    if  per > 50:
        filler = "="*int( bar - leni/2)
        if per == 100:
            print('\r%s%s%%%s' %("="*int(leni/2), per, "="*int(leni/2)))
        else:
            print('\r%s%s%%%s>' %("="*int(leni/2), per, filler), end="")
    else:
        filler = " "*int(leni/2 - bar )
        print('\r%s>%s%s%%' %("="*(bar - 1), filler, per), end="")
