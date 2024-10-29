from rich.console import Console

def display_ascii_art():
    console = Console()
    
    # The full ASCII art illustration
    art = r"""
         Display Monitor                            CPU
         ____________________                     ____
        |                    |                   |    |
        |   (•◡•)            |                   |(≧◡≦)|
        |____________________|                   |____|
              |     |                            |    |
              |     |                            |____|
              |     |                            /|  |\
             /       \                           /    \
            /         \                         |      |
           /___________\                        |______|

                 \                              /
                  \                            /
   ______________________________       ______________________
  |                              |     |                      |
  |  01010100 01101000 01100001  |     |  01001000 01100101    |
  |  01101110 01101011 01110011  |     |  01101100 01101100    |
  |  00100001                    |     |  01101111 00100001    |
  |                              |     |  01011001 01101111    |
  |                              |     |  01110101 00100000    |
  |                              |     |  01110011 01100101    |
  |                              |     |  01100101 01101101    |
  |                              |     |  00100000 01100010    |
  |                              |     |  01110010 01101001    |
  |                              |     |  01100111 01101000    |
  |                              |     |  01110100 00100000    |
  |                              |     |  01110100 01101111    |
  |______________________________|     |  01100100 01100001    |
                                       |  01111001 00100001    |
                                       |______________________|

   CPU: "Hello! You seem bright today!"
   Display: "Thanks!"
    """
    
    # Print the ASCII art
    console.print(art)

def ascii_art1():
    #Return the ASCII art as a string.
    return r"""
         Display Monitor                            CPU
         ____________________                     ____
        |                    |                   |    |
        |   (•◡•)            |                   |(≧◡≦)|
        |____________________|                   |____|
              |     |                            |    |
              |     |                            |____|
              |     |                            /|  |\
             /       \                           /    \
            /         \                         |      |
           /___________\                        |______|

                 \                              /
                  \                            /
   ______________________________       ______________________
  |                              |     |                      |
  |  01010100 01101000 01100001  |     |  01001000 01100101    |
  |  01101110 01101011 01110011  |     |  01101100 01101100    |
  |  00100001                    |     |  01101111 00100001    |
  |                              |     |  01011001 01101111    |
  |                              |     |  01110101 00100000    |
  |                              |     |  01110011 01100101    |
  |                              |     |  01100101 01101101    |
  |                              |     |  00100000 01100010    |
  |                              |     |  01110010 01101001    |
  |                              |     |  01100111 01101000    |
  |                              |     |  01110100 00100000    |
  |                              |     |  01110100 01101111    |
  |______________________________|     |  01100100 01100001    |
                                       |  01111001 00100001    |
                                       |______________________|

   CPU: "Hello! You seem bright today!"
   Display: "Thanks!"
    """
#second ascii

