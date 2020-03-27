from operator import index


class FakeMuscleActions(object):
    def __init__(self, nameinput):
        self.nameinput= nameinput
        pass


fake_muscle_actions_names_list = ['object1', 'object2', 'object3', 'object4']
fake_muscle_actions = {}
for fake_muscle_action_name in fake_muscle_actions_names_list:
    fake_muscle_actions[fake_muscle_action_name] = FakeMuscleActions('flsfkjhgosfd')

    print(type(fake_muscle_actions_names_list.index(fake_muscle_action_name)))
    print("type d'objet créé", type(fake_muscle_actions[fake_muscle_action_name]))
    print("nom objet créé", (fake_muscle_actions[fake_muscle_action_name]).__class__)


print(fake_muscle_actions)


# for name in ["object1", "object2", "object3"]:
#         d = {name: classname()}
#     print d[name]
