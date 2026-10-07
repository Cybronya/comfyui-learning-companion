# KSamplerAdvancedProvider

## 节点类型

`KSamplerAdvancedProvider`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `basic_pipe:BASIC_PIPE`（4 次）
- `sampler_opt:SAMPLER`（4 次）
- `scheduler_func_opt:SCHEDULER_FUNC`（4 次）

## 输出

- `KSAMPLER_ADVANCED:KSAMPLER_ADVANCED`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "deis", "beta", 1]`（2 次）
- `[5, "dpmpp_2m", "AYS SDXL", 1]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
