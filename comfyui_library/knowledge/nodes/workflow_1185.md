# workflow>采样

## 节点类型

`workflow>采样`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `CLIP:CLIP`（1 次）
- `模型:MODEL`（1 次）
- `seed:INT`（1 次）
- `sampler_name:COMBO`（1 次）
- `text:STRING`（1 次）
- `dishonesty_factor:FLOAT`（1 次）
- `start_percent:FLOAT`（1 次）
- `end_percent:FLOAT`（1 次）
- `smooth_factor:FLOAT`（1 次）
- `scheduler:COMBO`（1 次）

## 输出

- `随机种:INT`（1 次）
- `条件:CONDITIONING`（1 次）
- `SAMPLER:SAMPLER`（1 次）
- `Sigmas:SIGMAS`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[69599948924957, "randomize", "dpmpp_2m", "low quality, blurry, anatomical errors, wrong proportions, distorted face, un`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
