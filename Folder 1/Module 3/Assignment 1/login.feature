Feature: SauceDemo Login

  Scenario: Successful login
    Given I open the SauceDemo website
    When I enter valid username and password
    And I click the login button
    Then I should be logged in successfully