from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

PRJPATH = os.environ.get("PRJPATH")

def match():
    return None

if __name__ == '__main__':

    df = match()
