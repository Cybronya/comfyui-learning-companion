# SoraQueryTask

## 节点类型

`SoraQueryTask`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `task_id:STRING`（1 次）
- `api_base:STRING`（1 次）
- `api_key:STRING`（1 次）
- `wait:BOOLEAN`（1 次）
- `poll_interval_sec:INT`（1 次）
- `timeout_sec:INT`（1 次）

## 输出

- `状态:STRING`（1 次）
- `视频URL:STRING`（1 次）
- `GIF_URL:STRING`（1 次）
- `缩略图URL:STRING`（1 次）
- `原始响应JSON:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "https://api.kuai.host", "", true, 10, 1800]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
