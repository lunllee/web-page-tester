from scenario.scenario_1 import Scenario


if __name__ == '__main__':
    scenario = Scenario('https://localhost:8081/admin')
    scenario.start()
