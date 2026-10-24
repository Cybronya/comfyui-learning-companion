# CR SDXL Prompt Mixer

## 节点类型

`CR SDXL Prompt Mixer`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prompt_positive:STRING`（1 次）
- `prompt_negative:STRING`（1 次）
- `style_positive:STRING`（1 次）
- `style_negative:STRING`（1 次）
- `preset:COMBO`（1 次）

## 输出

- `pos_g:STRING`（1 次）
- `pos_l:STRING`（1 次）
- `pos_r:STRING`（1 次）
- `neg_g:STRING`（1 次）
- `neg_l:STRING`（1 次）
- `neg_r:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["The image is a beautiful landscape of a mountain range with pink rhododendrons in full bloom. The sky is a soft pink c`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
