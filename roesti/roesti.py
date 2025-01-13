import hashlib, os, typer
from typing_extensions import Annotated
import rich.progress 

BUFFER_SIZE = 65536

hash_types = [
    "md4",
    "md5",
    "sha1",
    "sha256",
    "sha512"
]

modes = [
    "Compare Hashes",
    "Generate File Hash"
]

# Roesti application instance
app = typer.Typer()

def compare_hash(digest: str, gen_digest: str) -> None:
    print("==== Comparing Hash ====")
    print(f"Comparing:\n{digest}\n{gen_digest}\n")
    if digest == gen_digest:
        print("Match success! Both hashes are the same.")
    else:
        print("Both hashes are different.")

def get_hash_algo_mode() -> int:
    mode_index = input("Selecting hash option: ")
    while not mode_index.isdigit():
        print(">>>> Invalid input. Please enter the hash mode index e.g. 1")
        mode_index = input("Selecting hash option: ")
    print()
    return int(mode_index)

def select_mode() -> str:
    mode = input("Selecting mode: ")
    while not mode.isdigit():
        print(">>>> Invalid input. Please enter the mode index e.g. 1")
        mode = input("Selecting mode: ")
    print()
    return mode

def configure_file_path() -> str:
    file_path = input(r"File path: ").strip(" \"'")
    while not os.path.exists(file_path):
        print(">>>> File path is not valid. Please try again.")
        file_path = input("File path: ").strip(" \"'")
    print()
    return file_path

def get_digest() -> str:
    digest = input("Enter hash: ").strip().lower()
    print()
    return digest

@app.command()
def generate_file_hash(path: Annotated[str, typer.Argument(help="File path")], hash_type: Annotated[str, typer.Argument(help="Hash type e.g. md5 or sha256")]) -> str:
    """
    Generate hash digest (of the specified type) from provided file path.\n
    >>>> IMPORTANT: Only files and ZIP files are supported.
    """   
    print("+++ Generating File Hash from Path")
    digest = hashlib.new(hash_type)
    try:
        with rich.progress.open(path, 'rb') as f:
            data = f.read(BUFFER_SIZE)
            while data:
                digest.update(data)
                data = f.read(BUFFER_SIZE)
            f.close()
    except PermissionError as e:
        print()
        print(e)
        print(">>>> Please check file permissions and ensure that the path target is a file, not a folder.")
    else:
        print()
        return digest.hexdigest()

@app.command()
def display_hash_modes() -> None:
    """
    Display list of hash modes
    """
    for i, mode in enumerate(modes):
        print(f"[ {i+1} ] {mode}")
    print()

@app.command()
def display_hash_types() -> None:
    """
    Display list of available hash types
    """
    for i, hash in enumerate(hash_types):
        print(f"[ {i+1} ] {hash}")
    print()

@app.command()
def roesti():
    """
    Use the roesti command to use the roesti tool
    """
    print("File hash modes:")
    display_hash_modes()

    mode = select_mode()
    file_path = configure_file_path()

    if mode == "1":
        print("==== Compare Hash Mode ====")
        print("Comparing with Hash Type:")
        display_hash_types()
        
        hash_mode_index = get_hash_algo_mode()
        hash_digest = get_digest()
        gen_digest = generate_file_hash(file_path, hash_types[hash_mode_index -1])
        compare_hash(hash_digest, gen_digest)

    elif mode == "2":
        print("==== Generate Hash Mode ====")
        print("Select Hash Type:")
        display_hash_types()
        hash_mode_index = get_hash_algo_mode()

        gen_digest = generate_file_hash(file_path, hash_types[hash_mode_index -1])
        print(gen_digest)
