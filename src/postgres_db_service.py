#!/usr/bin/env python3
import dataset
from concurrent import futures
import os
import grpc
import time

from skillitor.core.api import skillitor_pb2, skillitor_pb2_grpc


class SkillitorQueryHandler(skillitor_pb2_grpc.SkillitorQueryServicer):
    def __init__(self) -> None:
        super().__init__()
        self.config = {
            'hostname': os.getenv('DB_HOSTNAME', 'localhost'),
            'username': os.getenv('DB_USERNAME', 'postgres'),
            'password': os.getenv('DB_PASSWORD', ''),
            'port': os.getenv('DB_PORT', 5432),
            'db_name': os.getenv('DB_NAME', 'skillator'),
        }

        if self.config['password']:
            conn_string = 'postgresql://{username}:{password}@{hostname}:{port}/{db_name}'.format(
                **self.config)
        else:
            conn_string = 'postgresql://{username}@{hostname}:{port}/{db_name}'.format(
                **self.config)
        print("DB connection string: " + conn_string)
        self.db = dataset.connect(conn_string)
        print("Connected to Postgres DB")

    def SetSkills(self, request: skillitor_pb2.SkillAssociation, context):
        print("Received a call to SetSkills")
        try:
            user_table = self.db['user']
            user_table.upsert(dict(email=str(request.user_email).lower()), ['email'])
            # Get the user that we just inserted or updated
            user = user_table.find_one(email=request.user_email.lower())

            skill_associations = self.db['skill_associations']
            for skill in request.skills:
                skill_associations.upsert(dict(user_id=user['id'],
                                               skill_name=skill.skill_name.lower(),
                                               skill_level=skill.skill_level),
                                          ['user_id', 'skill_name'])
        except Exception as e:
            print("Caught an exception")
            return skillitor_pb2.Acknowledgement(success=False, error_msg=str(e))

        return skillitor_pb2.Acknowledgement(success=True)

    def UnsetSkills(self, request: skillitor_pb2.SkillAssociation, context):
        print("Received a call to UnsetSkills")
        try:
            user_table = self.db['user']
            user_table.find_one(email=str(request.user_email).lower())
            # Get the user that we just inserted or updated
            user = user_table.find_one(email=request.user_email.lower())
            if user is None:
                print('Not removing skills for non-existing user ' + request.user_email.lower())
            else:
                print("Found user ID {} for {}".format(user['id'], request.user_email.lower()))

                skill_associations = self.db['skill_associations']
                skills_to_remove = tuple(skill.skill_name.lower() for skill in request.skills)
                print("skills_to_remove type:{}, value{}".format(
                    type(skills_to_remove), skills_to_remove
                ))
                skill_associations.delete(skill_name=skills_to_remove, user_id=user['id'])
        except Exception as e:
            print("Caught an exception: " + str(e))
            return skillitor_pb2.Acknowledgement(success=False, error_msg=str(e))

        return skillitor_pb2.Acknowledgement(success=True)

    def FindSkills(self, request: skillitor_pb2.FindSpec, context):
        print("Received a call to FindSkills")
        try:
            search_list = tuple(skill.skill_name.lower() for skill in request.skill_list)
            print("Searching for skills: " + str(search_list))
            skill_associations = self.db['skill_associations']
            db_sa_matches = skill_associations.find(skill_name=search_list)

            # matching_user_emails = []
            matching_user_with_skills = {}
            for db_result in db_sa_matches:
                print("Looking at result: " + str(db_result))
                user_table = self.db['user']
                user = user_table.find_one(id=db_result['user_id'])
                print('Looked up user: ' + str(user))
                if user is None:
                    print("Error looking up user ID")
                    yield None
                if user['email'] not in matching_user_with_skills:
                    matching_user_with_skills[user['email']] = []
                ss = skillitor_pb2.SkillSpec(skill_name=db_result['skill_name'],
                                             skill_level=db_result['skill_level'])
                matching_user_with_skills[user['email']].append(ss)

            if request.find_method == 'any':
                for user_email, skills in matching_user_with_skills.items():
                    print("Found user {} with at least one matching skill {}".format(
                        user_email, [(s.skill_name, s.skill_level) for s in skills]))
                    sa = skillitor_pb2.SkillAssociation(user_email=user_email, skills=skills)
                    yield sa
            elif request.find_method == 'all':
                for user_email, skills in matching_user_with_skills.items():
                    user_skill_names = set([s.skill_name for s in skills])
                    print("List of skills for {}: {}".format(user_email, user_skill_names))
                    if set(search_list).issubset(user_skill_names):
                        print("Found user {} with all matching skills {}".format(
                            user_email, [(s.skill_name, s.skill_level) for s in skills]))
                        sa = skillitor_pb2.SkillAssociation(user_email=user_email, skills=skills)
                        yield sa
                yield None
            else:
                print("THIS SHOULD NEVER HAPPEN. AIEEEEE!")
                yield None
        except Exception as e:
            print("Caught an exception: " + str(e))
            yield None


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    skillitor_pb2_grpc.add_SkillitorQueryServicer_to_server(
        SkillitorQueryHandler(), server)
    listen_port = os.getenv('LISTEN_PORT', '50051')
    server.add_insecure_port('[::]:' + listen_port)
    server.start()
    print("Listening on port " + listen_port)

    # The server code above runs asynchronously, so we need to do a sleep loop
    # to avoid exiting.
    while True:
        time.sleep(10)
        # Time passes. If only we had something useful to do.


if __name__ == '__main__':
    serve()
