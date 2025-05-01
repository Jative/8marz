import threading

class StateMachine:
    def __init__(self):
        self.lock = threading.Lock()
        self.__data = {
            123: [0, 'Арина', 'Arina.mp4', 'BAACAgIAAxkDAAIBgWfLTKeH2yUFGIJqPGGwkL3QPGKwAAJYcAACtrdgSnKo5nIzxyS_NgQ'],
            123: [0, 'Ангелина', 'Angelina.mp4', 'BAACAgIAAxkDAAIBgmfLTKh6q2Eb93qB_GkPMHFJMUrTAAJZcAACtrdgSnJ06WIYb_uzNgQ'],
            123: [0, 'Анастасия', 'Anastasia.mp4', 'BAACAgIAAxkDAAIBg2fLTKnEN4SreHxtAzXOFcP9rN6BAAJacAACtrdgSlw4FudXV1uYNgQ'],
            123: [0, 'Владислава', 'Vladislava.mp4', 'BAACAgIAAxkDAAIBhGfLTKmYlfsKlzeuWEgCsUQdlMecAAJbcAACtrdgSk31YO_kJ7vNNgQ'],
            123: [0, 'Злата', 'Zlata.mp4', 'BAACAgIAAxkDAAIBhWfLTKvHr_w2kBt6ozg6oMpUmXbBAAKKZAACaVxgSup0_sm_EsyiNgQ'],
            123: [0, 'Мадина', 'Madina.mp4', 'BAACAgIAAxkDAAIBhmfLTKwWpyZzdaEiHStK90s58eunAAJccAACtrdgSuntEpXNfCxwNgQ'],
            123: [0, 'Кристина', 'Kristina.mp4', 'BAACAgIAAxkDAAIBh2fLTKw0jNENsXvtPXGTfRJgJwT4AAJecAACtrdgSlnpgLGvdmjpNgQ'],
            123: [0, 'Диана', 'Diana.mp4', 'BAACAgIAAxkDAAIBiGfLTK7MrzTjbP19Z638-V2GRQABNAACX3AAAra3YEpotaj0F3vGdDYE'],
            123: [0, 'Полина', 'Polina.mp4', 'BAACAgIAAxkDAAIBiWfLTK_taYV2N_9kJjtMHs1KvyBeAAJgcAACtrdgShhAPoFsLF06NgQ'],
            123: [0, 'Людмила', 'Lyudmila.mp4', 'BAACAgIAAxkDAAIBimfLTLAeRRmb_y5XPRQtzd6kTDZqAAJhcAACtrdgSp1NWFsICdZ4NgQ'],
            123: [0, 'Анна', 'Anna.mp4', 'BAACAgIAAxkDAAIBi2fLTLFv-w_TBs0uoDI2F-RVZJNpAAJicAACtrdgSnTAVUZDzml8NgQ'],
            123: [0, 'Ксения', 'Ksenia.mp4', 'BAACAgIAAxkDAAIBjGfLTLLa3wu4ExN9S8P11HCoqUNMAAJjcAACtrdgSspTvZ2dMrXFNgQ']
        }

    
    @property
    def state_dict(self):
        with self.lock:
            return self.__data
    
    @state_dict.setter
    def state_dict(self, value):
        with self.lock:
            self.__data = value
