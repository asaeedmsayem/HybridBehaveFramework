Feature: Verify Login Page

  Background:
    Given Launch the browser and open the app

  Scenario: HomePage Verification
    Then Verify page title
    And Quit the browser

Scenario: Verify Login Functionality
  When Enter login credential
  And Click login button
  Then Verify the page title and take screenshot
  And Close the app