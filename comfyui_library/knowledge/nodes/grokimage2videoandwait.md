# GrokImage2VideoAndWait

## 节点类型

`GrokImage2VideoAndWait`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:STRING`（1 次）
- `prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `size:COMBO`（1 次）
- `api_key:STRING`（1 次）
- `api_base:STRING`（1 次）
- `custom_model:STRING`（1 次）
- `max_wait_time:INT`（1 次）
- `poll_interval:INT`（1 次）

## 输出

- `任务ID:STRING`（1 次）
- `状态:STRING`（1 次）
- `视频URL:STRING`（1 次）
- `增强提示词:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "grok-video-3 (6秒)", "3:2", "720P", "", "https://api.kegeai.top", "", 1200, 10]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
