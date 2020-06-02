from plyer import notification

def register_correct():
    notification.notify(
        title = "OnlineChess",
        message = "You registered successfuly into OnlineChess",
        app_name = "OnlineChess",
        app_icon = "/home/nikita/Desktop/Python/OnlineChess/static/styling/OnlineChess.png",
        timeout = 10,
        toast = True
    )