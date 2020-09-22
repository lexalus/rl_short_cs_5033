from nim import Player

class HumanPlayer(Player):
    """A Nim player that makes moves based on user input."""
    def move(self, heaps, misere):
        print("Heaps:", ' '.join(str(heap) for heap in heaps))
        heap_index = self.get_heap_index(heaps)
        num_remove = self.get_num_remove(heaps[heap_index])
        return heap_index, num_remove

    def won(self):
        print("Congratulations, you won!")

    def lost(self):
        print("Sorry, you lost.")

    def get_heap_index(self, heaps):
        choices = [str(choice) for choice in self.heap_choices(heaps)]
        while True:
            heap_index = input("Enter heap index: ").strip()
            if heap_index in choices:
                break
            print("Invalid input. Choices:", *choices)
        return int(heap_index)

    def get_num_remove(self, heap_size):
        choices = [str(choice) for choice in range(1, heap_size + 1)]
        while True:
            num_remove = input("Enter number to remove: ").strip()
            if num_remove in choices:
                break
            print("Invalid input. Choices:", *choices)
        return int(num_remove)