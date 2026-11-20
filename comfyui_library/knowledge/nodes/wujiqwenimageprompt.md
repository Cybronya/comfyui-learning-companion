# WujiQwenImagePrompt

## 节点类型

`WujiQwenImagePrompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `助力源:WUJI_LLM`（1 次）
- `reference_images.reference_image_0:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `constraints:STRING`（1 次）
- `meta_instruction:STRING`（1 次）
- `meta_preset:COMBO`（1 次）
- `rewrite_mode:COMBO`（1 次）
- `transparent_background:BOOLEAN`（1 次）
- `multi_line:BOOLEAN`（1 次）
- `seed:INT`（1 次）

## 输出

- `图像提示词:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["（无手动提示词）", "", "", "双重曝光", "关闭", false, false, 424641823, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
