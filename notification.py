from win10toast import ToastNotifier
class Notification:
    def __init__(self):
        self.toast = ToastNotifier()

    def Notify(self):
        self.toast.show_toast("Notification", "Notification", duration=5)

