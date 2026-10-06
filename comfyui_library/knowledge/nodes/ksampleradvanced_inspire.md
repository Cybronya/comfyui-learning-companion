# KSamplerAdvanced //Inspire

## 节点类型

`KSamplerAdvanced //Inspire`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `model:MODEL`（3 次）
- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `latent_image:LATENT`（3 次）
- `noise_opt:NOISE_IMAGE`（3 次）
- `scheduler_func_opt:SCHEDULER_FUNC`（3 次）
- `noise_seed:INT`（3 次）

## 输出

- `LATENT:LATENT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 54591659018366, "randomize", 30, 3, "lcm", "karras", 0, 30, "GPU(=A1111)", false, "incremental", 0, 0, "linear"]`（1 次）
- `[true, 457091645746120, "randomize", 30, 3, "lcm", "karras", 5, 30, "GPU(=A1111)", false, "incremental", 0, 0, "linear"]`（1 次）
- `[true, 523616548034404, "randomize", 30, 3, "lcm", "karras", 0, 30, "GPU(=A1111)", false, "incremental", 0, 0, "linear"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
