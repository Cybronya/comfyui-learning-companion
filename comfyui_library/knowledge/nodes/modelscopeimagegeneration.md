# ModelScopeImageGeneration

## 节点类型

`ModelScopeImageGeneration`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model_url:STRING`（1 次）
- `task_status_url:STRING`（1 次）
- `api_key:STRING`（1 次）
- `model:STRING`（1 次）
- `prompt:STRING`（1 次）
- `max_wait_time:INT`（1 次）
- `polling_interval:INT`（1 次）
- `negative_prompt:STRING`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `status:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["https://api-inference.modelscope.cn/v1/images/generations", "https://api-inference.modelscope.cn/v1/tasks", "ms-4fe381`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
