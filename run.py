import threading
import subprocess
import webbrowser

# starts the python server and 'main.py' simultaneously to run as threads


def run_script(script_name):
    """
    Runs script as a subprocess

    Time Complexity:
    - Best Case: O(1).
    - Average Case: O(1).
    - Worst Case: O(1).
    """
    subprocess.run(["python", script_name])


if __name__ == "__main__":
    """
    threads both the 'app.py' and 'main.py' file to run simultaneously
    and automatically starts and opens the website

    Time Complexity:
    - Best Case: O(1).
    - Average Case: O(1).
    - Worst Case: O(1).
    """
    script1_thread = threading.Thread(target=run_script, args=("main.py",))
    script2_thread = threading.Thread(target=run_script, args=("app.py",))
    webbrowser.open('http://127.0.0.1:5000')

    script1_thread.start()
    script2_thread.start()

    script1_thread.join()
    script2_thread.join()

    print("Both scripts have finished executing.")