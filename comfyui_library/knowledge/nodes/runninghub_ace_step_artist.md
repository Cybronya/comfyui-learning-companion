# RunningHub ACE-Step Artist

## 节点类型

`RunningHub ACE-Step Artist`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `llm_handler:ACEStepLLM`（2 次）
- `prompt:STRING`（2 次）
- `vocal_language:COMBO`（2 次）
- `instrumental:BOOLEAN`（2 次）
- `seed:INT`（2 次）

## 输出

- `generation params:ACEStepGenerationParams`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "Chinese (zh)", true, 917040683, "randomize"]`（1 次）
- `["一首中国风伤感恋爱纯音乐", "Chinese (zh)", true, 2835317155, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
