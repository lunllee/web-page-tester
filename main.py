from scenario.scenario_2 import Scenario_2


def main():
    # scenario = Scenario_1('https://localhost:8081/admin')
    scenario = Scenario_2('https://localhost:8081')
    scenario.start()


if __name__ == '__main__':
    main()
