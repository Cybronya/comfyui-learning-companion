# DetailerForEachPipe

## 节点类型

`DetailerForEachPipe`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `segs:SEGS`（1 次）
- `basic_pipe:BASIC_PIPE`（1 次）
- `detailer_hook:DETAILER_HOOK`（1 次）
- `refiner_basic_pipe_opt:BASIC_PIPE`（1 次）
- `scheduler_func_opt:SCHEDULER_FUNC`（1 次）
- `guide_size:FLOAT`（1 次）
- `guide_size_for:BOOLEAN`（1 次）
- `max_size:FLOAT`（1 次）
- `seed:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）
- `segs:SEGS`（1 次）
- `basic_pipe:BASIC_PIPE`（1 次）
- `cnet_images:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, true, 1024, 0, "randomize", 20, 8, "euler", "simple", 0.5, 5, true, true, "", 0.2, 1, false, 20, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
