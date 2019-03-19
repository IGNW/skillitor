#!/usr/bin/env python3
import grpc

from skillitor.core.api import skillitor_pb2, skillitor_pb2_grpc
from skillitor.core import skills


# We're going to send some test messages and then quit.
# For production, we'll need to use the CLI code or otherwise accept
# command continuously.
channel = grpc.insecure_channel('127.0.0.1:50051')
stub = skillitor_pb2_grpc.SkillitorQueryStub(channel)

# Refer to the .proto to know what are the components of each message type
user_id = 'user@example.com'
kung_fu_is_strong = skillitor_pb2.SkillSpec(skill_name="Kung-fu", skill_level=skills.SkillLevel.ADVANCED)
golang_is_weak = skillitor_pb2.SkillSpec(skill_name="Golang", skill_level=skills.SkillLevel.BEGINNER)
skills = [kung_fu_is_strong, golang_is_weak]
sa = skillitor_pb2.SkillAssociation(user_id=user_id, skills=skills)
response = stub.SetSkills(sa)
print("Sent a SetSkills message, got response type: {}. "
      "String representation: {}".format(type(response), response))

response = stub.UnsetSkills(sa)
print("Sent a UnsetSkills message, got response type: {}. "
      "String representation: {}".format(type(response), response))

response = stub.FindSkills(kung_fu_is_strong)
print("Sent a FindSkills message, got response type: {}. "
      "String representation: {}".format(type(response), response))
