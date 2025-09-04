import sys
sys.path.insert(1,"/workspaces/BradleysStrings-python/src/BradleysStrings/")
import BradleysStrings
def test_1():
    print("Testing insert(\"aaaaa\",2,\"b\")!")
    print(BradleysStrings.insert("aaaaa",2,"b"))
def test_2():
    print("Testing replaceatpos(\"aaaaa\",2,\"b\")!")
    print(BradleysStrings.replaceatpos("aaaaa",2,"b"))


test_1()
test_2()