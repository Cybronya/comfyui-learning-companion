# SEGSDetailer

## 节点类型

`SEGSDetailer`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `segs:SEGS`（4 次）
- `basic_pipe:BASIC_PIPE`（4 次）
- `refiner_basic_pipe_opt:BASIC_PIPE`（4 次）
- `scheduler_func_opt:SCHEDULER_FUNC`（4 次）

## 输出

- `segs:SEGS`（4 次）
- `cnet_images:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, true, 1536, 0, "fixed", 10, 1.5, "euler", "normal", 0.5000000000000001, true, true, 0.2, 1, 1, false, 20]`（4 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
