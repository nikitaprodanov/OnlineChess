from plyer import notification

def login_correct():
    notification.notify(
        title = "OnlineChess",
        message = "You logged in successfuly",
        app_name = "OnlineChess",
        timeout = 10,
        toast = True
    )