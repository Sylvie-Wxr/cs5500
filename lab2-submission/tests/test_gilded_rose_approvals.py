import io
import sys

from approvaltests import verify
from texttest_fixture import main

def test_gilded_rose_approvals(resetItemsToV2=False):
    orig_sysout = sys.stdout
    try:
        fake_stdout = io.StringIO()
        sys.stdout = fake_stdout
        sys.argv = ["texttest_fixture.py", 30, resetItemsToV2]
        main()
        answer = fake_stdout.getvalue()
    finally:
        sys.stdout = orig_sysout

    verify(answer)
    
    print("All tests passed!")

if __name__ == "__main__":
    test_gilded_rose_approvals()
    # Comment the line above and uncomment the line below to run the v2 test
    # test_gilded_rose_approvals(True)