actors = {
'a': ('town_commoner', None),
'b': ('town_bandit', None),
'c': ('town_thug', None),
'd': ('town_assassin', None),
'e': ('town_bandit_captain', None),
'f': ('merchant', None),
}

#tuple with actor creation function and the tile to underneath

items = None

exits = {
'1': ('overworld', 1, '<')
}

vault_layouts = [
[
'################################################################################',
'################################################################################',
'######################################    ######################################',
'######################    ############   #######################################',
'#####################                                      #####################',
'############# #####                                          ###  ##############',
'############  ###                               #######        #  ##############',
'#########    ##                              ####     ####        ##############',
'########                         a          ##           ##        #############',
'########  #                                 #      f      #         ####  ######',
'###########                                 ##           ##          ####  #####',
'##########                   #######         ####     ####            ###  #####',
'#########                   ##     ##           ###+###         a      ##   ####',
'########     a             ##   1   ##                                  ##  ####',
'#######                     ##     ##                                    #  ####',
'######                       ###+###                                        ####',
'#####                                                                       ####',
'####      #####                                                             ####',
'####     ##   ##                                                            ####',
'###      #     #                                                             ###',
'###      #     +                                                              ##',
'###      #     #                                                              ##',
'##       ##   ##                                                              ##',
'##        ## ##                                                #######        ##',
'##                                                             #     #        ##',
'##                      ###                                    #     #        ##',
'##                      #                                      #  b           ##',
'##                      #     b                                #  b          ###',
'##                      #                                      #     #       ###',
'##                      #  c      +                            #     #       ###',
'###      aa             #         #                            #     #       ###',
'###                     #         #                            #     #       ###',
'####                    ###########                        ####### ###       ###',
'####                                  #####                #         #       ###',
'####                                  #   #                #         #       ###',
'####                                  #                    #         #       ###',
'####          #######                 # b                  +    c    #       ###',
'####          #     #                 #   #                          #       ###',
'####             c  #                 #   #                #         #       # #',
'####              c #                 #####                #         #         #',
'####                #                                      ###########        ##',
'#####               #    #######                                             ###',
'#####          ######   ##     ##                                           ####',
'######                 ##       ##    #################                   ######',
'#######                #         ######      c        #####        a     #######',
'########               #    d    #              b                       ########',
'########     aa        #    e    +         b                           #########',
'########               #         #                                    ##########',
'#########              #         ######               #####          ###########',
'##########             ##       ##    #################             # ##########',
'#############           ##     ##                                     ##########',
'###############          #######                                    ############',
'###############                                                   ##############',
'#################                                            ###################',
'##################                                         #####################',
'####################                                    ########################',
'###########################                             ########################',
'################################          #######     ##########################',
'#################################     ##########################################',
'################################################################################']]