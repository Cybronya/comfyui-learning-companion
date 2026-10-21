# ComfyuiZhangyuAPIImage2Node

## 节点类型

`ComfyuiZhangyuAPIImage2Node`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_01:IMAGE`（1 次）
- `image_02:IMAGE`（1 次）
- `image_03:IMAGE`（1 次）
- `image_04:IMAGE`（1 次）
- `image_05:IMAGE`（1 次）
- `image_06:IMAGE`（1 次）
- `image_07:IMAGE`（1 次）
- `image_08:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `api_key (API密钥):STRING`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `response:STRING`（1 次）
- `image_urls:STRING`（1 次）
- `chats:STRING`（1 次）
- `model_list:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "AUTO", "gpt-image-2", 1, "https://zhangyuapi.com/v1", "1K", "1:1", "auto", "b64_json", "jpeg", 85, 1550743992,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
