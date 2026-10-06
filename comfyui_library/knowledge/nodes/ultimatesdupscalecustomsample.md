# UltimateSDUpscaleCustomSample

## 节点类型

`UltimateSDUpscaleCustomSample`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `model:MODEL`（3 次）
- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `vae:VAE`（3 次）
- `upscale_model:UPSCALE_MODEL`（3 次）
- `custom_sampler:SAMPLER`（3 次）
- `custom_sigmas:SIGMAS`（3 次）
- `seed:INT`（3 次）
- `cfg:FLOAT`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, 510496990812670, "randomize", 4, 3.5, "euler", "beta", 0, "Linear", 1024, 1024, 8, 32, "None", 1, 64, 8, 16, true, f`（1 次）
- `[2, 970193660780313, "randomize", 4, 3.5, "euler", "beta", 0.01, "Linear", 1024, 1024, 8, 32, "None", 1, 64, 8, 16, true`（1 次）
- `[["545", 0], 841170276833792, "randomize", 4, 1, "euler", "kl_optimal", 0.5000000000000001, "Linear", 1024, 1024, 64, 64`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
