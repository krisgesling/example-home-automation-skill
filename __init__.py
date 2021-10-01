from mycroft import MycroftSkill, intent_file_handler


class ExampleHomeAutomation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('automation.home.example.intent')
    def handle_automation_home_example(self, message):
        self.speak_dialog('automation.home.example')


def create_skill():
    return ExampleHomeAutomation()

