# LatentUpscaleBy

## 节点类型

`LatentUpscaleBy`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `samples:LATENT`（4 次）
- `upscale_method:COMBO`（4 次）
- `scale_by:FLOAT`（4 次）

## 输出

- `LATENT:LATENT`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["nearest-exact", 1.5000000000000002]`（1 次）
- `["bislerp", 1.5]`（1 次）
- `["nearest-exact", 1]`（1 次）
- `["nearest-exact", 1.5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
