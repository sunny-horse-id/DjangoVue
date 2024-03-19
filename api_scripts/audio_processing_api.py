import subprocess
import json
import os


def run_npm_dev(package_json_path):
    # 执行 npm 命令
    subprocess.Popen(["npm.cmd", "run", "dev"], cwd=os.path.dirname(package_json_path), stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)


def run_python_script(audio_file):
    # 这里你可以编写调用你的 Python 程序的逻辑
    # 比如，你可以传递音频信息作为参数给 Python 程序
    # 这里我们只是打印一条消息来模拟调用 Python 程序的过程
    print("Running Python script with audio info:", audio_file)

    # 构造调用test.py脚本的命令
    command = ["python3", "/home/test/EDGE/test.py", "--music_dir", f"{audio_file}", "--save_motions"]

    # 调用test.py脚本并传递参数
    subprocess.run(command)

    # 构造调用test.py脚本的命令
    command = ["python3", "/home/test/EDGE/SMPL-to-FBX/Convert.py"]

    # 调用test.py脚本并传递参数
    subprocess.run(command)


def process_audio(audio_file):
    # 在这里你可以添加处理音频文件的逻辑，比如上传到服务器、处理音频等
    # 在这个示例中，我们只是假装处理了音频文件并返回一个固定的网址

    # 运行 Python 程序
    run_python_script(audio_file)

    # 获取 package.json 文件路径
    package_json_path = "../frontend/package.json"

    # 运行 npm 命令
    run_npm_dev(package_json_path)

    processed_url = "http://localhost:5173/three"
    return processed_url


def api_script(audio_file_path):
    # 处理音频文件
    processed_url = process_audio(audio_file_path)

    # 构造JSON响应
    response_data = {
        "processed_url": processed_url
    }

    # 返回JSON格式的响应
    return json.dumps(response_data)
