# PixelKSampleUpscalerProvider

## 节点类型

`PixelKSampleUpscalerProvider`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（1 次）
- `vae:VAE`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `upscale_model_opt:UPSCALE_MODEL`（1 次）
- `pk_hook_opt:PK_HOOK`（1 次）
- `scheduler_func_opt:SCHEDULER_FUNC`（1 次）
- `seed:INT`（1 次）

## 输出

- `UPSCALER:UPSCALER`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["nearest-exact", 769430016755031, "randomize", 20, 7, "dpmpp_sde", "karras", 0.5, false, 512]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
