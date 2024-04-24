class ApplicationState:
    instance = None

    def __init__(self):
        self.is_logged_in = False

    @staticmethod
    def get_app_state():
        if not ApplicationState.instance:  
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance


if __name__ == "__main__":
    app_state_1 = ApplicationState.get_app_state()
    print(app_state_1.is_logged_in) # False

    app_state_2 = ApplicationState.get_app_state()
    app_state_1.is_logged_in = True

    print(app_state_1.is_logged_in) # True
    print(app_state_2.is_logged_in) # True
