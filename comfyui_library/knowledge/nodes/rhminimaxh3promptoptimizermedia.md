# RHMiniMaxH3PromptOptimizerMedia

## 节点类型

`RHMiniMaxH3PromptOptimizerMedia`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 8 个 workflow 中。

## 输入

- `image_1:IMAGE`（8 次）
- `image_2:IMAGE`（8 次）
- `image_3:IMAGE`（8 次）
- `image_4:IMAGE`（8 次）
- `image_5:IMAGE`（8 次）
- `video_1:VIDEO`（8 次）
- `prompt:STRING`（8 次）
- `task:COMBO`（8 次）
- `duration_seconds:FLOAT`（8 次）
- `style:COMBO`（8 次）

## 输出

- `optimized_prompt:STRING`（8 次）
- `image_1:IMAGE`（8 次）
- `image_2:IMAGE`（8 次）
- `image_3:IMAGE`（8 次）
- `image_4:IMAGE`（8 次）
- `image_5:IMAGE`（8 次）
- `image_6:IMAGE`（8 次）
- `image_7:IMAGE`（8 次）
- `image_8:IMAGE`（8 次）
- `image_9:IMAGE`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "auto", 5, "none", "qwen/qwen3.8-max", 0.7, 8192, 108908176, "randomize", 180]`（5 次）
- `["", "auto", 5, "none", "qwen/qwen3.8-max", 0.7, 8192, 1120454070, "randomize", 180]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
