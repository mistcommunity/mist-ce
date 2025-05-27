@clouds-add-2
Feature: Add second-tier clouds

  Background:
    Given I am logged in to mist
#    Then I expect for "addBtn" to be clickable within max 20 seconds

  @cloud-add
  Scenario Outline: Add cloud for multiple providers
    When I click the fab button in the "dashboard" page
    Then I expect the "Cloud" add form to be visible within max 5 seconds
    When I select the "<provider>" provider
    And I wait for 3 seconds
    Then I expect the field "Name" in the cloud add form to be visible within max 4 seconds
    When I use my "<provider>" credentials
    And I focus on the button "Add Cloud" in the "cloud" add form
    And I click the button "Add Cloud" in the "cloud" add form
    And I wait for the navigation menu to appear
    And I scroll the clouds list into view
    Then the "<provider>" provider should be added within 120 seconds


    Examples: Providers
    | provider                      |
    | IBM Cloud                     |
    | OnApp                         |
    | Openstack                     |
    | LXD                           |

  @AWS-add
  Scenario: Add AWS
    When I click the fab button in the "dashboard" page
    Then I expect the "Cloud" add form to be visible within max 5 seconds
    When I select the "Amazon Web Services" provider
    And I wait for 3 seconds
    Then I expect the field "Name" in the cloud add form to be visible within max 4 seconds
    When I use my "Amazon Web Services No Images" credentials
    And I focus on the button "Add Cloud" in the "cloud" add form
    Then I click the button "Add Cloud" in the "cloud" add form
    And I wait for the navigation menu to appear
    And I scroll the clouds list into view
    Then the "Amazon Web Services" provider should be added within 120 seconds

  @cloud-edit-creds
  Scenario: AWS cloud added in the beginning, does not have access to list images (DenyDescribeImages policy in aws), whereas the seconds one has (EC2FullAccess)
    When I visit the Images page
    And I search for "ubuntu-focal-20.04"
    Then "ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-20210223" image should be absent within 10 seconds
    Then I visit the Home page
    And I wait for the dashboard to load
    When I open the cloud page for "Amazon Web Services"
    Then I expect the "cloud" page to be visible within max 10 seconds
    When I click the "Edit Credentials" action button in the "cloud" page
    Then I expect the "Edit Credentials" dialog to be open within 4 seconds
    When I use my second AWS credentials
    And I wait for 1 seconds
    When I click the "Edit Credentials" button in the "Edit Credentials" dialog
    And I wait for 3 seconds
    And I visit the Images page
    And I wait for 2 seconds
    And I clear the search bar
    And I wait for 2 seconds
    And I search for "ubuntu-focal-20.04"
    Then "ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-20210223" image should be present within 20 seconds
