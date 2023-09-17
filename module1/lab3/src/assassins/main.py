from AI import AI

artificial_intelligence = AI()

artificial_intelligence.greet()

first_time = True

while True:
    if first_time:
        artificial_intelligence.receive_data()
    else:
        artificial_intelligence.continue_receive_data()

    artificial_intelligence.give_info()
    if artificial_intelligence.ask_for_exit():
        artificial_intelligence.say_bye()
        break
    first_time = False
