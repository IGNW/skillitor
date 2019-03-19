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
response = stub.SetSkill(sa)
print("Sent a SetSkill message, got response type: {}. "
      "String representation: {}".format(type(response), response))

response = stub.UnsetSkill(sa)
print("Sent a UnsetSkill message, got response type: {}. "
      "String representation: {}".format(type(response), response))

response = stub.FindSkill(kung_fu_is_strong)
print("Sent a FindSkill message, got response type: {}. "
      "String representation: {}".format(type(response), response))
