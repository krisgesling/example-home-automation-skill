Feature: Example Home Aussie Skill
 
 Scenario: user asks a question about a person
   Given an english speaking user
    When the user says "make it comfortable"
    Then home-automation-skill should fetch current temperature inside # sensor
    And home-automation-skill should determine the current seasonal weather # weather request
    And home-automation-skill should fetch the current temperature outside # sensor or weather request
    And home-automation-skill references previous temperature preference # internal state or db query
    And home-automation-skill should set temperature on thermostat # API call
    Then home-automation-skill should set fetch current humidity # sensor
    And home-automation-skill should ask "should I turn on the de-humidifier" # Skill internals
    When the user says "make it so"
    Then home-automation-skill should reply "air conditioner is operating within normal functional parameters"