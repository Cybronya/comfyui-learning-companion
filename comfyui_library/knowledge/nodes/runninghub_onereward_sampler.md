# RunningHub OneReward Sampler

## 节点类型

`RunningHub OneReward Sampler`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `pipeline:RHOneRewardPipeline`（1 次）
- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `prompt:STRING`（1 次）
- `num_inference_steps:INT`（1 次）
- `guidance_scale:FLOAT`（1 次）
- `true_cfg:FLOAT`（1 次）
- `seed:INT`（1 次）

## 输出

- `image:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 50, 1, 4, 534738515211370, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
