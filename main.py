from json import load

from keyboard import add_hotkey, wait, write


#test commit
class HotkeysLoader:
    @staticmethod
    def load(file_path: str) -> dict:
        with open(file=file_path, encoding='UTF-8') as file:
            hotkeys = load(fp=file)

        return hotkeys


class AutoHotkey:
    file_path: str = 'bin/hotkeys.json'
    hotkeys: dict = HotkeysLoader.load(file_path=file_path)

    @classmethod
    def main(cls) -> None:
        for key, string in cls.hotkeys.items():
            add_hotkey(hotkey=key, callback=write, args=(string,))

        wait()


if __name__ == '__main__':
    AutoHotkey.main()
