# Kimodo_Sampler

## 节点类型

`Kimodo_Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:KIMODO_MODEL`（1 次）
- `conditioning:KIMODO_COND`（1 次）
- `duration:FLOAT`（1 次）
- `seed:INT`（1 次）
- `num_samples:INT`（1 次）
- `diffusion_steps:INT`（1 次）
- `constraints_json:STRING`（1 次）

## 输出

- `motion:KIMODO_MOTION`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[5, 28420262, "randomize", 1, 100, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
