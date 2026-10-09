# QwenVideoNode

## 节点类型

`QwenVideoNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `video:VIDEO`（1 次）
- `prompt:STRING`（1 次）
- `api_token:STRING`（1 次）
- `video_path:STRING`（1 次）
- `model:STRING`（1 次）
- `max_tokens:INT`（1 次）
- `temperature:FLOAT`（1 次）
- `seed:INT`（1 次）
- `cloudinary_cloud_name:STRING`（1 次）
- `cloudinary_api_key:STRING`（1 次）

## 输出

- `description:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["详细描述一下这个视频", "", "", "Qwen/Qwen3-VL-235B-A22B-Instruct", 1000, 0.7, 1181462472, "randomize", "", "", ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
