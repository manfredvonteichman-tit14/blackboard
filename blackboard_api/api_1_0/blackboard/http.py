# Common request response
RESPONSE_400 = 'Input Payload Validation Failed'
RESPONSE_404 = 'Blackboard Not Found'
RESPONSE_500 = 'Internal Server Error'

# GET specific response
GET_RESPONSE_200 = 'Blackboard Read'
GET_RESPONSE_409 = 'Blackboard Empty'

# PUT specific response
PUT_RESPONSE_201 = 'Blackboard Created'
PUT_RESPONSE_409 = 'Blackboard Already Exists'

# POST specific response
POST_RESPONSE_201 = 'Blackboard Updated'
POST_RESPONSE_409 = 'Use PATCH /clear'
POST_RESPONSE_413 = 'Blackboard Message Payload Too Large'

# PATCH specific response
PATCH_RESPONSE_200 = 'Blackboard Cleared'  # 'Blackboard status successfully fetched.'

# DELETE specific response
DELETE_RESPONSE_200 = 'Blackboard Deleted'
