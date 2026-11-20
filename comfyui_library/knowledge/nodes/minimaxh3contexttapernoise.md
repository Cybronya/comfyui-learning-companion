# MiniMaxH3ContextTaperNoise

## 节点类型

`MiniMaxH3ContextTaperNoise`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `tail_frames:INT`（1 次）
- `alpha:FLOAT`（1 次）
- `alpha_end:FLOAT`（1 次）
- `ramp_frames:INT`（1 次）
- `seed:INT`（1 次）
- `pattern:COMBO`（1 次）
- `grid_mode:COMBO`（1 次）
- `block_size:INT`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `alpha_schedule:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[22, 0.55, 0, 3, 0, "fixed", "poc_chroma_blocks", "poc_36x64", 16]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
