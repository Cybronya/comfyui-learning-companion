# QwenImage21_EditPromptRewrite

## 节点类型

`QwenImage21_EditPromptRewrite`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `image_1:IMAGE`（1 次）
- `image_2:IMAGE`（1 次）
- `image_3:IMAGE`（1 次）
- `image_4:IMAGE`（1 次）
- `image_5:IMAGE`（1 次）
- `image_6:IMAGE`（1 次）
- `image_7:IMAGE`（1 次）
- `image_8:IMAGE`（1 次）
- `image_9:IMAGE`（1 次）

## 输出

- `positive_prompt:STRING`（1 次）
- `negative_prompt:STRING`（1 次）
- `wh_ratio:STRING`（1 次）
- `ratio_follow:STRING`（1 次）
- `thinking:STRING`（1 次）
- `parse_ok:BOOLEAN`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 0.68, 0.95, 0, 24000, 3429296618, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