def ascii_art2():
    #Return the ASCII art as a string
    return r"""

            :BPPP77Y:      JYYG&BBP!7GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            :BPPG?7J~      ?YY5&BGB7!PYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .GGPG57?!      !YYY#BGBY!5PYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .5BPGP777      ~5YYB#GGJ!JGYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .JBGBG7!P?~~~7!?YYJYYYGB!7GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .?BPPGJ!P#G555YYYYYJJJP&?!P5YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .7BPPGY7J!.::::^555P&&&#Y!JPYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .!GGPG5!J~      ?YJJB#BBP!7GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .!5GPG57??      7YYJG#BGG7!GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .!JBPPP77J      ~YYY5#GGG?!55YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .!?BPPG?!J.     :YYYY#BGBY!JPYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .77BPPG?!J:     .YYYJGBGGG!7GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .7!GPPGJ!?!   . .Y5YY5#GG#?!P5YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .7!PGPGY77BJ!!!7?J??J??7?#G!YPYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY555555555YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .7!YGGGP7!BG5555Y55555PPP##77GYYYYYYYYYYYYYYYYYYYYYYYYYYYYY5555J?7!~~~~!!7JY555YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .7!?BGGP7!5:.....!555YG&&&B7!GYYYYYYYYYYYYYYYYYYYYYYYYYY5P57^.               .~JP5YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            .7!!BPPG?!Y.     :YYYJY&#BGJ755YYYYYYYYYYYYYYYYYYYYYYYYPJ:                      .?GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            :7!!GGPG?!Y^     .YYYYJ#BPGJ!JGYYYYYYYYYYYYYYYYYYYYYY5P:                          ^GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            :7!!PBPGJ!J!      JYYYJGBPPP!7GYYYYYYYYYYYYYYYYYYYYY55       WHAT IS HE TRYING     !GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            :!!!J#PGY!??      7YYYJ5#PPG7!P5YYYYYYYYYYYYYYYYYYYYG.   TO SAY?                ~:  .BYYYYYYYYYYYYYYYYYY555Y555YYYYYYYYYYYYYYYYYYYYYYYYYYYY
            :7!!7BPPP?7Y      ~YYYYY#GPGY!JPYYYYYYYYYYYYYYYYYYYP?                                .GYYY555YYYYYYYJYYJ?77777JYJ5P555YYYYYYYYYYYYYYYYYYYYYY
            :!!!~GPPGJ!Y:.....~5555YBBPBG!7GYYYYYYYYYYYYYYYYYYYP!                               YG5Y5P555555PPPPPPPPPGGGYJ~JYG?JJYYY555YYYYYYYYYYYYYYYY
            :!!!^PPPGJ7JB777777?77???77J&Y!P5YYYYYYYYYYYYYYYYYY5Y                              JGP!P##GBGBBBBGGGBBGGGBB#Y7!Y5GJJJJJJJJJYGYYYYYYYYYYYYYY
            :7!!^JGPGY77B5YYYYYPPPPPPB##&G~JPYYYYYYYYYYYYYYYYYYYG^                          ^5P557BBGGG#P!.    :J#BGGBGY!?JPP55YYYJJJJJBYYYYYYYYYYYYYY
            :7!!^!GPG577J      Y5P5PP####B??G555555YYYYYYYYYYYYYYG!                     :75PYJGJ?BGGG#7   .~^   :#BGBPY~?JPG###BBGGPYJBYYYYYYYYYYYYYY
            :!!!^^GPBP?!Y    .!G5^!5555?~?5??PP55YJPGPY55YYYYYYYYY557:               ^7J555YYYJB?JBGG#~   Y#B#5   ~#G#5Y~JJPG&&#####BPYBYYYYYYYYYYYYYY
            ^!!!~.GPGG?!Y. .JPP55~~55P!^J5??YYYYYYYYYYY5PBGYYYYYYYYY5P5J7!~^^^^!!    PPYYYYYYYJB7YBGB5   J#GGG&:  .#GBYY~JJGG&####&#GPY#YYYYYYYYYYYYYY
            ^!!!!!GPPG7!J~!GP555Y~.^~~:?P5JPYY5555BG#  555GPPPYYYYYYYYYY5555555YPY:  .GYYYYYYYJB!5BG#~  .#GGGG#^  .#GBYY~JJGG&#####BGPYBYYYYYYYYYYYYYY
            ^!!!!!PPPGJ!Y#!~Y5Y!:.^^~:^.7P:?55PP55GG&#5555Y5YP#YYYYYYYYYYYYYYYYYYYPY~ :55JYYYYYB!PBG#:  ^#GGGG&:  ^&GBJY~JJGG######BB5YBYYYYYYYYYYYYYY
            ^!!!!.7GPG5?&5!JJ7:.:^.^^~7^!YP^^7JJ??JYYY555P5P5GBYYYYYYYYYYYYYYYYYYYYY55J?GBYYYYYG!GBG#.  ^#GGGG#   J#GGJY~JJBG&#####BB5YBYYYYYYYYYYYYYY
            ^!!!!.^BPGPB#75555!^:.:.^YBBGB&#5J7?7~?J5GBPYYYYYYYYYYYYYYYYYYYYYYYYYY5PYYYY5P7GBG#.#BGB#~   BBBGJJ~JJBG#####&BBY5BYYYYYYYYYYYYYY
            ^!!!!..BPGB&Y!5J7~..::.^G#GP#&#&##&5PPP555555555YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY557BBG#7   ^5P5^   ?#GBGJJ~YYBG#####&GBY5BYYYYYYYYYYYYYY
            ^!!!!. GPP#&?^77~:^^:.:GBP5B&###Y7PPYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYPJ?BGGG#^         J#GGBGYJ~YYGG&#####GGJPGYYYYYYYYYYYYYY
            ^!!!!^.PGG#&7~555?....~B5PGBB&##G!?GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYG?JBBBGGB57~^:^!YB#GGB#PY?!YYG5BBB#B#BGJPGYYYYYYYYYYYYYY
            ^!!!!!!PGG#&J:Y555!^^::G55PGG&###7!P5YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYG7JPBBGGGBBBB###BGGGBBBPY??JYGJJJYY555YJGPYYYYYYYYYYYYYY
            ^!!!!!~YBGB&5:!5Y?:...:Y5Y555GPG#P?YPYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYG7JYYYYYYYYYYYYYYYYYYYY?7^7YYGJYJJJJJJJJG5YYYYYYYYYYYYYY
            ^!!!!~ :BGB&B!.^~~!~^^:^GPY?::7Y5P5?Y55YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY5B###B###############&&###&&&&&&&&&&&&#GG5YYYYYYYYYYYYYY
            ^!!!!~ .GGB#&P~^555Y^.:^:7PP?~~!!^..~YBPYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYG75P55555555YYYYYYYYYYY55!YYPGYY555PPPP5G5YYYYYYYYYYYYYY
            ^!!!!!  PGB#&&P~755J!^^.::!^?555Y7!^!?YGPYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYG!####BBB###B##BB#BBB#B#B~?J5PJYYJJJJJJJG5YYYYYYYYYYYYYY
            ^!!!!!. YGGB&&&P!^:~555Y?^..~.^~!7!7~^:7GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYG7####B#5BB#B##GBBBBJGBBB~?JPPB&&BYJYYYJG5YYYYYYYYYYYYYY
            ^!!!!!. 7GPB#&&GBJ^:!J5555!^.^^~.!::~^:YGYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYB7#&&&#&PBJBBB#GBBBBB##BG~JJPP&&#&#5JYYJG5YYYYYYYYYYYYYY
            ^!!!!!. ^BPGB#&Y5BGY~:^^~~:.^^::.!..!.^PYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY#&7##&&#&G#B#BB#GBGBBPPB#G^JJG5G&&#&&YJYJG5YYYYYYYYYYYYYY
            ^!!!!!: .BPGGB&GJ5PGBPY7^:.^^...^:.^Y5BYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY5#&#?##&##&GB7#BBBB#BB#BB#BG^JJG5PGB&#&#JYJG5YYYYYYYYYYYYYY
            ^!!!!!^  PPPGP##!^JPPPGGBGPPYJJY5Y5B#BG5YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY#&&&?##&#BBGB5##BB#######&BP:JJGY5GG&&#&5YJG5YYYYYYYYYYYYYY
            ^!!!!!~..5GPGYB#P^.^7Y55PG##GPPP&&&#G7?GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJB&&&B?#BBB#BBG####BB#&######5^YJGY5GG#&#&GJJG5YYYYYYYYYYYYYY
            ^!!!!!!!!5GPGJGB&5^:~^^!?JY5PGG5BBB#B!!PYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYP&&&PP?###GPPPPPPG##B&&BBG#G#J^YJGY5GG#&#&GJJG5YYYYYYYYYYYYYY
            :!!!!!!!~7BPGYJB&&#!..^^..:~?5BGY77Y&Y!YPYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY5&&&&BPJBB#BPPPPPPG##B&##&&#B#?~YJGYYGG&&#&5YJG5YYYYYYYYYYYYYY
            :!!!!!!. .GPGP7Y#&#&G!^^^:^^::~?P###&P7?GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY#&#&&&PJBGB##&#&#####B&##&&&&#7~YJGY5B#&&&GJYJB5YYYYYYYYYYYYYY
            :!!!!!!:  5PGP?7PB?!JP57^^~^^:::^Y&BBG?7GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY#@&#&#5?#PBGPGPGGGB##B&#B&&###!!YJGYB&&#&&YYYJB5YYYYYYYYYYYYYY
            :!!!!!!^  ?GPGJ7?5  .?JGP7^^!~::..5#BB?!5PYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY5#@&55PJ#G#B##BBBB#B#B&#BB#BB#~7YJGB&&&#&#JYYJB5YYYYYYYYYYYYYY
            .!!!!!!^  ~G5PY77G?:.?JY5G?::!^:::~&GBY!?GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY5PYYPYBBBBBB#####GBB#BBBBBB#~7JJBBB&&&&BJYYJBYYYYYYYYYYYYYYY
            .!!!!!!~..~B5PP77P#7~??YYG5^^~^...7#GGG77GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY55#BBB#B#B#B###B#B#B##B#~?YJGP&&&&BYYYYYBYYYYYYYYYYYYYYY
            .!!!!!!!!!7BPPG?7Y#BY??YGP~^^!^^::B#GGBJ!5PYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY555#BB#####B#B#########BB~?YJGY55YYJYYYYYBYYYYYYYYYYYYYYY
            .!!!!!!!!!~PPPG?7?#5?YYJJ^^^!^..~PP#GGB5!?GYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY55P#GG#BPGGGBP#BBBBBBBG#B~?YJGYYYJYYYYYYYBYYYYYYYYYYYYYYY
            .!!!!!!!:  7GPPJ77G5^~~::!^~^~?PG5Y5Y?P#7!P?7777777777777777777777777777777777777?J5#GG#BGGBGB5#GGPGGG55#B^?YJGYPPJYYYYYY5P777777777777777
             !!!!!!!:  ^G5G577J#GPPYYY5PGBPY??J?JJ5&Y!Y:                                      ?75GGBB##&#&#&#&####BB#G^?YYGY5P55PP55YP!               
             ~!!!!!!^  .G5P577?GYGBB##BG5YJ?7!~^B&&#G!?7                                      YYYYYYYYYYYYY55PPPGGGGG5~?YYGYYYYYYY555P^               
             ~!!!!!!~   5PPP?77GPYJ?7~:..       J#BBB7!Y.                                      ...::~&##B!77??JJJY5P5P?J55B5YYJ?7!^:..                
             ^!!!!!!~   JGPGJ775!.              :#BBBY!J~                                           .&&&&.        Y@&@?.::...                         
             ^7!77???!~:!BPPP77J5~~^:..          GBGGG77Y                                           .&&#&^        5&&&5                               
         ....~????77!!!!7B5PG?77P!!!!!!~~^^::... J#GGB?!5:  .                         :.       ^?YPG#&&#&G~~~!!!~~B&#&G~!!!!!!!!~~~~~^^:.             
  ...::::...  .:^~!!!!!!!BP5G57!P?!!!!!!777!!!!!~7PPGB57Y~  .                                 ?&&&&&&##BB5!!!!!!J#&##&#!!!!!!!!!!!!!7777!.            
::...             ..:^~!!GBPGP7!J5!!~~^^::...       .....                                     .~!~~^^^^^^^~~!!!Y&&&&&#J!!!!!!!!!!!~~^:..              
                       ..^?Y5PJ??7..                                    ..                                   ..:!7?7~...........                      
            ........         ...                                     .?J???J!                                                           .:^^~~^:      
          .JYYJJJY?JJ.                                                .:^^^^.                                                           ^77?JJJY:     
           ..:^~~~~^:                                                                                                                        .        
                                                                                                                              ....   ...   .     ..   
                                                                                                                              ^7^~^!:^~^^:^:~::^^^^.  
                                                                                                                                                      
                                                                                                                                                      
"""


