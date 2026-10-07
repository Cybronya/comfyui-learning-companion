# WanVideoPromptExtender

## 节点类型

`WanVideoPromptExtender`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `qwen:QWENMODEL`（1 次）
- `custom_system_prompt:STRING`（1 次）
- `prompt:STRING`（1 次）
- `max_new_tokens:INT`（1 次）
- `device:COMBO`（1 次）
- `force_offload:BOOLEAN`（1 次）
- `system_prompt:COMBO`（1 次）
- `seed:INT`（1 次）

## 输出

- `STRING:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["一个仙女", 512, "gpu", true, "T2V Movie Director (Chinese)", 100292835055106, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
