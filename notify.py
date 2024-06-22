from winotify import Notification
from winotify import audio
from status import Status
class Notify:
    def __init__(self):
        pass
    def show_notification(self, controller):
        for task in controller.tasks:
            if task["status"] == Status.AWAITING.value:
                toast = Notification(
                    app_id="Hello",
                    title="Task Alert",
                    msg="You have an awaiting task to do",
                    duration="short"
                )
                toast.set_audio(audio.SMS, loop=False)
                toast.show()
                break # stop

