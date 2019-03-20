#!/usr/bin/env python3
from concurrent import futures
import grpc
import time

from skillitor.core.api import skillitor_pb2, skillitor_pb2_grpc


class SkillitorQueryHandler(skillitor_pb2_grpc.SkillitorQueryServicer):
    def SetSkills(self, request, context):
        print("Got a request to SetSkills. Request type: {}. "
              "String representation: {}".format(type(request), request))
        return skillitor_pb2.Acknowledgement(success=True)

    def UnsetSkills(self, request, context):
        print("Got a request to UnsetSkills. Request type: {}. "
              "String representation: {}".format(type(request), request))
        return skillitor_pb2.Acknowledgement(success=True)

    def FindSkills(self, request, context):
        print("Got a request to FindSkills. Request type: {}. "
              "String representation: {}".format(type(request), request))
        return skillitor_pb2.Acknowledgement(success=True)

    def RawCommand(self, request, context):
        print("Got a request to RawCommand. Request type: {}. "
              "String representation: {}".format(type(request), request))
        return skillitor_pb2.RawResponse(text="Real response will go here.")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    skillitor_pb2_grpc.add_SkillitorQueryServicer_to_server(
        SkillitorQueryHandler(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Listening on port 50051")

    # The server code above runs asynchronously, so we need to do a sleep loop
    # to avoid exiting.
    while True:
        time.sleep(10)
        # Time passes. If only we had something useful to do.


if __name__ == '__main__':
    serve()
