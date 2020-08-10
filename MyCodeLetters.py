# GLOBALS:
# blocks = [GRASS, SAND, BRICK, STONE]

def PillarOfBlocks():
    Px, Py, Pz = Position()
    touch = Touch()
    if touch:
        Tx, Ty, Tz = touch

        for y in range(-1,10):
            SetBlock((Tx, Ty + y, Tz), BLOCK)

alphabet = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 01234567890!@#$%^&*()_+{}[]\|;:'",<.>/?`~'''



def PutLetters(s):
    ASCII = '''
  AAA   BBBBB    CCCCC  DDDDD   EEEEEEE FFFFFFF   GGGG  HH   HH IIIII     JJJ KK  KK LL      MM    MM NN   NN  OOOOO  PPPPPP   QQQQQ  RRRRRR   SSSSS  TTTTTTT UU   UU VV     VV WW      WW XX    XX YY   YY ZZZZZ         bb                  dd         fff         hh      iii   jjj kk     lll                                                         tt                                                        00000   1   2222   333333      44   555555    666   7777777  88888           00000  !!!   @@@@           /|-\ %%  %%  ^^    &&&                                       {{ }}    [[[[ ]]]] \\                ''  """""                       //  ???   `         
 AAAAA  BB   B  CC    C DD  DD  EE      FF       GG  GG HH   HH  III      JJJ KK KK  LL      MMM  MMM NNN  NN OO   OO PP   PP QQ   QQ RR   RR SS        TTT   UU   UU VV     VV WW      WW  XX  XX  YY   YY    ZZ   aa aa bb        cccc      dd   eee  ff    gggggg hh                kk  kk lll mm mm mmmm  nn nnn   oooo  pp pp     qqqqq rr rr   sss  tt    uu   uu vv   vv ww      ww xx  xx yy   yy zzzzz    00   00 111 222222     3333    444   55       66         777 88   88  99999  00   00 !!!  @ @@ @  ## ##  / |   %% %%  ^^^^  && &&   *   *  ((( )))            +++     {{   }}   [[     ]]  \\    ||         ''  """""      <<<     >>>     /// ?? ?? ```  ~~ ~~ 
AA   AA BBBBBB  CC      DD   DD EEEEE   FFFF    GG      HHHHHHH  III      JJJ KKKK   LL      MM MM MM NN N NN OO   OO PPPPPP  QQ   QQ RRRRRR   SSSSS    TTT   UU   UU  VV   VV  WW   W  WW   XXXX    YYYYY    ZZ   aa aaa bbbbbb  cc      dddddd ee   e ffff gg   gg hhhhhh  iii   jjj kkkkk  lll mmm  mm  mm nnn  nn oo  oo ppp  pp qq   qq rrr  r s     tttt  uu   uu  vv vv  ww      ww   xx   yy   yy   zz     00   00  11     222   3333   44  4   555555  666666     777   88888  99   99 00   00 !!! @ @  @@ ####### \-|-\   %%   ^  ^  &&&&&&&  ***  (((   )))         +++++++ {{{     }}} [[     ]]   \\   || ;;; ::: ''   """      <<<       >>>   ///     ??  `` ~  ~   
AAAAAAA BB   BB CC    C DD   DD EE      FF      GG   GG HH   HH  III  JJ  JJJ KK KK  LL      MM    MM NN  NNN OO   OO PP      QQ  QQ  RR  RR       SS   TTT   UU   UU   VV VV    WW WWW WW  XX  XX    YYY    ZZ   aa  aaa bb   bb cc     dd   dd eeeee  ff   ggggggg hh   hh iii   jjj kk kk  lll mmm  mm  mm nn   nn oo  oo pppppp   qqqqqq rr      sss  tt    uu   uu   vvv    ww ww ww    xx    yyyyyy  zz      00   00  11  2222       333 44444444    5555 66   66   777   88   88  999999 00   00     @  @@@  #######   | |  %% %%      &&& &&    ***  (((   )))         +++++++ {{{     }}} [[     ]]    \\  ||                    ,  <<<  ...  >>>  ///     ??             
AA   AA BBBBBB   CCCCC  DDDDDD  EEEEEEE FF       GGGGGG HH   HH IIIII  JJJJJ  KK  KK LLLLLLL MM    MM NN   NN  OOOOO  PP       QQQQ Q RR   RR  SSSSS    TTT    UUUUU     VVV      WW   WW  XX    XX   YYY   ZZZZZ  aaa aa bbbbbb   ccccc  dddddd  eeeee ff        gg hh   hh iii   jjj kk  kk lll mmm  mm  mm nn   nn  oooo  pp           qq rr         s  tttt  uuuu u    v      ww  ww   xx  xx      yy zzzzz     00000  111 2222222 333333     444   555555   66666   777     88888      99   00000  !!!  @@@@@   ## ##  \-|-/ %%  %%       &&&&&&& *   * (((   ))) _______   +++     {{   }}   [[[[ ]]]]     \\ || ;;; :::           ,,,  <<< ... >>>  ///      ??             
                                                                                                                                                                                                                                                              ggggg              jjjj                                        pp           qq         sss                                           yyyyy                                                                                  999                                                                 ((( )))                     {{ }}                     || ;;                ,,                                        
'''
    fl = []
    x = 0
    for c in s:
        if c == ' ':
            fl.append((c, 0, 2))
            continue
        first = 9e99
        last = 0
        for line in ASCII.splitlines():
            if c in line:
                p = line.index(c)
                if p < first:
                    first = p
                p = line.rindex(c)
                if p > last:
                    last = p
        fl.append((c, first, last))

    for (c, a, b) in fl:
        y = 6
        if c == ' ':
            x += 6
        else:
            for line in ASCII.splitlines():
                l = line[a:b+1]
                X = 0
                for C in l:
                    if C == ' ':
                        yield((x+X,y,0,0))
                    else:
                        yield((x+X,y,0,1))
                    X += 1
                y -= 1
            x += b - a + 2

def f():
    touch = Touch()
    tx,ty,tz = touch if touch else (-40,0,-20)
    for x,y,z,b in PutLetters("Hello World!"):
        if b:
            SetBlock((tx+x, ty+y, tz+z), BRICK)

f()