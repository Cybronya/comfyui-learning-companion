# easy preSamplingDynamicCFG

## 节点类型

`easy preSamplingDynamicCFG`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `pipe:PIPE_LINE`（2 次）
- `image_to_latent:IMAGE`（2 次）
- `latent:LATENT`（2 次）
- `steps:INT`（2 次）
- `cfg:FLOAT`（2 次）
- `cfg_mode:COMBO`（2 次）
- `cfg_scale_min:FLOAT`（2 次）
- `sampler_name:COMBO`（2 次）
- `scheduler:COMBO`（2 次）
- `denoise:FLOAT`（2 次）

## 输出

- `pipe:PIPE_LINE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[30, 5, "Constant", 3.5, "dpmpp_2m_sde", "karras", 1, 1074528687505226, "randomize"]`（1 次）
- `[20, 8, "Constant", 3.5, "euler", "normal", 1, 1109322060008863, "randomize"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