def ascii_art3():
    #Return the ascii art as a string
    return r"""
                                                                                                                                                                 
                                                                                                                                                                 
                                                                                       +                                                                         
             XXXXXXXXXXXX$                                                           +++                                                                         
            XX++xXXXXXX$$$$                                                   ++     +++                                           +++++++                       
           XXXx+XXXXX$$$$$$                                                 ++++     +++                                            + ++++                       
           XXXXXXXXX$$$$$$$                                                 ++++     +++                                                                         
      XXXXXXXXXXXX$$$$$$$$$ +++++            ++++++++++    ++++       +++  ++++++++  +++++++++++      +++++++++      ++++++++++                                  
    XXXXXXXXXXXXX$$$$$$$$$$ +++++++         +++      +++   ++++       +++   ++++     +++++   ++++   +++++    ++++  ++++     ++++                                 
    XXXXXXXXXXX$$$$$$$$$$$$ +++++++         +++       +++  ++++       +++   ++++     +++      ++++  +++       +++  +++       +++                                 
    XXXXXXXXX$$$$$$$$$$$$$++++++++++        +++       +++  ++++       +++   ++++     +++      ++++ ++++       ++++ +++       +++                                 
    XXXXXXXX$$++++++++++++++++++++++        +++       +++  ++++       +++   ++++     +++      ++++ ++++       ++++ +++       +++                                 
    XXXXXX$$++++++++++++++++++++++x         +++       +++  ++++       +++   ++++     +++      ++++  +++       +++  +++       +++                                 
    XXXX$$$++++++++++++++++++++xxxx         +++      ++++   +++      ++++   ++++     +++      ++++  ++++     ++++  +++       +++                                 
     XX$$$$++++++++++++++++++xxxxx          +++++++++++      ++++++++++++    +++++   +++      ++++    +++++++++    +++       +++                                 
           ++++++++++++++++                 +++                       +++                                                                                        
           ++++++++++++xxxx                 +++                      +++                                                                                         
           +++++++++xx++++x                 +++                     x++x                                                                                         
             +++++xxxxx+xxx                 xxx                 xxx+x+                                                                                           
                +xxxxx+                                                                                                                                          
                                                                                                                                                                 
         &&&&&&&&&&&&&&&&&&&&                                                                                                                                    
          &&&&&&&&&&&&&&&&&                                                                                                                               
          """