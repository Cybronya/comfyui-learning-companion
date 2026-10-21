# DaSiWa_LLMPromptWriter

## 节点类型

`DaSiWa_LLMPromptWriter`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `images:IMAGE`（4 次）
- `model:COMBO`（4 次）
- `write_for:COMBO`（4 次）
- `start_with:STRING`（4 次）
- `idea:STRING`（4 次）
- `style:COMBO`（4 次）
- `detail:INT`（4 次）
- `creativity:INT`（4 次）
- `max_tokens:INT`（4 次）
- `seed:INT`（4 次）

## 输出

- `prompt:STRING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen3.5-9B-Q4_0.gguf", "Krea2", "", "", "None", 5, 5, 1024, 1601194782, "randomize", true]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
