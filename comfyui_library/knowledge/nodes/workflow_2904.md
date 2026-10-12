# workflow>重要

## 节点类型

`workflow>重要`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `images:IMAGE`（2 次）
- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `noise_seed:INT`（2 次）
- `sigmas:STRING`（2 次）
- `sampler_name:COMBO`（2 次）
- `ManualSigmas sigmas:STRING`（2 次）
- `model_name:COMBO`（2 次）
- `RandomNoise noise_seed:INT`（2 次）

## 输出

- `CLIP:CLIP`（2 次）
- `Lora Loader Stack (rgthree) CLIP:CLIP`（2 次）
- `batch_size:INT`（2 次）
- `denoised_output:LATENT`（2 次）
- `output:LATENT`（2 次）
- `VIDEO:VIDEO`（2 次）
- `Lora Loader Stack (rgthree) 20 CLIP:CLIP`（1 次）
- `Lora Loader Stack (rgthree) 17 CLIP:CLIP`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[21900892019488, "randomize", "1., 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0", "euler", "0.8025, 0`（1 次）
- `["1., 0.99375, 0.9875, 0.98125, 0.975, 0.909375, 0.725, 0.421875, 0.0", "euler", "0.8025, 0.6332, 0.4525, 0.2425, 0.0", `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
