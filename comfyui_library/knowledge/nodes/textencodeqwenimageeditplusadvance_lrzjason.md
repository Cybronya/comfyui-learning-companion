# TextEncodeQwenImageEditPlusAdvance_lrzjason

## 节点类型

`TextEncodeQwenImageEditPlusAdvance_lrzjason`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `clip:CLIP`（5 次）
- `vae:VAE`（5 次）
- `vl_resize_image1:IMAGE`（5 次）
- `vl_resize_image2:IMAGE`（5 次）
- `vl_resize_image3:IMAGE`（5 次）
- `not_resize_image1:IMAGE`（5 次）
- `not_resize_image2:IMAGE`（5 次）
- `not_resize_image3:IMAGE`（5 次）
- `prompt:STRING`（5 次）
- `target_size:COMBO`（5 次）

## 输出

- `conditioning_with_full_ref:CONDITIONING`（5 次）
- `latent:LATENT`（5 次）
- `target_image1:IMAGE`（5 次）
- `target_image2:IMAGE`（5 次）
- `target_image3:IMAGE`（5 次）
- `vl_resized_image1:IMAGE`（5 次）
- `vl_resized_image2:IMAGE`（5 次）
- `vl_resized_image3:IMAGE`（5 次）
- `conditioning_with_first_ref:CONDITIONING`（5 次）
- `pad_info:ANY`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["让图1的人物穿上图2人物的衣服", 1536, 384, "lanczos", "pad", "Describe the key features of the input image (color, shape, size, text`（3 次）
- `["移除图片1中的红颜色", 1024, 384, "lanczos", "pad", "Describe the key features of the input image (color, shape, size, texture, `（1 次）
- `["", 1024, 384, "lanczos", "pad", "Describe the key features of the input image (color, shape, size, texture, objects, b`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
