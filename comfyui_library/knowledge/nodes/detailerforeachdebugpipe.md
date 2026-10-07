# DetailerForEachDebugPipe

## 节点类型

`DetailerForEachDebugPipe`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `segs:SEGS`（2 次）
- `basic_pipe:BASIC_PIPE`（2 次）
- `detailer_hook:DETAILER_HOOK`（2 次）
- `refiner_basic_pipe_opt:BASIC_PIPE`（2 次）
- `scheduler_func_opt:SCHEDULER_FUNC`（2 次）
- `wildcard:STRING`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `segs:SEGS`（2 次）
- `basic_pipe:BASIC_PIPE`（2 次）
- `cropped:IMAGE`（2 次）
- `cropped_refined:IMAGE`（2 次）
- `cropped_refined_alpha:IMAGE`（2 次）
- `cnet_images:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, true, 1024, 151181021749590, "randomize", 20, 3, "euler_ancestral", "karras", 0.4000000000000001, 5, true, true, "`（1 次）
- `[787.2001953125, true, 1024, 957008891035553, "randomize", 20, 3, "euler_ancestral", "karras", 0.3500000000000001, 5, tr`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
