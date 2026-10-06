# FaceDetailerPipe

## 节点类型

`FaceDetailerPipe`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `detailer_pipe:DETAILER_PIPE`（4 次）
- `scheduler_func_opt:SCHEDULER_FUNC`（4 次）
- `guide_size:FLOAT`（4 次）
- `guide_size_for:BOOLEAN`（4 次）
- `max_size:FLOAT`（4 次）
- `seed:INT`（4 次）
- `steps:INT`（4 次）
- `cfg:FLOAT`（4 次）
- `sampler_name:COMBO`（4 次）

## 输出

- `image:IMAGE`（4 次）
- `cropped_refined:IMAGE`（4 次）
- `cropped_enhanced_alpha:IMAGE`（4 次）
- `mask:MASK`（4 次）
- `detailer_pipe:DETAILER_PIPE`（4 次）
- `cnet_images:IMAGE`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, true, 4096, 503358268249446, "randomize", 16, 6, "er_sde", "simple", 0.24, 16, true, true, 0.38, 8, 4, "none", 4, `（1 次）
- `[512, true, 4096, 114662926858895, "randomize", 16, 6, "er_sde", "simple", 0.26, 16, true, true, 0.4, 8, 3, "none", 4, 0`（1 次）
- `[512, true, 4096, 987380626785891, "randomize", 16, 6, "er_sde", "simple", 0.3, 16, true, true, 0.44, 8, 3, "none", 4, 0`（1 次）
- `[512, true, 4096, 169155960518039, "randomize", 16, 6, "er_sde", "simple", 0.4, 16, true, true, 0.5, 8, 3, "none", 4, 0.`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
