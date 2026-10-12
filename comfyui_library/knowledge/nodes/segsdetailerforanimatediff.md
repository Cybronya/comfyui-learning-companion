# SEGSDetailerForAnimateDiff

## 节点类型

`SEGSDetailerForAnimateDiff`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image_frames:IMAGE`（1 次）
- `segs:SEGS`（1 次）
- `basic_pipe:BASIC_PIPE`（1 次）
- `refiner_basic_pipe_opt:BASIC_PIPE`（1 次）
- `scheduler_func_opt:SCHEDULER_FUNC`（1 次）

## 输出

- `segs:SEGS`（1 次）
- `cnet_images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[256, true, 768, 1033752348837856, "randomize", 12, 7, "euler", "normal", 0.45, 0.2, 20]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
