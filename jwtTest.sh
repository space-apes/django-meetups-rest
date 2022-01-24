#!/usr/bin/bash
#script to use curl to retrieve admin JWT tokens and request an endpoint from api

#arg1 is username
#arg2 is password
#arg3 is http method 
#arg4 is endpoint (EX: /users/)
#arg5 is optional json string to send (WRAP IN DOUBLE QUOTES)

if [ $# != 5 ]; then
	echo "usage is ./jwtTest.sh username password http_method endpoint jsonString"
	exit 1
fi

tokenResponse=$(curl \
		-q \
		-X POST \
		-H "Content-type: application/json" \
		-d '{"username":"'$1'", "password":"'$2'"}' \
		http://localhost:62231/api/token/)

#-d '{"username":"admin", "password":"password"}' \
#printf "\n"
#printf "\n"
#printf "\n"

accessToken=$(echo $tokenResponse | sed 's/.*access\":\"\(.*\)\".*/\1/')
refreshToken=$(echo $tokenResponse | sed 's/^.*refresh\":\"\(.*\)\",.*/\1/')


#printf "TOKEN RESPONSE:\n$tokenResponse\n"

#printf "ACCESS TOKEN:\n$accessToken\n"
#printf "REFRESH TOKEN:\n$refreshToken\n"


curl \
	     -X $3\
	     -H  "Authorization: Bearer ${accessToken}"\
	     -d $5\
	     "http://localhost:62231$4"
