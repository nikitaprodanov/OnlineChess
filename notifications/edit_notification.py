from plyer import notification

def edit_correct():
    notification.notify(
        title = "OnlineChess",
        message = "You edited your credentials successfuly.",
        app_name = "OnlineChess",
        timeout = 10,
        toast = True
    )