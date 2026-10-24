# MaskDetailerPipe

## 节点类型

`MaskDetailerPipe`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `mask:MASK`（4 次）
- `basic_pipe:BASIC_PIPE`（4 次）
- `refiner_basic_pipe_opt:BASIC_PIPE`（4 次）
- `detailer_hook:DETAILER_HOOK`（4 次）
- `scheduler_func_opt:SCHEDULER_FUNC`（4 次）
- `guide_size:FLOAT`（3 次）
- `guide_size_for:BOOLEAN`（3 次）
- `max_size:FLOAT`（3 次）
- `mask_mode:BOOLEAN`（3 次）

## 输出

- `image:IMAGE`（4 次）
- `cropped_refined:IMAGE`（4 次）
- `cropped_enhanced_alpha:IMAGE`（4 次）
- `basic_pipe:BASIC_PIPE`（4 次）
- `refiner_basic_pipe_opt:BASIC_PIPE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, true, 1024, true, 45217413249826, "fixed", 5, 2, "dpmpp_sde", "karras", 0.5, 5, 3, 10, 0.2, 1, 1, false, 20, false`（2 次）
- `[1024, true, 1024, true, 888888, "fixed", 6, 1, "euler", "simple", 0.5, 5, 3, 10, 0.2, 1, 1, true, 20, false, true]`（1 次）
- `[1024, true, 1536, true, 1003, "fixed", 20, 1, "euler", "normal", 1, 5, 10, 10, 1, 1, 1, true, 20, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
