from plyer import notification

def end_game():
    notification.notify(
        title = "OnlineChess",
        message = "The chess party is over",
        app_name = "OnlineChess",
        app_icon = "/home/nikita/Desktop/Python/OnlineChess/static/styling/OnlineChess.png",
        timeout = 10,
        toast = True
    )