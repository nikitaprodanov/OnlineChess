from plyer import notification

def end_game():
    notification.notify(
        title = "OnlineChess",
        message = "The chess party is over",
        app_name = "OnlineChess",
        timeout = 10,
        toast = True
    )