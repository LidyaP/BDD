Feature: Check if i can create my first Workspace
  @T3   @positiveTesting
    Scenario: I want to close the offer for Microsoft Intro app
      Given I am logged into my account
      When I see the offer
      When I click on x button
      Then The offer is closed
