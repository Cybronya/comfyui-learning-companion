# KSamplerAdvanced

## 节点类型

`KSamplerAdvanced`

## 分类

Sampling

## 作用

采样类节点：执行扩散去噪（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 33 个 workflow 中。

## 输入

- `model:MODEL`（61 次）
- `positive:CONDITIONING`（61 次）
- `negative:CONDITIONING`（61 次）
- `latent_image:LATENT`（61 次）
- `add_noise:COMBO`（61 次）
- `noise_seed:INT`（61 次）
- `steps:INT`（61 次）
- `cfg:FLOAT`（61 次）
- `sampler_name:COMBO`（61 次）
- `scheduler:COMBO`（61 次）

## 输出

- `LATENT:LATENT`（61 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["enable", 814571185709278, "fixed", 12, 1, "euler", "simple", 8, 10000, "disable"]`（5 次）
- `["disable", 629720711683578, "randomize", 16, 1.2, "res_2s", "simple", 8, 1000, "disable"]`（4 次）
- `["enable", 1099946684369635, "randomize", 16, 2, "sa_solver", "beta", 0, 8, "enable"]`（4 次）
- `["enable", 734061230122947, "randomize", 12, 1, "euler", "simple", 8, 10000, "disable"]`（3 次）
- `["disable", 71120889683296, "randomize", 3, 1, "euler", "simple", 0, 10000, "disable"]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
