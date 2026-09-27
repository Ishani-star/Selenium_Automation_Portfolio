Feature: SauceDemo Data Driven Login

  Scenario Outline: Login with different credentials
    Given I open the SauceDemo website
    When I enter username "<username>" and password "<password>"
    And I click the login button
    Then the login result should be "<result>"

    Examples:
      | username                | password     | result  |
      | standard_user           | secret_sauce | success |
      | locked_out_user         | secret_sauce | locked |
      | invalid_user            | wrong_pass   | invalid |