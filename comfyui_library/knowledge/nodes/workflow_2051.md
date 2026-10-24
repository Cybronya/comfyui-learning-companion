# workflow/图像尺寸

## 节点类型

`workflow/图像尺寸`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `模型:MODEL`（1 次）
- `CLIP:CLIP`（1 次）
- `CLIPTextEncode clip:CLIP`（1 次）
- `图像:IMAGE`（1 次）
- `参考图像大小:IMAGE`（1 次）
- `ImageResizeKJ image:IMAGE`（1 次）
- `ImageResizeKJ get_image_size:IMAGE`（1 次）
- `CLIP视觉:CLIP_VISION`（1 次）
- `风格模型:STYLE_MODEL`（1 次）
- `正面条件:CONDITIONING`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `宽度:INT`（1 次）
- `高度:INT`（1 次）
- `ImageResizeKJ 图像:IMAGE`（1 次）
- `ImageResizeKJ 宽度:INT`（1 次）
- `ImageResizeKJ 高度:INT`（1 次）
- `条件:CONDITIONING`（1 次）
- `Latent:LATENT`（1 次）
- `VAEDecode 图像:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 1280, 1280, "nearest-exact", true, 2, "disabled", 1280, 1280, "nearest-exact", true, 2, "disabled", 30, "center`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
