# SDXLPromptStylerAdvanced

## 节点类型

`SDXLPromptStylerAdvanced`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输出

- `text_positive_g:STRING`（3 次）
- `text_positive_l:STRING`（3 次）
- `text_positive:STRING`（3 次）
- `text_negative_g:STRING`（3 次）
- `text_negative_l:STRING`（3 次）
- `text_negative:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["masterpiece, best quality, anime style, very aesthetic, 8k resolution,  ", "1girl, red hair, twintails, blue eyes, sch`（1 次）
- `["masterpiece, best quality, very aesthetic, 8k resolution,  ", "", "", "sai-cinematic", "Both", "Yes"]`（1 次）
- `["", "1 girl", "", "sai-anime", "Both", "Yes"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
