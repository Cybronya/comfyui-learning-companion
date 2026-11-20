# Sa2VAVideoReversePrompt

## 节点类型

`Sa2VAVideoReversePrompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:SA2VA_MODEL`（1 次）
- `video:VIDEO`（1 次）
- `preset:COMBO`（1 次）
- `custom_prompt:STRING`（1 次）
- `max_frames:INT`（1 次）
- `llm_frames:INT`（1 次）
- `max_new_tokens:INT`（1 次）

## 输出

- `prompt:STRING`（1 次）
- `raw:STRING`（1 次）
- `masks:MASK`（1 次）
- `seg_count:INT`（1 次）
- `frames:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["describe", "详细描述视频内容", 16, 12, 512]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
