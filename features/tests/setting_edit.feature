Feature: Test Scenarios for Search functionality of soft.reelly page

  Scenario: User login main page functionality
    Given Open soft reelly main page
    And Login to the page
    Then Click on continue button
    And Click on settings open
    And Click on Edit profile option
    When Enter some test information in the input fields
    Then Click on Save changes
    And Check the right information is present in the input fields
    And Click on Close