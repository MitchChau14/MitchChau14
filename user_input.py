import argparse
import os
from dacite import from_dict


from dataclasses import dataclass


@dataclass
class UserInputObj:
    debug: bool
    pathname: str
    flag_error: bool = False

    def __post_init__(self):
        if not os.path.exists(self.pathname):
            self.flag_error = True


class UserInput:
    def __init__(self):
        self.setup()

    def setup(self):
        # Setup Main Parser
        parserMain = argparse.ArgumentParser(prog="Flexible IO (FIO) Script")
        parserMain.add_argument(
            "--debug", action="store_true", help="Prints debug info."
        )
        parserMain.add_argument(
            "-p",
            "--pathname",
            required=True,
            help="Enter in the parent location of the files to be analyzed.",
        )

        # Parse arguments
        self.args = parserMain.parse_args()
        self.args = from_dict(data_class=UserInputObj, data=self.args.__dict__)