Issue Summary

From 6:26 PM to 7:58 PM PT, requests to most Spam Filter APIs resulted in 500 error response messages.All customers could not use Spam Filter website properly.The root cause was the result of bad security configuration in the website.

Timeline (all times Pacific Time)
6:19 PM: security Configuration push begins
6:26 PM: Outage begins
6:26 PM: Pagers alerted teams
6:54 PM: Trying to change security configuration
7:15 PM: Successful change of the security configuration
7:19 PM: Server restarts begin
7:58 PM: 100% of traffic back online
Root Cause and Resolution and recovery
At 6:19 PM PT,  a security configuration change was inadvertently released to our production environment without first being released to the testing environment.  The security configuration was in the front end part which is vulnerable to any attack like sql 
injection which will cause a problem in the database and the servers will not be able to work properly. The solution for that problem is to change the place of the security verification configuration from frontend to backend.
Corrective and Preventative Measures
In recent days we had a problem in the database and we did not know what was the cause of it. we discovered it was happening because of the security verification configuration in the frontend. It was giving any one ability to miss up with the database. there are some step which should be  followed to prevent occuring that problem again:
All security verification configuration should be in the backend part not in the front end part.
Our system should be tested with different security tests to know how our system deals with those cases and also discover any shortage in our system during the development process. 

