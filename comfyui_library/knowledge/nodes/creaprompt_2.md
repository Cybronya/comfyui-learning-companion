# CreaPrompt_2

## 节点类型

`CreaPrompt_2`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `Man:COMBO`（1 次）
- `Celebrity_Man:COMBO`（1 次）
- `Haircuts_Thomas_Buyle:COMBO`（1 次）
- `Haircolors_Thomas_Buyle:COMBO`（1 次）
- `Places:COMBO`（1 次）
- `Image_Quality:COMBO`（1 次）
- `Cameras:COMBO`（1 次）
- `Lighting:COMBO`（1 次）
- `Prompt_count:INT`（1 次）
- `CreaPrompt_Collection:COMBO`（1 次）

## 输出

- `prompt:STRING`（1 次）
- `seed:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["disabled", "🎲random", "disabled", "disabled", "disabled", "disabled", "disabled", "disabled", 1, "disabled", 780275709`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
