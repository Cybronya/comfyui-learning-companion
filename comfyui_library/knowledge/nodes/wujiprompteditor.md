# WujiPromptEditor

## 节点类型

`WujiPromptEditor`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive_prompt:STRING`（1 次）
- `extra_requirements:STRING`（1 次）
- `aspect_ratio:COMBO`（1 次）
- `megapixels:FLOAT`（1 次）
- `batch_size:INT`（1 次）
- `multiple:INT`（1 次）
- `selected_styles:STRING`（1 次）
- `transparent_background:BOOLEAN`（1 次）
- `multi_line:BOOLEAN`（1 次）

## 输出

- `正面文本:STRING`（1 次）
- `额外要求:STRING`（1 次）
- `宽度:INT`（1 次）
- `高度:INT`（1 次）
- `潜空间:LATENT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", "3:4 (竖版标准)", 1, 1, 32, "[]", false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
