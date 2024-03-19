# 导入API脚本
from audio_processing_api import api_script

def test_api():
    # 测试音频文件路径
    audio_file_path = "/wavs/No1/"

    # 调用API脚本
    api_response = api_script(audio_file_path)

    # 打印API响应
    print(api_response)

# 运行测试函数
test_api()