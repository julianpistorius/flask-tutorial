Feature: Test basic home page

  Background:
    Given "Andrew" as the persona

  Scenario: Just see if the the home page is up.
    When I go to home
    Then I should see "Hi, Adam!"