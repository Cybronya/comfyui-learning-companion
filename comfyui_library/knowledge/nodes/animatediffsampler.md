# AnimateDiffSampler

## 节点类型

`AnimateDiffSampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `motion_module:MOTION_MODULE`（2 次）
- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `latent_image:LATENT`（2 次）
- `sliding_window_opts:SLIDING_WINDOW_OPTS`（2 次）
- `seed:INT`（2 次）

## 输出

- `LATENT:LATENT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["default", 47, 642264967220193, "fixed", 6, 10, "lcm", "normal", 1]`（1 次）
- `["default", 47, 642264967220193, "fixed", 6, 9, "euler_ancestral", "normal", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
