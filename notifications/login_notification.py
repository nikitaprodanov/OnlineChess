from plyer import notification

def login_correct():
    notification.notify(
        title = "OnlineChess",
        message = "You logged in successfuly",
        app_name = "OnlineChess",
        app_icon = "/home/nikita/Desktop/Python/OnlineChess/static/styling/OnlineChess.png",
        timeout = 10,
        toast = True
    )