# HD UltimateSDUpscale

## 节点类型

`HD UltimateSDUpscale`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（3 次）
- `model:MODEL`（3 次）
- `positive:CONDITIONING`（3 次）
- `negative:CONDITIONING`（3 次）
- `vae:VAE`（3 次）
- `upscale_model:UPSCALE_MODEL`（3 次）
- `seed:INT`（3 次）

## 输出

- `IMAGE:IMAGE`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[2, 580530866836954, "randomize", 20, 8, "euler_ancestral", "normal", 0.2, "Linear", 512, 512, 8, 32, "None", 1, 64, 8, `（2 次）
- `[2, 218003362412995, "randomize", 20, 8, "euler_ancestral", "normal", 0.2, "Linear", 512, 512, 8, 32, "None", 1, 64, 8, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
