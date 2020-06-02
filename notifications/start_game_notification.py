from plyer import notification

def start_game_notification():
    notification.notify(
        title = "OnlineChess",
        message = "You are in a party now.",
        app_name = "OnlineChess",
        timeout = 10,
        toast = True
    )