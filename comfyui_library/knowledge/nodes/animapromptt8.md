# AnimaPromptT8

## 节点类型

`AnimaPromptT8`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive:STRING`（2 次）
- `negative:STRING`（2 次）
- `style:STRING`（2 次）
- `merge_separator:STRING`（2 次）

## 输出

- `POSITIVE:STRING`（2 次）
- `NEGATIVE:STRING`（2 次）
- `STYLE:STRING`（2 次）
- `MERGED_POSITIVE:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["score_9, score_8_up, score_7_up, masterpiece, best quality, highly detailed, anime style, beautiful face, detailed eye`（1 次）
- `["year 2026, newest, score_9,score_8,score_7,1girl, masterpiece, best quality, ultra detailed", "score_1, score_2, score`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
