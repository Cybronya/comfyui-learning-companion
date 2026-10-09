# DoubaoLLMNode

## 节点类型

`DoubaoLLMNode`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `video_frames:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `api_key:STRING`（1 次）
- `thinking_mode:COMBO`（1 次）
- `temperature:FLOAT`（1 次）
- `max_tokens:INT`（1 次）
- `stream:BOOLEAN`（1 次）
- `timeout:INT`（1 次）
- `system_prompt:STRING`（1 次）

## 输出

- `response:STRING`（1 次）
- `thinking_content:STRING`（1 次）
- `conversation_json:STRING`（1 次）
- `total_tokens:FLOAT`（1 次）
- `thinking_tokens:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "auto", 0.7, 4096, false, 60, "", "", 138936325, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
