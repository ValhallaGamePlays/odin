from errbot import BotPlugin

class PluginExample(BotPlugin):
        def odin_callback_troll(self, mess):
                    if mess.body.find('cookie') != -1:
                                    self.send(
                                         mess.frm,
                                          "What, you want a cookie!?",
                                    )
                     
                    if mess.body.find('complex doom') != -1:
                                    self.send(
                                            mess.frm,
                                             "Fuck Complex Doom!",
                                    )

                    if mess.body.find('call of duty') != -1:
                                     self.send(
                                             mess.frm,
                                              "Worst VG series ever BTW..."
                                    )
                
                    if mess.body.find('shit') != -1:
                                     self.send(
                                             mess.frm
                                              "fuck"
                                    )          
