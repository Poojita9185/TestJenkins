Feature: Currency Conversion
  Scenario: Convert currency from one to another
    Given the User launch the url in browser
    When the user enters the Amount
    And the user selects the Currency in 'From' field
    And the user selects the Currency in 'To' field
    And click on Convert button
    Then the converted value should be read and display


