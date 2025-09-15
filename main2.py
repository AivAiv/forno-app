from backend.state import SystemState
from backend.controller import Controller
from ui.app import MyApp

if __name__ == "__main__":
    state = SystemState()
    controller = Controller(state)
    controller.start()

    MyApp(state=state).run()
