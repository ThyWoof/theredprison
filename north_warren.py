actors = {'a': ('town_commoner', 'indoors'),
'b': ('town_guard', None),
'c': ('merchant', 'indoors'),
'A': ('odette', 'indoors'),
'B': ('sunny', 'indoors'),
'C': ('susie', 'indoors'), 
'D': ('saint_barnabas', None),
'E': ('ingefred', 'indoors')
} #tuple with actor creation function and the tile to underneath

items = None

exits = {
'1': ('overworld', 1, '<')
}

vault_layouts = [
[
'                                                                                ',
'                                                                                ',
'                                                                                ',
'                                                                                ',
'        t                                                                       ',
'                                                             t                  ',
'                           t                                                    ',
'                                    #####                                       ',
'                  #######           #,,,#                                       ',
'                  #,,,,,#           #,a,#                                       ',
't                 #,,,,,#           #,,,#                                  Tt   ',
'                  #,,a,,#           #,,,+     t                            T    ',
'       ttt        #,,,,,#      ######,,,#                                       ',
'        T         ###+###      #,,,,+,,,#                    ########           ',
'       T                       #,,,,#####       #######      #,,,a,,#           ',
'                               #,a,,#           #,a,,,#      #,,,,a,#           ',
'                               #,,,,#           #,,,,,#      +,,,,,,#           ',
'                       ######  ####+#           ####+##      #,,,,,,#           ',
'                       #,,,,#                ######          ########           ',
'           ######      #,c,,#           b    #,,,,#                   t         ',
'           #,,,,#      #,,,,#                #,E,,#                             ',
'           #,,a,#      #,,,,#                #,,,,#                             ',
'     TT    #,,a,+      #,,,,+      t         #,,,,#                             ',
'           #,,,,#      ######                ##++##       ####                  ',
'           ######                T                        #,a#                  ',
'                               t                          +,,#                  ',
'                                                          ####                  ',
'                           b                   Tt                               ',
'                                      D                                         ',
'                   #########                                                    ',
'   1               #,,,,,,,#                                ####                ',
'                   #,,,B,,,#                         b      #,,#          Tt    ',
'                   #,,A,C,,+                                #,,#                ',
'       t           #,,,,,,,#     t                          #a,#                ',
'                   #########                                +,,#                ',
'                                              t             #,,#                ',
'                                               T            #,,#                ',
'                                                  ###+##    ####                ',
'                                                  #,,,,#                        ',
'                              #+#                 #,,c,#                        ',
'                              #,#     Tt          ######                        ',
'                     #####+#  #,#                                               ',
'                     #,,,,,#  #,#                                       TT      ',
'       T     Tt      #,,a,,#  ###                                               ',
'       t             #,,,,,#                 ###+###      ###+###               ',
'                     #,,,,,#                 #,,,,a#      #,,,,,#               ',
'                     #,,,,,#                 #,,,,,#      #,,,,,#               ',
'                     #######                 #######      #,,a,,#               ',
'                                                          #,,,,,#               ',
'                                  ###+##                  #####+####            ',
'                                  #,,,,#                    #,,,,,,#            ',
'        T                         ######                    #,,,,,,#            ',
'                                                            #,,,,,,#            ',
'                                                            ########            ',
'                                                                                ',
'            t                                                                   ',
'                                                                       t        ',
'                      t                                               Tt        ',
'                                                                                ',
'                                                                                ']]