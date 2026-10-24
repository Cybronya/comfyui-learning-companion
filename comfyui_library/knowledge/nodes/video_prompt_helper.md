# Video_Prompt_Helper

## 节点类型

`Video_Prompt_Helper`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `Language:COMBO`（1 次）
- `User Prompt:STRING`（1 次）
- `Shot Size:COMBO`（1 次）
- `Lighting Type:COMBO`（1 次）
- `Light Source:COMBO`（1 次）
- `Color Tone:COMBO`（1 次）
- `Camera Angle:COMBO`（1 次）
- `Lens:COMBO`（1 次）
- `Camera Movement Basic:COMBO`（1 次）
- `Camera Movement Advanced:COMBO`（1 次）

## 输出

- `generated_prompt:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["zh", "一个美丽的场景", "none", "none", "none", "none", "none", "none", "none", "none", "none", "none", "none", "none", "none"`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
