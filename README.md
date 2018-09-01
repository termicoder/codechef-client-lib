# codechef_client
CodeChef API to support different applications.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import codechef_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import codechef_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import codechef_client
from codechef_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: codechef_auth
codechef_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = codechef_client.ContestProblemsApi()
problem_code = 'problem_code_example' # str | Problem code of the problem, eg. SALARY
contest_code = 'contest_code_example' # str | Contest code of the contest, eg. PRACTICE, COOK97, JAN17
fields = 'fields_example' # str | Possible fields are- problemCode, author, problemName, languagesSupported, sourceSizeLimit,  dateAdded, challengeType, maxTimeLimit, successfulSubmissions, body, totalSubmissions, partialSubmissions, tags.  Multiple fields can be entered using comma. (optional)

try:
    # Get details of a problem.
    api_response = api_instance.contests_contest_code_problems_problem_code_get(problem_code, contest_code, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContestProblemsApi->contests_contest_code_problems_problem_code_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.codechef.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContestProblemsApi* | [**contests_contest_code_problems_problem_code_get**](docs/ContestProblemsApi.md#contests_contest_code_problems_problem_code_get) | **GET** /contests/{contestCode}/problems/{problemCode} | Get details of a problem.
*ContestsApi* | [**contests_contest_code_get**](docs/ContestsApi.md#contests_contest_code_get) | **GET** /contests/{contestCode} | Get contest details.
*ContestsApi* | [**contests_get**](docs/ContestsApi.md#contests_get) | **GET** /contests | Get the list of contests.
*CountriesApi* | [**country_get**](docs/CountriesApi.md#country_get) | **GET** /country | Get the list of countries on codechef.
*IDEApi* | [**ide_run_post**](docs/IDEApi.md#ide_run_post) | **POST** /ide/run | Runs a code submitted by user.
*IDEApi* | [**ide_status_get**](docs/IDEApi.md#ide_status_get) | **GET** /ide/status | Get status of submitted code.
*InstitutionsApi* | [**institution_get**](docs/InstitutionsApi.md#institution_get) | **GET** /institution | Get the list of institutions on codechef.
*LanguagesApi* | [**language_get**](docs/LanguagesApi.md#language_get) | **GET** /language | Get the list of languages on codechef.
*ProblemsApi* | [**problems_category_name_get**](docs/ProblemsApi.md#problems_category_name_get) | **GET** /problems/{categoryName} | Get the list of problems for given categoryName.
*RankingsApi* | [**rankings_contest_code_get**](docs/RankingsApi.md#rankings_contest_code_get) | **GET** /rankings/{contestCode} | Return ranklist for a particular contest.
*RatingsApi* | [**ratings_contest_type_get**](docs/RatingsApi.md#ratings_contest_type_get) | **GET** /ratings/{contestType} | Return ratinglist for a particular contest type.
*SetsApi* | [**sets_add_post**](docs/SetsApi.md#sets_add_post) | **POST** /sets/add | Adds set to the user&#39;s account to whom the access token being used belongs.
*SetsApi* | [**sets_delete_delete**](docs/SetsApi.md#sets_delete_delete) | **DELETE** /sets/delete | Deletes set from the user&#39;s account to whom the access token belongs.
*SetsApi* | [**sets_get**](docs/SetsApi.md#sets_get) | **GET** /sets/ | Get set details for logged in user
*SetsApi* | [**sets_members_add_post**](docs/SetsApi.md#sets_members_add_post) | **POST** /sets/members/add | Adds set members to an existing set of the user to whom the access token belongs.
*SetsApi* | [**sets_members_delete_delete**](docs/SetsApi.md#sets_members_delete_delete) | **DELETE** /sets/members/delete | Removes members belonging to a set.
*SetsApi* | [**sets_members_get_get**](docs/SetsApi.md#sets_members_get_get) | **GET** /sets/members/get | Get set details for particular sets of the logged in user
*SetsApi* | [**sets_update_put**](docs/SetsApi.md#sets_update_put) | **PUT** /sets/update | Updates set of the logged in user&#39;s account.
*SubmissionApi* | [**submissions_get**](docs/SubmissionApi.md#submissions_get) | **GET** /submissions/ | Get submissions for particular user, problemCode, result and year.
*SubmissionApi* | [**submissions_submission_id_get**](docs/SubmissionApi.md#submissions_submission_id_get) | **GET** /submissions/{submissionId} | Get details of a submission.
*TagsApi* | [**tags_problems_get**](docs/TagsApi.md#tags_problems_get) | **GET** /tags/problems | Get list of tags for a given problem.
*TodoApi* | [**todo_add_post**](docs/TodoApi.md#todo_add_post) | **POST** /todo/add | Adds a problem to todo list.
*TodoApi* | [**todo_delete_all_delete**](docs/TodoApi.md#todo_delete_all_delete) | **DELETE** /todo/delete/all | Deletes all the problems added to the todo list.
*TodoApi* | [**todo_delete_delete**](docs/TodoApi.md#todo_delete_delete) | **DELETE** /todo/delete/ | Deletes a problem added to the todo list.
*TodoApi* | [**todo_problems_get**](docs/TodoApi.md#todo_problems_get) | **GET** /todo/problems | Gets problems listed in todo.
*UsersApi* | [**users_get**](docs/UsersApi.md#users_get) | **GET** /users | Get the list of users maximum 20.
*UsersApi* | [**users_me_get**](docs/UsersApi.md#users_me_get) | **GET** /users/me | Fetches all the details of logged-in user.
*UsersApi* | [**users_username_get**](docs/UsersApi.md#users_username_get) | **GET** /users/{username} | Fetches all the details of a user.


## Documentation For Models

 - [AddSetMemberParameters](docs/AddSetMemberParameters.md)
 - [AddSetParameters](docs/AddSetParameters.md)
 - [AddTodoParameters](docs/AddTodoParameters.md)
 - [AllRanking](docs/AllRanking.md)
 - [City](docs/City.md)
 - [Contest](docs/Contest.md)
 - [ContestList](docs/ContestList.md)
 - [ContestProblem](docs/ContestProblem.md)
 - [ContestProblemsList](docs/ContestProblemsList.md)
 - [ContestWiseProblems](docs/ContestWiseProblems.md)
 - [Country](docs/Country.md)
 - [CountryList](docs/CountryList.md)
 - [Error](docs/Error.md)
 - [ErrorResult](docs/ErrorResult.md)
 - [ErrorResultErrors](docs/ErrorResultErrors.md)
 - [IDERun](docs/IDERun.md)
 - [IDEStatus](docs/IDEStatus.md)
 - [IdeRunSourceCode](docs/IdeRunSourceCode.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20010Result](docs/InlineResponse20010Result.md)
 - [InlineResponse20010ResultData](docs/InlineResponse20010ResultData.md)
 - [InlineResponse20010ResultDataContent](docs/InlineResponse20010ResultDataContent.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20011Result](docs/InlineResponse20011Result.md)
 - [InlineResponse20011ResultData](docs/InlineResponse20011ResultData.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20012Result](docs/InlineResponse20012Result.md)
 - [InlineResponse20012ResultData](docs/InlineResponse20012ResultData.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20013Result](docs/InlineResponse20013Result.md)
 - [InlineResponse20013ResultData](docs/InlineResponse20013ResultData.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20014Result](docs/InlineResponse20014Result.md)
 - [InlineResponse20014ResultData](docs/InlineResponse20014ResultData.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20017Result](docs/InlineResponse20017Result.md)
 - [InlineResponse20017ResultData](docs/InlineResponse20017ResultData.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse20019](docs/InlineResponse20019.md)
 - [InlineResponse2001Result](docs/InlineResponse2001Result.md)
 - [InlineResponse2001ResultData](docs/InlineResponse2001ResultData.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse20020](docs/InlineResponse20020.md)
 - [InlineResponse20020Result](docs/InlineResponse20020Result.md)
 - [InlineResponse20020ResultData](docs/InlineResponse20020ResultData.md)
 - [InlineResponse20020ResultDataContent](docs/InlineResponse20020ResultDataContent.md)
 - [InlineResponse20021](docs/InlineResponse20021.md)
 - [InlineResponse20022](docs/InlineResponse20022.md)
 - [InlineResponse20022Result](docs/InlineResponse20022Result.md)
 - [InlineResponse20022ResultContent](docs/InlineResponse20022ResultContent.md)
 - [InlineResponse20023](docs/InlineResponse20023.md)
 - [InlineResponse20023Result](docs/InlineResponse20023Result.md)
 - [InlineResponse20023ResultContent](docs/InlineResponse20023ResultContent.md)
 - [InlineResponse2002Result](docs/InlineResponse2002Result.md)
 - [InlineResponse2002ResultData](docs/InlineResponse2002ResultData.md)
 - [InlineResponse2002ResultDataContent](docs/InlineResponse2002ResultDataContent.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2003Result](docs/InlineResponse2003Result.md)
 - [InlineResponse2003ResultData](docs/InlineResponse2003ResultData.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2004Result](docs/InlineResponse2004Result.md)
 - [InlineResponse2004ResultData](docs/InlineResponse2004ResultData.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2005Result](docs/InlineResponse2005Result.md)
 - [InlineResponse2005ResultData](docs/InlineResponse2005ResultData.md)
 - [InlineResponse2005ResultDataContent](docs/InlineResponse2005ResultDataContent.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2006Result](docs/InlineResponse2006Result.md)
 - [InlineResponse2006ResultData](docs/InlineResponse2006ResultData.md)
 - [InlineResponse2006ResultDataContent](docs/InlineResponse2006ResultDataContent.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2007Result](docs/InlineResponse2007Result.md)
 - [InlineResponse2007ResultData](docs/InlineResponse2007ResultData.md)
 - [InlineResponse2007ResultDataContent](docs/InlineResponse2007ResultDataContent.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2008Result](docs/InlineResponse2008Result.md)
 - [InlineResponse2008ResultData](docs/InlineResponse2008ResultData.md)
 - [InlineResponse2008ResultDataContent](docs/InlineResponse2008ResultDataContent.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse2009Result](docs/InlineResponse2009Result.md)
 - [InlineResponse2009ResultData](docs/InlineResponse2009ResultData.md)
 - [InlineResponse2009ResultDataContent](docs/InlineResponse2009ResultDataContent.md)
 - [InlineResponse200Result](docs/InlineResponse200Result.md)
 - [InlineResponse200ResultData](docs/InlineResponse200ResultData.md)
 - [Institution](docs/Institution.md)
 - [Language](docs/Language.md)
 - [Problems](docs/Problems.md)
 - [RankList](docs/RankList.md)
 - [RankListProblemScore](docs/RankListProblemScore.md)
 - [Ranking](docs/Ranking.md)
 - [Rating](docs/Rating.md)
 - [RatingList](docs/RatingList.md)
 - [SetMembers](docs/SetMembers.md)
 - [Sets](docs/Sets.md)
 - [SetsaddResult](docs/SetsaddResult.md)
 - [SetsaddResultData](docs/SetsaddResultData.md)
 - [SetsupdateResult](docs/SetsupdateResult.md)
 - [SetsupdateResultData](docs/SetsupdateResultData.md)
 - [State](docs/State.md)
 - [Submission](docs/Submission.md)
 - [Tag](docs/Tag.md)
 - [TodoProblemDetails](docs/TodoProblemDetails.md)
 - [TodoaddResult](docs/TodoaddResult.md)
 - [TodoaddResultData](docs/TodoaddResultData.md)
 - [TododeleteResult](docs/TododeleteResult.md)
 - [TododeleteResultData](docs/TododeleteResultData.md)
 - [UpdateSetParameters](docs/UpdateSetParameters.md)
 - [User](docs/User.md)
 - [UserProblemStats](docs/UserProblemStats.md)
 - [UserSubmissionStats](docs/UserSubmissionStats.md)
 - [Users](docs/Users.md)


## Documentation For Authorization


## codechef_auth

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://api.codechef.com/oauth/authorize
- **Scopes**: 
 - **public**: public
 - **private**: private
 - **set**: set
 - **todo**: todo
 - **submission**: submission


## Author


