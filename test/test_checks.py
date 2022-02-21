import json
import os
import re
import unittest

import cv2

from bsc_schema import BscSchema


def get_content_from(fp, as_json=False):
    with fp as _point:
        return json.load(_point) if as_json else _point.read()


def check_path(directory, key):
    return os.path.exists(os.path.join(directory, key))


def jsoncontain(directory):
    return check_path(directory, "info.json")


def logopng(directory):
    return check_path(directory, "logo.png")


def validate_json(_file):
    return get_content_from(_file, as_json=True)


def validate_json_schema(filename):
    data = get_content_from(filename, as_json=True)
    schema = BscSchema()
    return schema.load(data), ...


def validate_picture_size(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    height = img.shape[0]
    width = img.shape[1]
    return width == 256 or height == 256


def check_capitalisation_of_dir(dirname):
    return re.search("(?=.*[a-z])(?=.*[A-Z])(^0x[A-Fa-f0-9]{40}$)", dirname)


def check_key(data, key, val):
    return data.get(key) == val


def check_type(_file, _type):
    content = json.loads(get_content_from(_file))
    return _type == content["type"]


def check_capitalisation_of_id(_file, dirname):
    content = get_content_from(_file, as_json=True)
    return dirname == content["id"]


class FilecheckTest(unittest.TestCase):
    def test_check_blockchains(self):
        dirs = os.listdir("./blockchains")
        self.assertTrue(len(dirs) == 2, "Not a valid blockchain")

    # check if blockchains name has assets in there
    def test_check_asset(self):
        dirs = os.listdir("./blockchains/smartchain")
        self.assertTrue(
            len(dirs) == 1,
            "asset should be the only repository allowed in smartchain folder",
        )
        dirs = os.listdir("./blockchains/ethereum")
        self.assertTrue(
            len(dirs) == 1,
            "asset should be the only repository allowed in ethereum folder",
        )

    def test_checkfiles(self):
        for root, dirs, files in os.walk(".", topdown=False):

            for name in files:
                if os.path.join(root, name) is None:
                    continue
                self.assertFalse(
                    re.search("(?=.*[a-z])(?=.*[A-Z])(^0x[A-Fa-f0-9]{40}$)", name)
                    and not re.search("assets(/|\\|)$", root),
                    os.path.join(root, name) + " is not in the right place",
                )

            for name in dirs:
                if root == ".":
                    self.assertFalse(
                        re.search("(?=.*[a-z])(?=.*[A-Z])(^0x[A-Fa-f0-9]{40}$)", name),
                        "Folder should not be in here",
                    )
                self.assertFalse(
                    re.search("(?=.*[a-z])(?=.*[A-Z])(^0x[A-Fa-f0-9]{40}$)", name)
                    and re.search("assets(/|\\|)$", root),
                    os.path.join(root, name) + " is not in the right place",
                )


class BSCChainTest(unittest.TestCase):
    dirBSCPath = "blockchains/smartchain/assets"

    def test_bscside(self):
        for directory in os.listdir(self.dirBSCPath):
            if re.search(r"(\.)|(native)", directory):
                continue
            with self.subTest(directory=directory):
                self.assertTrue(
                    jsoncontain(os.path.join(self.dirBSCPath, directory)),
                    '{}: Needs a "info.json" file. Please check the name'.format(
                        directory
                    ),
                )

                self.assertTrue(
                    logopng(os.path.join(self.dirBSCPath, directory)),
                    '{}: Needs a "logo.png" file. Please check the name'.format(
                        directory
                    ),
                )

                self.assertTrue(
                    validate_json(
                        open(os.path.join(self.dirBSCPath, directory, "info.json"))
                    ),
                    "{}: has not a valid json format!".format(directory),
                )
                validbool, failedFields = validate_json_schema(
                    open(os.path.join(self.dirBSCPath, directory, "info.json"))
                )
                self.assertTrue(
                    validbool,
                    "{}: Field {} was  not set".format(directory, failedFields),
                )
                self.assertTrue(
                    validate_picture_size(
                        os.path.join(self.dirBSCPath, directory, "logo.png")
                    ),
                    "{} : Make sure that your logo.png is 256x256px".format(directory),
                )
                self.assertTrue(
                    check_capitalisation_of_dir(directory),
                    "{} : check for capitalisation of directory name".format(directory),
                )
                self.assertTrue(
                    check_capitalisation_of_id(
                        open(os.path.join(self.dirBSCPath, directory, "info.json")),
                        directory,
                    ),
                    "{} : ID field in json need to match the directory (check capitalisation)".format(
                        directory
                    ),
                )
                self.assertTrue(
                    check_type(
                        open(os.path.join(self.dirBSCPath, directory, "info.json")),
                        "BEP20",
                    ),
                    "{} : Symbol needs to be BEP20".format(directory),
                )

    def test_only_two_files_in_folder(self):

        for root, dirs, files in os.walk(self.dirBSCPath, topdown=False):
            if root == self.dirBSCPath:
                continue
            self.assertTrue(len(dirs) == 0, "No dirs are allowed in " + root)
            self.assertTrue(len(files) == 2, "At most 2 files are allowed in " + root)


class ETHChainTest(unittest.TestCase):
    dirETHPath = "blockchains/ethereum/assets"

    def test_ethside(self):
        for directory in os.listdir(self.dirETHPath):
            if re.search(r"(\.)|(native)", directory):
                continue
            with self.subTest(directory=directory):
                self.assertTrue(
                    jsoncontain(os.path.join(self.dirETHPath, directory)),
                    '{}: Needs a "info.json" file. Please check the name'.format(
                        directory
                    ),
                )

                self.assertTrue(
                    logopng(os.path.join(self.dirETHPath, directory)),
                    '{}: Needs a "logo.png" file. Please check the name'.format(
                        directory
                    ),
                )

                self.assertTrue(
                    validate_json(
                        open(os.path.join(self.dirETHPath, directory, "info.json"))
                    ),
                    "{}: has not a valid json format!".format(directory),
                )
                validbool, failedFields = validate_json_schema(
                    open(os.path.join(self.dirETHPath, directory, "info.json"))
                )
                self.assertTrue(
                    validbool,
                    "{}: Field {} was  not set".format(directory, failedFields),
                )
                self.assertTrue(
                    validate_picture_size(
                        os.path.join(self.dirETHPath, directory, "logo.png")
                    ),
                    "{} : Make sure that your logo.png is 256x256px".format(directory),
                )
                self.assertTrue(
                    check_capitalisation_of_dir(directory),
                    "{} : check for capitalisation of directory name".format(directory),
                )
                self.assertTrue(
                    check_capitalisation_of_id(
                        open(os.path.join(self.dirETHPath, directory, "info.json")),
                        directory,
                    ),
                    "{} : ID field in json need to match the directory (check capitalisation)".format(
                        directory
                    ),
                )
                self.assertTrue(
                    check_type(
                        open(os.path.join(self.dirETHPath, directory, "info.json")),
                        "ERC20",
                    ),
                    "{} : Symbol needs to be BEP20".format(directory),
                )

    def test_only_two_files_in_folder(self):
        for root, dirs, files in os.walk(self.dirETHPath, topdown=False):
            if root == self.dirETHPath:
                continue
            self.assertTrue(len(dirs) == 0, "No dirs are allowed in " + root)
            self.assertTrue(len(files) == 2, "At most 2 files are allowed in " + root)


if __name__ == "__main__":
    unittest.main()
