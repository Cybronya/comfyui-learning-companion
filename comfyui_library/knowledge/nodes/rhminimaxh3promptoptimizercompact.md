# RHMiniMaxH3PromptOptimizerCompact

## 节点类型

`RHMiniMaxH3PromptOptimizerCompact`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_1:IMAGE`（1 次）
- `image_2:IMAGE`（1 次）
- `image_3:IMAGE`（1 次）
- `image_4:IMAGE`（1 次）
- `image_5:IMAGE`（1 次）
- `video_1:VIDEO`（1 次）
- `video_2:VIDEO`（1 次）
- `prompt:STRING`（1 次）
- `task:COMBO`（1 次）
- `duration_seconds:INT`（1 次）

## 输出

- `optimized_prompt:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "ref2va", 5, "none", "openai/gpt-5.4-mini", 0.7, 4096, 320585463, "randomize", 180]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
