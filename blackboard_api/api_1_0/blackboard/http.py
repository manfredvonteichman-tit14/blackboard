""" Custom HTTP Response messages for the Blackboard API """

# Common request response messages
RESPONSE_400 = 'Input Payload Validation Failed'
RESPONSE_404 = 'Blackboard Not Found'
RESPONSE_500 = 'Internal Server Error'

# GET specific response messages
GET_RESPONSE_200 = 'Blackboard Read'
GET_RESPONSE_409 = 'Blackboard Empty'

# PUT specific response messages
PUT_RESPONSE_201 = 'Blackboard Created'
PUT_RESPONSE_409 = 'Blackboard Already Exists'

# POST specific response messages
POST_RESPONSE_201 = 'Blackboard Updated'

# PATCH specific response messages
PATCH_RESPONSE_200 = 'Blackboard Cleared'

# DELETE specific response messages
DELETE_RESPONSE_200 = 'Blackboard Deleted'
DELETE_ALL_RESPONSE_200 = 'All Blackboards Deleted'
