from plyer import notification

def register_correct():
    notification.notify(
        title = "OnlineChess",
        message = "You registered successfuly into OnlineChess",
        app_name = "OnlineChess",
        timeout = 10,
        toast = True
    )