# PromptSelectorSingleCHAOS

## 节点类型

`PromptSelectorSingleCHAOS`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `mode_code:INT`（1 次）
- `selection_mode:COMBO`（1 次）
- `fixed_index:INT`（1 次）
- `seed:INT`（1 次）
- `F_portrait:STRING`（1 次）
- `F_half:STRING`（1 次）
- `F_full:STRING`（1 次）
- `F_custom:STRING`（1 次）
- `M_portrait:STRING`（1 次）
- `M_half:STRING`（1 次）

## 输出

- `prompt:STRING`（1 次）
- `prompt_info:STRING`（1 次）
- `mode_name:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, "random", 0, 1003, "randomize", "A professional portrait captures the captivating beauty of a young girl. Soft, diff`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
