# H3LatentUpscaleByJingchen573

## 节点类型

`H3LatentUpscaleByJingchen573`

## 分类

Upscale

## 作用

放大类节点：提升图像/视频分辨率（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `samples:LATENT`（3 次）
- `upscale_method:COMBO`（3 次）
- `scale_by:FLOAT`（3 次）

## 输出

- `LATENT:LATENT`（3 次）
- `width:INT`（3 次）
- `height:INT`（3 次）
- `effective_scale_x:FLOAT`（3 次）
- `effective_scale_y:FLOAT`（3 次）
- `alignment_info:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["nearest-exact", 1]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
