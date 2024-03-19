from django.shortcuts import render

# Create your views here.

# 在您的 Django 应用中的 views.py 文件中

from django.http import JsonResponse
def handle_upload_request(request):
    if request.method == 'POST':
        # 在这里处理您的上传逻辑
        # 假设您已经处理完上传逻辑，并且生成了一个链接
        generated_link = "test"  # 临时使用示例链接，请替换为您实际生成的链接

        # 构造要返回的数据，这里假设您返回一个 JSON 对象
        response_data = {
            'code': 1,
            'link': generated_link,
            'msg': "上传成功！c",
        }

        # 使用 JsonResponse 将数据转换为 JSON 格式并返回给前端
        return JsonResponse(response_data, status=200)
    else:
        # 如果请求方法不是 POST，则返回错误信息
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=400)