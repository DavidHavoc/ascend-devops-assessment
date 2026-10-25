# Candidate Notes

_Fill this in as you work. Bullet points are fine._

## Approach
-
1.run the tests that are already avaliable and see the results

## Problems I found
- Store.list_appointments accepts it and include_cancelled igonres it . the route passes flase, but the cnaclled records appear 
- (security) debugf defualt on , ROS uses a wildcard origin and with credentials set to True, unused settings SECRET token and database_url, API kets
- .env was not ignored
- in appointments.py in def list_appointments it was exposing data that may have been sensitve logger.debug("Returning %d appointments", items)
- (operational)
- DOCKERFILE -- the started image compied the checkout before dteh dependecy, was runnign as root, did not have a health check, uvicorn was not requredid,
- missing dockerignore
- missing CI
- PostgreSQL is configured but not actually used.

## What I fixed vs. left (and why)
-added cancellation flag to storage while perserving the old logic of date filerign and safed cancallations 
- added tests for untested behaviors
    Calling list_appointments() without a date: the existing cancellation test only covers date-filtered results.
Passing include_cancelled=True: the API never exercises this branch, so it should be tested directly against the store.
Ensuring filtering removes only cancelled appointments, without dropping other statuses.
- i put debug on off defualt
-i turned of the credentials for CORS
- and i left unused API_KEY and SECRET_TOKEN, because maybe they are planned for the future and same goes with DATABASE i jsut dont have enough inforamtion to make that changes
- added .env to .gitignore
-  logger.debug("Returning %d appointments", items) -- > logger.debug("Returning %d appointments", len(items))
- dockerfile -
    Uses python:3.13-slim instead of the full image.
    Installs only requirements.txt; pytest, Ruff, and HTTPX are not installed.
    Copies only app/ and data/.
    Runs as the unprivileged app user.
    Preserves dependency-install build caching.
    Disables pip cache and Python bytecode files.
    Adds a /health container health check.
- added dockerigonre
- removed docker compose + postgre

## How I used my tools / AI
- (what I asked, what I accepted, what I rejected and why)
1. i asked to double check the problem if i was correct 
    prompt : "i have an error --FAILED tests/test_appointments.py::test_cancelled_excluded_by_default - AssertionError: assert 'cancelled' not in {'cancelled', 'completed', 'no_show'}- what part of the reqeuset handling is failing"
2. i asked to double check if my hunch was right 
    prompt pointing to storage.py "look at def list_appointments is the unused cancallation flag the problem o the failure , suggest the fix with minimal change"

    when i made sure its correct i ased for simplest fix and to apply it. 
        prompt : "apply the change "
3. asked to find untested behaviors, after it suggest a new code a revieed and said apply. thee tests pass
    prompt:whate behaviors are still untested , suggest test for cancellation flag , see what mistakes each test finds, and avoide dates or ids
4. the thinks i wanted to check out, because it didnat look right to my eye. i asked ai to do it - promnpt; " rg -n 'DEBS
UG|ALLOWED_ORIGINS' app and do rg -n "API_KEY =|SECRET_TOKEN|DATABASE_URL and follw these settings to there uses" 
    then it identided uses and wat and how it was used , then i gave a promt: "review the table u provided identify concrete concerns. recommend ad provide a small configuration for devug logging that is defaulting to off and explicit browser origins. dont add any code yet"
    after it rtecommend chagnes and i agreed i said to apply and the tests passed
5. for this  logger.debug("Returning %d appointments", items) i wanted to double check my thory and idea 
    prompt : "here @router.get("")
    def list_appointments(date: str | None = None):
    # Cancelled appointments should not appear in the default listing.
    items = store.list_appointments(date=date, include_cancelled=False)
    logger.debug("Returning appointments: %s", items)
    return items . i think the logger.debug is not optimal, idientify the simplest fix or if am wrong tell me"
6. the ddockerfile was looking quite blend i also felt uneasy with root and copy so i asked ai to invistage and teh napply the changes 
    prompt: " check dockerfile and check if its optimal, now its to simple, it optimaly should - no tests tools , no root , also check if uvicorn is requred in this app, check if it requres json "
7. i askedd to test dockerfile and checked if it worked
8. i asked ai to create a ci file that covers everything : push piull, docker, req, with read only permissions
    prompt: draft a githhub actions workflow for push and pull requests, becasue teh dockerfile is 3.13 use that isntall all req , do make test and make lint , also teh docker iamge , use simple permissons as posible read only"
9. investiage docker compose and postgre
10. asked to make sure my changed docker compose was correct and it runs
## What I'd do next with more time
-
