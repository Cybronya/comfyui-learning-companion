# PromptComposerCustomLists

## 节点类型

`PromptComposerCustomLists`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `text_in_opt:STRING`（2 次）
- `effect:COMBO`（2 次）
- `effect_weight:FLOAT`（2 次）
- `lens_type:COMBO`（2 次）
- `lens_type_weight:FLOAT`（2 次）
- `painting_style:COMBO`（2 次）
- `painting_style_weight:FLOAT`（2 次）
- `photo_style:COMBO`（2 次）
- `photo_style_weight:FLOAT`（2 次）
- `active:BOOLEAN`（2 次）

## 输出

- `text_out:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Oil Painting", 1, "wide-angle photo", 1, "Surrealism", 1, "-", 1, true]`（1 次）
- `["-", 1, "-", 1, "-", 1, "-", 1, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
