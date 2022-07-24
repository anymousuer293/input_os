from pathlib import Path
import os

class DisplayablePath(object):
    display_filename_prefix_middle = '├──'
    display_filename_prefix_last = '└──'
    display_parent_prefix_middle = '    '
    display_parent_prefix_last = '│   '

    def __init__(self, path, parent_path, is_last):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        root = Path(str(root))
        criteria = criteria or cls._default_criteria

        displayable_root = cls(root, parent, is_last)
        yield displayable_root

        children = sorted(list(path
                               for path in root.iterdir()
                               if criteria(path)),
                          key=lambda s: str(s).lower())
        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                yield from cls.make_tree(path,
                                         parent=displayable_root,
                                         is_last=is_last,
                                         criteria=criteria)
            else:
                yield cls(path, displayable_root, is_last)
            count += 1

    @classmethod
    def _default_criteria(cls, path):
        return True

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    def displayable(self):
        if self.parent is None:
            return self.displayname

        _filename_prefix = (self.display_filename_prefix_last
                            if self.is_last
                            else self.display_filename_prefix_middle)

        parts = ['{!s} {!s}'.format(_filename_prefix,
                                    self.displayname)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.display_parent_prefix_middle
                         if parent.is_last
                         else self.display_parent_prefix_last)
            parent = parent.parent

        return ''.join(reversed(parts))

user = input("Username: ")
password = input("Password: ")
if user == "admin" and password == "input":
    print("Hello Admin!")
    while True:
        inp = input("admin > ")
        if inp.split(" ")[0] == "say" and inp.split(" ")[1].startswith("\"") and inp.endswith("\""):
            print(inp[4:].removeprefix("\"").removesuffix("\""))
        elif inp.split(" ")[0] == "run":
            if inp.split(" ")[1] == "cryptography":
                import extensions.cryptography as crypto
                a = input("Message: ")
                crypto.msg = a
                print("1. Encrypt\n2. Decrypt")
                b = input("Your Choice: ")
                if b == "1":
                    crypto.run()
                elif b == "2":
                    crypto.run1()
            if inp.split(" ")[1] == "calculator":
                import extensions.calculator as calculator
                c = input("Expression: ")
                calculator.expression = c
                calculator.run()
        elif inp.split(" ")[0] == "tree":
            # With a criteria (skip hidden files)
            def is_not_hidden(path):
                return not path.name.startswith(".")
            paths = DisplayablePath.make_tree(
                    Path('doc'),
                    criteria=is_not_hidden
                )
            paths = DisplayablePath.make_tree(Path('input_os'))
            for path in paths:
                print(path.displayable())
        elif inp.split(" ")[0] == "makefile":
            filename = input("Filename: ")
            with open("input_os/files/"+filename, "x"):
                pass
        elif inp.split(" ")[0] == "replacefilecontent":
            filename = input("Filename: ")
            content = input("Content: ")
            with open("input_os/files/"+filename, "w") as f:
                f.write(content)
        elif inp.split(" ")[0] == "writefile" and inp.split(" ")[1] == "newline":
            filename = input("Filename: ")
            content = input("Content: ")
            with open("input_os/files/"+filename, "a") as f:
                f.write("\n"+content)
        elif inp.split(" ")[0] == "deletefile":
            filename = input("Filename: ")
            yn = input("Are you sure? (y/n): ")
            if yn == "y":
                os.remove("input_os/files/"+filename)
            elif yn == "n":
                pass
        elif inp.split(" ")[0] == "deletefile" and inp.split(" ")[1] == "line":
            filename = input("Filename: ")
            lineno = input("Line Number: ")
            yn = input("Are you sure? (y/n): ")
            if yn == "y":
                os.remove("input_os/files/"+filename)
            elif yn == "n":
                pass
        elif inp.split(" ")[0] == "readfile":
            filename = input("Filename: ")
            print(open("input_os/files/"+filename, "r").read())