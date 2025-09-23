import wx
from controller.media_controller import MediaController

class PlayerUI(wx.Dialog):
    def __init__(self, parent, title):
        super(PlayerUI, self).__init__(parent, title=title, size=(400, 200))
        self.media_controller = MediaController(url=None)

        panel = wx.Panel(self)
        
        # Sizers
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        volume_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Controles
        self.play_pause_btn = wx.Button(panel, label=_(u"Reproducir"))
        self.avanzar_live_btn = wx.Button(panel, label=_(u"Adelantar hasta el tiempo actual de la transmisión"))
        self.mute_btn = wx.Button(panel, label=_(u"Silenciar"))
        self.stop_live_btn = wx.Button(panel, label=_(u"Detener reproducción de trasmisión"))
        
        self.volume_label = wx.StaticText(panel, label=_(u"Volumen:"))
        self.volume_slider = wx.Slider(panel, value=100, minValue=0, maxValue=100,
                                        style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS)

        # Adición de los botones al sizer horizontal
        button_sizer.Add(self.play_pause_btn, 0, wx.ALL, 5)
        button_sizer.Add(self.avanzar_live_btn, 0, wx.ALL, 5)
        button_sizer.Add(self.mute_btn, 0, wx.ALL, 5)
        button_sizer.Add(self.stop_live_btn, 0, wx.ALL, 5)

        # Adición del control de volumen al sizer horizontal
        volume_sizer.Add(self.volume_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        volume_sizer.Add(self.volume_slider, 1, wx.EXPAND | wx.ALL, 5)

        # Adición de los sizers al sizer principal
        main_sizer.Add(button_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        main_sizer.Add(volume_sizer, 0, wx.EXPAND | wx.ALL, 10)

        panel.SetSizerAndFit(main_sizer)
        self.Layout()

        # Enlazar eventos (sin funcionalidad, solo el esqueleto)
        self.Bind(wx.EVT_BUTTON, self.on_play_pause, self.play_pause_btn)
        self.Bind(wx.EVT_BUTTON, self.on_avanzar_live, self.avanzar_live_btn)
        self.Bind(wx.EVT_BUTTON, self.on_mute, self.mute_btn)
        self.Bind(wx.EVT_BUTTON, self.on_stop, self.stop_live_btn)
        self.Bind(wx.EVT_SLIDER, self.on_volume_change, self.volume_slider)
        self.is_paused = True

    # Métodos para la funcionalidad (listos para ser implementados)
    def on_play_pause(self, event):
        self.media_controller.toggle_pause()
        if self.is_paused:
            self.play_pause_btn.SetLabel(_(u"&Pausar"))
        else:
            self.play_pause_btn.SetLabel(_(u"Reproducir"))
        self.is_paused = not self.is_paused
        # print("Botón Play/pause presionado.")

    def on_avanzar_live(self, event):
        print("Botón avanzar hasta la transmisión presionado.")

    def on_mute(self, event):
        print("Botón silenciar presionado.")

    def on_stop(self, event):
        print("Botón Stop presionado.")

    def on_volume_change(self, event):
        volume_level = self.volume_slider.GetValue()
        print(f"Volumen cambiado a: {volume_level}")

    def show_player(self):
        return self.ShowModal()
    
    def close_player(self):
        return self.Destroy()

if __name__ == '__main__':
    app = wx.App()
    dialog = PlayerUI(None, _(u"Reproductor de Audio"))
    dialog.ShowModal()
    dialog.Destroy()
    app.MainLoop()