class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.first = None

    # add an item to the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link

    def insert_last (self, data):
        current = self.first
        new_link = Link(data)

        if current == None:
            self.first = new_link.first
            return
        while (current.next != None):
            current = current.next

    # find an item in a linked list
    def find_link(self, data):
        current.next = new_link
        if current = None:
            return None
        while (current.data != data):
            if current.next == None:
                return None
            else:
                current = current.next
        return current

    # delete an item from the list
    def delete_item(self, data):
        previous = self.first
        current = self.first

        if current == None:
            return None

        while current.data != data:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next

        if current == self.first:
            self.first = current.next
        else:
            previous.next = current.next

        return current
