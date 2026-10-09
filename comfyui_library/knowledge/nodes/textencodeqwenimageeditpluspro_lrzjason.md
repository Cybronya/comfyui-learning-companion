# TextEncodeQwenImageEditPlusPro_lrzjason

## 节点类型

`TextEncodeQwenImageEditPlusPro_lrzjason`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `vae:VAE`（1 次）
- `image1:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `image4:IMAGE`（1 次）
- `image5:IMAGE`（1 次）
- `prompt:STRING`（1 次）
- `vl_resize_indexs:STRING`（1 次）
- `main_image_index:INT`（1 次）

## 输出

- `conditioning_with_full_ref:CONDITIONING`（1 次）
- `latent:LATENT`（1 次）
- `image1:IMAGE`（1 次）
- `image2:IMAGE`（1 次）
- `image3:IMAGE`（1 次）
- `image4:IMAGE`（1 次）
- `image5:IMAGE`（1 次）
- `conditioning_with_main_ref:CONDITIONING`（1 次）
- `pad_info:ANY`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["a woman of big breast", "1,2,3", 1, 1024, 384, "lanczos", "center", "Describe the key features of the input image (col`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
