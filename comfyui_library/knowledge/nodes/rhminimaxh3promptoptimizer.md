# RHMiniMaxH3PromptOptimizer

## 节点类型

`RHMiniMaxH3PromptOptimizer`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image_1:IMAGE`（2 次）
- `image_2:IMAGE`（2 次）
- `image_3:IMAGE`（2 次）
- `image_4:IMAGE`（2 次）
- `image_5:IMAGE`（2 次）
- `video_1:VIDEO`（2 次）
- `video_2:VIDEO`（2 次）
- `idea:STRING`（2 次）
- `task:COMBO`（2 次）
- `duration_seconds:INT`（2 次）

## 输出

- `optimized_prompt:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "auto", 15, "none", "google/gemini-3.1-flash-lite-preview", "", 0, 0, 0, "", "", 0.7, 4096, 515678974, "randomize",`（1 次）
- `["", "auto", 15, "none", "google/gemini-3.1-flash-lite-preview", "", 0, 0, 0, "", "", 0.7, 4096, 389292337, "randomize",`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
