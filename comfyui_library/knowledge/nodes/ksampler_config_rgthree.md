# KSampler Config (rgthree)

## 节点类型

`KSampler Config (rgthree)`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `steps_total:INT`（3 次）
- `refiner_step:INT`（3 次）
- `cfg:FLOAT`（3 次）
- `sampler_name:COMBO`（3 次）
- `scheduler:COMBO`（3 次）

## 输出

- `STEPS:INT`（3 次）
- `REFINER_STEP:INT`（3 次）
- `CFG:FLOAT`（3 次）
- `SAMPLER:COMBO`（3 次）
- `SCHEDULER:COMBO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[28, 24, 5, "res_multistep", "linear_quadratic"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
