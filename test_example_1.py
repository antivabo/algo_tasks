SEARCH_DEEP = 2


class Person:
    def __init__(self, name):
        self.name = name
        self.friends = set([])

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def add_friend(self, friend, **kwargs):
        if '__final' not in kwargs or not kwargs['__final']:
            friend.add_friend(self, __final=True)
        self.friends.add(friend)

    def friends_of_friends(self, **kwargs):
        results = set([])
        if '__relative_root' not in kwargs or not ['__relative_root']:
            __relative_root = self
        else:
            __relative_root = kwargs['__relative_root']

        if '__deep' not in kwargs or not kwargs['__deep']:
            __deep = SEARCH_DEEP
        else:
            __deep = kwargs['__deep']

        if __deep <= 1:
            return self.friends.difference({__relative_root})

        for friend in self.friends.difference({__relative_root}):
            if __deep < SEARCH_DEEP:
                results.add(friend)
            results.update(friend.friends_of_friends(__relative_root=self, __deep=__deep - 1))
        return results


LEVEL1_COUNT = 2
LEVEL2_COUNT = 2
LEVEL3_COUNT = 1
LEVEL4_COUNT = 1


def prepare_test_case():
    root_person = Person('Root Person')
    """ Prepare test case"""
    for i in range(LEVEL1_COUNT):
        person_l1 = Person('Person level 1 - %s' % i)
        for j in range(LEVEL2_COUNT):
            person_l2 = Person('Person level 2 - %s-%s' % (i, j))
            person_l1.add_friend(person_l2)
            for k in range(LEVEL3_COUNT):
                person_l3 = Person('Person level 3 - %s-%s-%s' % (i, j, k))
                person_l2.add_friend(person_l3)
                for n in range(LEVEL4_COUNT):
                    person_l4 = Person('Person level 4 - %s-%s-%s-%s' % (i, j, k, n))
                    person_l3.add_friend(person_l4)
        root_person.add_friend(person_l1)
    return root_person


def test_mutual_friendship(root_person):
    """ Test that friendship is mutual """
    for person_l1 in root_person.friends:
        for friend in person_l1.friends:
            print friend
        assert root_person in person_l1.friends


def test_friends_of_friends(root_person):
    """ Test that we have required amount of friends of friends,
    also check that our friends not in friends of friends set"""
    global SEARCH_DEEP

    """ Firstly test as defined in task description 
        with search deep 2"""
    SEARCH_DEEP = 2
    assert len(root_person.friends_of_friends()) == LEVEL1_COUNT * LEVEL2_COUNT
    assert not root_person.friends.intersection(root_person.friends_of_friends())

    print 'SEARCH_DEEP %s' % SEARCH_DEEP
    for friend in sorted(root_person.friends_of_friends(), key=lambda x: x.name):
        print friend

    """ Now lets make task a little bit wider and test with arbitrary search deep,
        for instance with search deep 3 """
    SEARCH_DEEP = 3
    assert len(root_person.friends_of_friends()) == LEVEL1_COUNT * LEVEL2_COUNT + \
                                                    LEVEL1_COUNT * LEVEL2_COUNT * LEVEL3_COUNT
    assert not root_person.friends.intersection(root_person.friends_of_friends())

    print 'SEARCH_DEEP %s' % SEARCH_DEEP
    for friend in sorted(root_person.friends_of_friends(), key=lambda x: x.name):
        print friend


if __name__ == '__main__':
    test_mutual_friendship(prepare_test_case())
    test_friends_of_friends(prepare_test_case())