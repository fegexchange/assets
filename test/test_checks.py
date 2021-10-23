import unittest
import os
import re
import json
import cv2


def jsoncontain(directory):
    try:
        path = os.path.join(directory, "info.json")
        return os.path.exists(path)
    except FileExistsError:
        return False


def logopng(directory):
    try:
        path = os.path.join(directory, "logo.png")
        return os.path.exists(path)
    except FileExistsError:
        return False


def validateJSON(file):
    try:
        json.loads(file.read())
    except ValueError:
        return False
    return True


def validateFieldsPresentJson(file):
    content = json.loads(file.read())
    invalidFields = ""
    valid = True
    if not ("id" in content):
        invalidFields += "id "
        valid = False
    if not ("name" in content):
        invalidFields += "name "
        valid = False
    if not ("symbol" in content):
        invalidFields += "symbol "
        valid = False
    if not ("type" in content):
        invalidFields += "type "
        valid = False
    if not ("decimals" in content):
        invalidFields += "decimals "
        valid = False
    file.close()
    return valid, invalidFields


def validatePicturesize(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    height = img.shape[0]
    width = img.shape[1]
    if width != 256 or height != 256:
        return False
    return True


def checkCapitalisationOfDir(dirname):
    return re.search("(?=.*[a-z])(?=.*[A-Z])(^0x[A-Fa-f0-9]{40}$)", dirname)


def checkType(file, type):
    content = json.loads(file.read())
    verify = type == content["type"]
    file.close()
    return verify



def checkCapitalisationOfId(file, dirname):
    content = json.loads(file.read())
    verify = dirname == content["id"]
    file.close()
    return verify


class BSCChainTest(unittest.TestCase):
    dirBSCPath = "blockchains/smartchain/assets"

    def test_bscside(self):
        for directory in os.listdir(self.dirBSCPath):
            if re.search(r"\.", directory):
                continue
            with self.subTest(directory=directory):
                self.assertTrue(jsoncontain(os.path.join(self.dirBSCPath, directory)),
                                "{}: Needs a \"info.json\" file. Please check the name".format(directory))

                self.assertTrue(logopng(os.path.join(self.dirBSCPath, directory)),
                                "{}: Needs a \"logo.png\" file. Please check the name".format(directory))

                self.assertTrue(validateJSON(open(os.path.join(self.dirBSCPath, directory, "info.json"))),
                                "{}: has not a valid json format!".format(directory))
                validbool, failedFields = validateFieldsPresentJson(
                    open(os.path.join(self.dirBSCPath, directory, "info.json")))
                self.assertTrue(validbool,
                                "{}: Field {} was  not set".format(directory, failedFields))
                self.assertTrue(validatePicturesize(os.path.join(self.dirBSCPath, directory, "logo.png")),
                                "{} : Make sure that your logo.png is 256x256px".format(directory))
                self.assertTrue(checkCapitalisationOfDir(directory),
                                "{} : check for capitalisation of directory name".format(directory))
                self.assertTrue(
                    checkCapitalisationOfId(open(os.path.join(self.dirBSCPath, directory, "info.json")), directory),
                    "{} : ID field in json need to match the directory (check capitalisation)".format(directory))
                self.assertTrue(
                    checkType(open(os.path.join(self.dirBSCPath, directory, "info.json")), "BEP20"),
                    "{} : Symbol needs to be BEP20".format(directory))
                print("{} : passed all the tests".format(directory))


if __name__ == '__main__':
    unittest.main()
